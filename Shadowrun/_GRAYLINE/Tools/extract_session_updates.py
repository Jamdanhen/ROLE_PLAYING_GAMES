#!/usr/bin/env python3
"""
Create staged campaign extraction files from one finalized session log.

This script does not modify source logs or canon files. It only writes:
- SESSION_###_extraction.json
- SESSION_###_extraction_review.md
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ENTITY_TYPES = {
    "pcs": [
        "pc",
        "pcs",
        "player character",
        "player characters",
        "runner",
        "runners",
    ],
    "npcs": ["npc", "npcs", "contact", "contacts"],
    "factions": ["faction", "factions", "gang", "corp", "corporation", "agency", "organization"],
    "locations": ["location", "locations", "place", "places", "district", "site"],
    "jobs": ["job", "jobs", "run", "runs", "mission", "missions", "contract"],
    "clues": ["clue", "clues", "lead", "leads", "evidence", "intel"],
    "threads": ["thread", "threads", "plot", "plots", "arc", "arcs", "loose end"],
    "items_or_artifacts": ["item", "items", "artifact", "artifacts", "gear", "object", "objects"],
}

UPDATE_BUCKETS = {
    "pcs": "pc_updates",
    "npcs": "npc_updates",
    "factions": "faction_updates",
    "locations": "location_updates",
    "jobs": "job_updates",
    "clues": "clue_updates",
    "threads": "thread_updates",
    "items_or_artifacts": "item_or_artifact_updates",
}

RECOMMENDED_AREAS = {
    "pcs": "PC files",
    "npcs": "NPC files",
    "factions": "Faction files",
    "locations": "Location files",
    "jobs": "Job files",
    "clues": "Clue files",
    "threads": "Thread files",
    "items_or_artifacts": "Items or artifacts files",
}

COMMON_ENTITY_FALSE_POSITIVES = {
    "act",
    "actors",
    "advanced",
    "bikes",
    "chapter",
    "clock",
    "delivered",
    "first",
    "hired",
    "last",
    "local",
    "loot",
    "lost",
    "new",
    "old",
    "optional",
    "origin",
    "player-facing",
    "recovered",
    "retrieval",
    "run",
    "scene",
    "session",
    "six",
    "squatter",
    "updated",
    "update",
    "version",
    "unknown",
}

DOCUMENT_STATUS_FALSE_POSITIVES = {
    "updated canon version",
    "loot recovered",
}

KNOWN_PCS = {
    "switch",
    "kilmer",
    "the chin",
}

KNOWN_FACTIONS = {
    "boeing",
    "brigada 12",
    "burnouts",
    "burnouts gang",
    "chinese triads",
    "kestrel",
    "kestrel defense systems",
    "lone star",
    "russian mafia",
}

KNOWN_ITEMS_OR_ARTIFACTS = {
    "box truck",
    "burner phone",
    "crate",
    "drone craft",
    "light pistols",
    "modified pager/tracker",
    "prototype bug detector",
    "the doughnut",
    "uzi",
}

KNOWN_LOCATIONS = {
    "gray line district",
    "north side",
    "pier 12",
    "pier 15",
    "rusty spade",
    "siberian wolf",
    "south side",
}

DATE_PATTERNS = [
    re.compile(r"\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|"
               r"Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)"
               r"\s+\d{1,2},?\s+\d{4}\b", re.I),
    re.compile(r"\b\d{4}-\d{2}-\d{2}\b"),
    re.compile(r"\b\d{1,2}/\d{1,2}/\d{2,4}\b"),
]

UPDATE_VERBS = [
    "accepted",
    "acquired",
    "activated",
    "agreed",
    "ambushed",
    "arrested",
    "attacked",
    "betrayed",
    "blackmailed",
    "captured",
    "changed",
    "completed",
    "compromised",
    "confirmed",
    "contacted",
    "created",
    "damaged",
    "decided",
    "declined",
    "defeated",
    "delivered",
    "destroyed",
    "discovered",
    "escaped",
    "exposed",
    "failed",
    "finished",
    "found",
    "gave",
    "gained",
    "hired",
    "identified",
    "injured",
    "killed",
    "learned",
    "left",
    "lost",
    "made",
    "met",
    "moved",
    "opened",
    "paid",
    "promised",
    "received",
    "recovered",
    "refused",
    "revealed",
    "secured",
    "sold",
    "stole",
    "survived",
    "took",
    "traded",
    "triggered",
    "uncovered",
    "updated",
]

UNCERTAINTY_MARKERS = [
    "unclear",
    "unknown",
    "maybe",
    "possibly",
    "probably",
    "not sure",
    "tbd",
    "???",
    "[?]",
]


@dataclass(frozen=True)
class Line:
    number: int
    text: str


def empty_extraction() -> dict[str, Any]:
    return {
        "session_identity": {
            "session_number": "",
            "real_world_date": "",
            "in_game_date": "",
            "in_game_time_passage": "",
            "primary_locations": [],
            "participating_pcs": [],
        },
        "entities": {
            "pcs": [],
            "npcs": [],
            "factions": [],
            "locations": [],
            "jobs": [],
            "clues": [],
            "threads": [],
            "items_or_artifacts": [],
        },
        "updates": {
            "npc_updates": [],
            "faction_updates": [],
            "location_updates": [],
            "pc_updates": [],
            "job_updates": [],
            "clue_updates": [],
            "thread_updates": [],
            "item_or_artifact_updates": [],
        },
        "structured_session_updates": [],
        "retrofit_structured_updates": [],
        "agnostic_structured_updates": [],
        "preserved_fragile_details": [],
        "downstream_file_impacts": [],
        "reconciliation_flags": [],
        "user_decisions_required": [],
        "_skip_update_lines": [],
    }


def read_text(path: Path) -> str:
    for encoding in ("utf-8-sig", "utf-8", "cp1252"):
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue
    return path.read_text(errors="replace")


def normalize_name(name: str) -> str:
    name = re.sub(r"^[#*\-\s:]+", "", name.strip())
    name = re.sub(r"\s+", " ", name)
    return name.strip(" .,:;\"'")


def split_list(value: str) -> list[str]:
    value = re.sub(r"\([^)]*\)", "", value)
    parts = re.split(r"\s*(?:,|;|\||/|\band\b)\s*", value)
    return unique_sorted(normalize_name(part) for part in parts if normalize_name(part))


def unique_sorted(values: Any) -> list[str]:
    seen = {}
    for value in values:
        if value:
            key = value.lower()
            if key not in seen:
                seen[key] = value
    return sorted(seen.values(), key=str.lower)


def canonical_key(value: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", normalize_name(value).lower())).strip()


def heading_title(text: str) -> str:
    stripped = text.strip()
    if not stripped:
        return ""
    if re.fullmatch(r"[-=]{3,}", stripped):
        return ""
    markdown = re.match(r"^#+\s*(.+?)\s*$", stripped)
    if markdown:
        return normalize_name(markdown.group(1))
    bracketed = re.match(r"^\[\s*(.+?)\s*\]$", stripped)
    if bracketed:
        return normalize_name(bracketed.group(1))
    if re.fullmatch(r"[A-Z0-9][A-Z0-9 /_()&+\-–—]+", stripped) and len(stripped) > 2:
        return normalize_name(stripped)
    return ""


def heading_matches(title: str, headings: list[str]) -> bool:
    title_key = canonical_key(title)
    return any(title_key == canonical_key(heading) for heading in headings)


def session_token(input_path: Path, text: str) -> str:
    filename_match = re.search(r"session[_\-\s]*(\d+)", input_path.stem, re.I)
    if filename_match:
        return f"SESSION_{int(filename_match.group(1)):03d}"

    text_match = re.search(r"\bsession\s*(?:number|#|no\.?)?\s*[:#-]?\s*(\d+)\b", text, re.I)
    if text_match:
        return f"SESSION_{int(text_match.group(1)):03d}"

    safe_stem = re.sub(r"[^A-Za-z0-9]+", "_", input_path.stem).strip("_").upper()
    return safe_stem or "SESSION_UNKNOWN"


def labeled_value(lines: list[Line], labels: list[str]) -> str:
    label_pattern = "|".join(re.escape(label) for label in labels)
    pattern = re.compile(rf"^\s*(?:#+\s*)?(?:{label_pattern})\s*[:\-]\s*(.+?)\s*$", re.I)
    for line in lines:
        match = pattern.match(line.text)
        if match:
            return normalize_name(match.group(1))
    return ""


def section_values(lines: list[Line], headings: list[str], max_items: int | None = None) -> list[str]:
    items: list[str] = []
    in_section = False
    for line in lines:
        title = heading_title(line.text)
        if title and heading_matches(title, headings):
            in_section = True
            continue
        if in_section and title:
            break
        if not in_section:
            continue
        bullet = re.match(r"^\s*(?:[-*]|\d+\.)\s+(.+?)\s*$", line.text)
        if bullet:
            items.append(normalize_name(bullet.group(1)))
            if max_items and len(items) >= max_items:
                break
            continue
        value = normalize_name(line.text)
        if value and not re.fullmatch(r"[-=]{3,}", value):
            items.append(value)
            if max_items and len(items) >= max_items:
                break
    return unique_sorted(items)


def collect_section_items(lines: list[Line], headings: list[str]) -> list[str]:
    items: list[str] = []
    in_section = False
    for line in lines:
        title = heading_title(line.text)
        if title and heading_matches(title, headings):
            in_section = True
            continue
        if in_section and title:
            break
        if in_section:
            bullet = re.match(r"^\s*(?:[-*]|\d+\.)\s+(.+?)\s*$", line.text)
            if bullet:
                items.extend(split_list(bullet.group(1)))
    return unique_sorted(items)


def extract_identity(data: dict[str, Any], input_path: Path, text: str, lines: list[Line]) -> None:
    identity = data["session_identity"]
    token = session_token(input_path, text)
    session_number = re.search(r"(\d+)$", token)
    identity["session_number"] = session_number.group(1) if session_number else ""

    real_world_source = (
        labeled_value(
            lines,
            [
                "real date",
                "real world date",
                "real-world date",
                "real-world session date",
                "session date",
                "date played",
                "played",
            ],
        )
        or " ".join(section_values(lines, ["REAL DATE", "Real Date"], max_items=1))
    )
    # real_world_date is the date the session happened, not the date notes were recorded or revised.
    identity["real_world_date"] = first_date_value(real_world_source)

    in_game_source = (
        labeled_value(lines, ["in game date", "in-game date", "game date", "fiction date"])
        or " ".join(section_values(lines, ["IN-GAME DATES", "IN-GAME DATE", "In-Game Date"], max_items=1))
    )
    identity["in_game_date"] = first_date_value(in_game_source)
    identity["in_game_time_passage"] = labeled_value(
        lines,
        ["run time", "in game time passage", "in-game time passage", "time passage", "elapsed time", "downtime"],
    )
    if not identity["in_game_time_passage"]:
        identity["in_game_time_passage"] = "; ".join(collect_time_advances(lines))
    if not identity["in_game_time_passage"]:
        identity["in_game_time_passage"] = collect_time_jump(text)

    identity["primary_locations"] = split_list(
        labeled_value(lines, ["primary locations", "primary location", "locations", "location"])
    )
    identity["participating_pcs"] = split_list(
        labeled_value(lines, ["participating pcs", "participating PCs", "pcs", "player characters", "players"])
    )

    identity["primary_locations"] = unique_sorted(
        identity["primary_locations"]
        + collect_section_items(lines, ["Primary Locations", "Locations", "Location Flow"])
    )
    identity["participating_pcs"] = unique_sorted(
        identity["participating_pcs"]
        + collect_section_items(lines, ["Participating PCs", "PCs", "Player Characters"])
    )

    text_key = text.lower()
    identity["participating_pcs"] = unique_sorted(
        identity["participating_pcs"]
        + [pc.title() if pc != "the chin" else "The Chin" for pc in KNOWN_PCS if re.search(rf"\b{re.escape(pc)}\b", text_key)]
    )


def collect_time_advances(lines: list[Line]) -> list[str]:
    advances: list[str] = []
    seen: set[str] = set()
    in_time_advance = False
    for line in lines:
        title = heading_title(line.text)
        if title:
            in_time_advance = canonical_key(title) == "time advance"
            continue
        if not in_time_advance:
            continue
        match = re.match(r"^\s*[-*]\s*(\+\s*\d+\s+days?(?:\s*[→\-]+\s*.+?)?)\s*$", line.text, re.I)
        if match:
            value = re.sub(r"\s*[→–—]+\s*", " -> ", normalize_name(match.group(1)))
            key = value.lower()
            if key not in seen:
                seen.add(key)
                advances.append(value)
    return advances


def collect_time_jump(text: str) -> str:
    match = re.search(
        r"\bfrom\s+((?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|"
        r"Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{1,2},?\s+\d{4})"
        r"\s+to\s+((?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|"
        r"Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{1,2},?\s+\d{4})",
        text,
        re.I,
    )
    if match:
        return f"{match.group(1)} to {match.group(2)}"
    match = re.search(
        r"\b((?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|"
        r"Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{1,2},?\s+\d{4})"
        r"\s+to\s+((?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|"
        r"Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{1,2},?\s+\d{4})",
        text,
        re.I,
    )
    if match:
        return f"{match.group(1)} to {match.group(2)}"
    return ""


def first_date_value(value: str) -> str:
    if not value:
        return ""
    for pattern in DATE_PATTERNS:
        match = pattern.search(value)
        if match:
            return match.group(0)
    return value


def infer_entity_type_from_label(line: str) -> tuple[str, str] | None:
    for bucket, labels in ENTITY_TYPES.items():
        for label in labels:
            patterns = [
                rf"^\s*(?:[-*]\s*)?(?:{re.escape(label)})\s*[:\-]\s*(.+)$",
                rf"^\s*(?:[-*]\s*)?(.+?)\s*\((?:{re.escape(label)})\)\s*$",
            ]
            for pattern in patterns:
                match = re.match(pattern, line, re.I)
                if match:
                    name = normalize_name(match.group(1))
                    if name:
                        return bucket, name
    return None


def extract_named_phrases(text: str) -> list[str]:
    candidates: list[str] = []
    phrase_pattern = re.compile(
        r"\b(?:[A-Z][A-Za-z0-9'&.-]+|[A-Z]{2,})(?:\s+(?:of|the|and|&|[A-Z][A-Za-z0-9'&.-]+|[A-Z]{2,})){0,5}\b"
    )
    for match in phrase_pattern.finditer(text):
        candidate = normalize_name(match.group(0))
        if not candidate or len(candidate) < 2:
            continue
        if is_weak_entity_candidate(candidate):
            continue
        if is_malformed_entity_candidate(candidate):
            continue
        if re.fullmatch(r"\d+", candidate):
            continue
        candidates.append(candidate)
    return unique_sorted(candidates)


def is_weak_entity_candidate(candidate: str) -> bool:
    if canonical_key(candidate) in DOCUMENT_STATUS_FALSE_POSITIVES:
        return True
    words = re.findall(r"[A-Za-z]+", candidate.lower())
    if not words:
        return True
    if candidate.lower() in {"gm", "npc", "pc", "pcs", "npcs"}:
        return True
    return all(word in COMMON_ENTITY_FALSE_POSITIVES for word in words)


def is_malformed_entity_candidate(candidate: str) -> bool:
    return candidate.count("(") != candidate.count(")")


def is_table_control_candidate(candidate: str) -> bool:
    key = canonical_key(candidate)
    return key in {
        "advanced",
        "clock",
        "killed",
        "no",
        "none",
        "optional",
        "player facing",
        "retrieval",
        "this",
        "three",
        "track",
        "update",
        "update npc",
    }


def known_bucket(name: str) -> str | None:
    key = canonical_key(name)
    if key in KNOWN_PCS:
        return "pcs"
    if key in KNOWN_FACTIONS:
        return "factions"
    if key in KNOWN_ITEMS_OR_ARTIFACTS:
        return "items_or_artifacts"
    if key in KNOWN_LOCATIONS:
        return "locations"
    return None


def infer_bucket_from_context(name: str, line: str) -> str:
    bucket = known_bucket(name)
    if bucket:
        return bucket
    lower = line.lower()
    for bucket, labels in ENTITY_TYPES.items():
        if any(re.search(rf"\b{re.escape(label)}\b", lower) for label in labels):
            return bucket

    if re.search(r"\b(place|went to|arrived at|left|district|building|bar|club|warehouse|clinic|safehouse)\b", lower):
        return "locations"
    if re.search(r"\b(job|mission|contract|run|pay|Johnson)\b", lower):
        return "jobs"
    if re.search(r"\b(clue|lead|evidence|intel|learned|discovered|revealed)\b", lower):
        return "clues"
    if re.search(r"\b(faction|gang|corp|corporation|organization|syndicate|agency|mafia|triad|triads|police)\b", lower):
        return "factions"
    if re.search(r"\b(item|artifact|weapon|gear|file|datachip|drone|vehicle|crate|truck|pager|tracker|pistol|pistols|uzi|phone)\b", lower):
        return "items_or_artifacts"
    return "npcs"


def add_known_entities_from_text(entity_lines: dict[str, set[str]], text: str) -> None:
    lower = text.lower()
    display_names = {
        "boeing": "Boeing",
        "brigada 12": "Brigada 12",
        "burnouts": "Burnouts",
        "burnouts gang": "Burnouts gang",
        "chinese triads": "Chinese Triads",
        "kestrel": "Kestrel",
        "kestrel defense systems": "Kestrel Defense Systems",
        "kilmer": "Kilmer",
        "lone star": "Lone Star",
        "russian mafia": "Russian Mafia",
        "switch": "Switch",
        "the chin": "The Chin",
        "box truck": "Box truck",
        "burner phone": "Burner phone",
        "crate": "Crate",
        "drone craft": "Drone craft",
        "light pistols": "Light Pistols",
        "modified pager/tracker": "Modified pager/tracker",
        "prototype bug detector": "Prototype Bug Detector",
        "the doughnut": "The Doughnut",
        "uzi": "Uzi",
        "gray line district": "Gray Line District",
        "north side": "North Side",
        "pier 12": "Pier 12",
        "pier 15": "Pier 15",
        "rusty spade": "Rusty Spade",
        "siberian wolf": "Siberian Wolf",
        "south side": "South Side",
    }
    for name in KNOWN_PCS:
        if re.search(rf"\b{re.escape(name)}\b", lower):
            entity_lines["pcs"].add(display_names.get(name, name.title()))
    for name in KNOWN_FACTIONS:
        if re.search(rf"\b{re.escape(name)}\b", lower):
            entity_lines["factions"].add(display_names.get(name, name.title()))
    for name in KNOWN_ITEMS_OR_ARTIFACTS:
        if re.search(rf"\b{re.escape(name)}\b", lower):
            entity_lines["items_or_artifacts"].add(display_names.get(name, name.title()))
    for name in KNOWN_LOCATIONS:
        if re.search(rf"\b{re.escape(name)}\b", lower):
            entity_lines["locations"].add(display_names.get(name, name.title()))


def extract_entities(data: dict[str, Any], lines: list[Line]) -> dict[str, set[str]]:
    entity_lines: dict[str, set[str]] = {bucket: set() for bucket in ENTITY_TYPES}
    full_text = "\n".join(line.text for line in lines)

    for pc in data["session_identity"]["participating_pcs"]:
        entity_lines["pcs"].add(pc)
    for location in data["session_identity"]["primary_locations"]:
        entity_lines["locations"].add(location)
    add_known_entities_from_text(entity_lines, full_text)

    section_bucket = ""
    for line in lines:
        if line.number in data.get("_skip_update_lines", []):
            continue
        title = heading_title(line.text)
        if title:
            section_bucket = ""
            heading_text = title.lower()
            for bucket, labels in ENTITY_TYPES.items():
                if heading_matches(heading_text, labels):
                    section_bucket = bucket
                    break
            continue

        labeled = infer_entity_type_from_label(line.text)
        if labeled:
            bucket, name = labeled
            for item in split_list(name):
                if not is_weak_entity_candidate(item) and not is_malformed_entity_candidate(item):
                    entity_lines[known_bucket(item) or bucket].add(item)
            continue

        bullet = re.match(r"^\s*[-*]\s+(.+?)\s*$", line.text)
        if bullet and section_bucket:
            for item in split_list(bullet.group(1)):
                if not is_weak_entity_candidate(item) and not is_malformed_entity_candidate(item):
                    entity_lines[known_bucket(item) or section_bucket].add(item)
            continue

        if has_update_language(line.text):
            for name in extract_named_phrases(line.text):
                if is_table_control_candidate(name):
                    continue
                bucket = infer_bucket_from_context(name, line.text)
                entity_lines[bucket].add(name)

    for bucket, values in entity_lines.items():
        data["entities"][bucket] = unique_sorted(values)

    return entity_lines


def has_update_language(text: str) -> bool:
    lower = text.lower()
    return any(re.search(rf"\b{re.escape(verb)}\b", lower) for verb in UPDATE_VERBS)


def update_type(text: str) -> str:
    lower = text.lower()
    if re.search(r"\b(killed|destroyed|defeated|completed|finished|delivered|paid)\b", lower):
        return "resolution"
    if re.search(r"\b(discovered|learned|revealed|uncovered|found|identified|confirmed)\b", lower):
        return "discovery"
    if re.search(r"\b(accepted|hired|agreed|promised|refused|declined|decided)\b", lower):
        return "decision"
    if re.search(r"\b(moved|left|escaped|captured|arrested|injured|damaged|lost|gained|acquired|received)\b", lower):
        return "state_change"
    return "event"


def confidence_for(text: str, entity_name: str) -> str:
    lower = text.lower()
    if any(marker in lower for marker in UNCERTAINTY_MARKERS):
        return "low"
    if re.search(rf"\b{re.escape(entity_name.lower())}\b", lower) and has_update_language(text):
        return "high"
    return "medium"


def fragile_category_for(text: str) -> str:
    lower = text.lower()
    if re.search(r"\b\d+\b", text):
        return "Exact Numbers"
    if re.search(r"\b(?:phone|pager|contact|number|address|line)\b", lower):
        return "Contact Information"
    if re.search(r"\b(?:unknown|unclear|tbd|not sure|maybe|possibly|probably)\b", lower):
        return "Deferred Content"
    return "Recall Triggers"


def section_update_area(update_type_value: str) -> str:
    if update_type_value in {"payment", "karma"}:
        return "Session reward/payment review"
    if update_type_value in {"directive", "monitoring", "status"}:
        return "Clue/job/thread review"
    if update_type_value == "team_decision":
        return "Session decision review"
    return "Session review"


def add_structured_session_update(
    data: dict[str, Any],
    seen: set[tuple[str, str, str]],
    *,
    entity_name: str,
    entity_type: str,
    update_type_value: str,
    update_text: str,
    source_excerpt: str,
    confidence: str = "high",
) -> None:
    cleaned_text = normalize_name(update_text)
    key = (entity_name.lower(), update_type_value, cleaned_text.lower())
    if key in seen:
        return
    seen.add(key)
    data["structured_session_updates"].append(
        {
            "entity_name": entity_name,
            "entity_type": entity_type,
            "update_type": update_type_value,
            "update_text": cleaned_text,
            "source_excerpt": source_excerpt,
            "confidence": confidence,
            "recommended_repository_area": section_update_area(update_type_value),
            "requires_user_review": True,
        }
    )


def add_section_based_updates(data: dict[str, Any], lines: list[Line]) -> None:
    seen: set[tuple[str, str, str]] = set()
    current_heading = ""
    pending_payment = False
    major_context = ""

    for line in lines:
        title = heading_title(line.text)
        if title:
            current_heading = canonical_key(title)
            if "ivan" in current_heading and "russian mafia" in current_heading:
                major_context = "ivan_contact"
            elif current_heading == "team activity days 1 3":
                major_context = "team_activity"
            elif current_heading == "current state":
                major_context = "current_state"
            elif current_heading in {
                "campaign log session 2 final revised",
                "session start may 24 2057",
                "post run may 24 2057",
                "post session development",
            }:
                major_context = current_heading
            pending_payment = False
            continue

        text = normalize_name(line.text)
        if not text:
            continue
        bullet = re.match(r"^\s*(?:[-*]|[→•])\s*(.+?)\s*$", line.text)
        bullet_text = normalize_name(bullet.group(1)) if bullet else text
        lower = bullet_text.lower()
        source_excerpt = f"Line {line.number}: {line.text.strip()}"

        if current_heading == "update" and "payment increased" in lower:
            pending_payment = True
            continue

        if pending_payment and re.search(r"\b\d[\d,]*\s*¥\s+per runner\b", lower):
            add_structured_session_update(
                data,
                seen,
                entity_name="Team",
                entity_type="session_reward",
                update_type_value="payment",
                update_text=f"Payment increased: {bullet_text}",
                source_excerpt=source_excerpt,
            )
            continue

        if current_heading == "team decision" and re.search(r"\b(team declines|declines opening|advocates opening crate)\b", lower):
            add_structured_session_update(
                data,
                seen,
                entity_name="Team",
                entity_type="team",
                update_type_value="team_decision",
                update_text=bullet_text,
                source_excerpt=source_excerpt,
            )
            continue

        if current_heading == "team debrief" and "switch shares lone star background" in lower:
            add_structured_session_update(
                data,
                seen,
                entity_name="Switch",
                entity_type="pc",
                update_type_value="disclosure",
                update_text=bullet_text,
                source_excerpt=source_excerpt,
            )
            continue

        if current_heading == "reward" and re.search(r"\+\s*1\s+karma.*switch", lower):
            add_structured_session_update(
                data,
                seen,
                entity_name="Switch",
                entity_type="pc",
                update_type_value="karma",
                update_text=bullet_text,
                source_excerpt=source_excerpt,
            )
            continue

        if current_heading == "mission reward" and re.search(r"\+\s*4\s+karma.*each runner", lower):
            add_structured_session_update(
                data,
                seen,
                entity_name="Team",
                entity_type="team",
                update_type_value="karma",
                update_text=bullet_text,
                source_excerpt=source_excerpt,
            )
            continue

        if major_context == "ivan_contact" and current_heading == "directive" and re.search(
            r"\b(monitor triad activity|report opportunities|interfere when viable|support russian mafia control)\b",
            lower,
        ):
            add_structured_session_update(
                data,
                seen,
                entity_name="Ivan / Russian Mafia",
                entity_type="faction_contact",
                update_type_value="directive",
                update_text=bullet_text,
                source_excerpt=source_excerpt,
            )
            continue

        if current_heading in {"team", "status"} and re.search(r"\b(monitoring triad|monitoring triads|seeking additional work)\b", lower):
            add_structured_session_update(
                data,
                seen,
                entity_name="Team",
                entity_type="team",
                update_type_value="monitoring",
                update_text=bullet_text,
                source_excerpt=source_excerpt,
            )
            continue

        if current_heading == "blackjack" and re.search(r"\bmissing|non-responsive\b", lower):
            add_structured_session_update(
                data,
                seen,
                entity_name="Blackjack",
                entity_type="npc",
                update_type_value="status",
                update_text=bullet_text,
                source_excerpt=source_excerpt,
            )
            continue

        if current_heading == "team" and major_context == "current_state" and re.search(
            r"\b(active in gray line district|operational posture: alert)\b",
            lower,
        ):
            add_structured_session_update(
                data,
                seen,
                entity_name="Team",
                entity_type="team",
                update_type_value="status",
                update_text=bullet_text,
                source_excerpt=source_excerpt,
            )
            continue


RETROFIT_TABLE_HEADINGS = {
    "npc impacts": "npc_impact",
    "pc impacts": "pc_impact",
    "faction impacts": "faction_impact",
    "location impacts": "location_impact",
    "thread clue job updates": "thread_clue_job_update",
    "loot money gear": "loot_money_gear",
}


RETROFIT_TABLE_COLUMNS = {
    "npc_impact": ["entity_name", "change", "follow_up"],
    "pc_impact": ["entity_name", "change", "mechanical_or_story_impact", "follow_up"],
    "faction_impact": ["entity_name", "change", "pressure_or_clock", "next_likely_action"],
    "location_impact": ["entity_name", "change", "file_update_needed"],
    "thread_clue_job_update": ["entity_name", "status", "evidence", "next_step"],
    "loot_money_gear": ["entity_name", "current_holder", "status", "follow_up"],
}


def split_pipe_row(text: str) -> list[str]:
    return [normalize_name(part) for part in text.strip().strip("|").split("|")]


def is_pipe_table_row(text: str) -> bool:
    stripped = text.strip()
    return "|" in stripped and not re.fullmatch(r"\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)+\|?", stripped)


def add_retrofit_structured_updates(data: dict[str, Any], lines: list[Line]) -> None:
    current_table = ""
    skip_lines: set[int] = set(data.get("_skip_update_lines", []))
    seen: set[tuple[str, str, str]] = set()

    for line in lines:
        title = heading_title(line.text)
        if title:
            current_table = RETROFIT_TABLE_HEADINGS.get(canonical_key(title), "")
            continue

        if not current_table or not is_pipe_table_row(line.text):
            continue

        cells = split_pipe_row(line.text)
        if len(cells) < 2:
            continue
        if cells[0].lower() in {"npc", "pc", "faction", "location", "thread", "item"}:
            skip_lines.add(line.number)
            continue
        if cells[0].lower() in {"downstream file updates"}:
            skip_lines.add(line.number)
            continue

        columns = RETROFIT_TABLE_COLUMNS[current_table]
        record = {
            "source_section": current_table,
            "record_type": current_table,
            "entity_name": cells[0],
            "source_excerpt": f"Line {line.number}: {line.text.strip()}",
            "visibility": "GM_ONLY" if "[gm only]" in line.text.lower() else "STANDARD",
            "requires_user_review": False,
        }
        for index, cell in enumerate(cells[1:], start=1):
            key = columns[index] if index < len(columns) else f"column_{index + 1}"
            record[key] = cell

        dedupe = (
            record["source_section"].lower(),
            record["entity_name"].lower(),
            record.get("change", record.get("status", "")).lower(),
        )
        if dedupe not in seen:
            seen.add(dedupe)
            data["retrofit_structured_updates"].append(record)
        skip_lines.add(line.number)

    data["_skip_update_lines"] = sorted(skip_lines)


def add_updates(data: dict[str, Any], lines: list[Line]) -> None:
    all_entities: list[tuple[str, str]] = []
    for bucket, names in data["entities"].items():
        for name in names:
            all_entities.append((bucket, name))

    seen_updates: set[tuple[str, str, str]] = set()
    skip_lines = set(data.get("_skip_update_lines", []))
    for line in lines:
        if line.number in skip_lines:
            continue
        if not has_update_language(line.text):
            continue
        line_lower = line.text.lower()
        for bucket, name in all_entities:
            if name.lower() not in line_lower:
                continue
            confidence = confidence_for(line.text, name)
            update = {
                "entity_name": name,
                "entity_type": bucket.rstrip("s") if bucket != "items_or_artifacts" else "item_or_artifact",
                "update_type": update_type(line.text),
                "update_text": normalize_name(line.text),
                "source_excerpt": f"Line {line.number}: {line.text.strip()}",
                "confidence": confidence,
                "recommended_repository_area": RECOMMENDED_AREAS[bucket],
                "requires_user_review": True,
            }
            key = (name.lower(), update["update_type"], update["update_text"].lower())
            if key in seen_updates:
                continue
            seen_updates.add(key)
            data["updates"][UPDATE_BUCKETS[bucket]].append(update)


def add_reconciliation_flags(data: dict[str, Any], lines: list[Line]) -> None:
    identity = data["session_identity"]
    for field, value in identity.items():
        if value:
            continue
        data["reconciliation_flags"].append(
            {
                "flag_type": "missing_session_identity",
                "field": field,
                "details": f"{field} was not clearly found in the session log.",
                "requires_user_review": True,
            }
        )

    for line in lines:
        lower = line.text.lower()
        if any(marker in lower for marker in UNCERTAINTY_MARKERS):
            data["preserved_fragile_details"].append(
                {
                    "category": fragile_category_for(line.text),
                    "source_excerpt": f"Line {line.number}: {line.text.strip()}",
                    "preservation_reason": "Uncertain or deferred source text may support later recall, validation, continuity, extraction, or reconstruction.",
                    "suggested_destination": "ADDITIONAL PRESERVED DETAILS or UNCERTAIN / DEFERRED FACTS",
                    "status": "non_blocking_preserved_reference",
                    "requires_user_review": False,
                }
            )
        if re.search(r"\b(?:aka|alias|also known as|spelled|misspelled)\b", lower):
            data["reconciliation_flags"].append(
                {
                    "flag_type": "possible_name_reconciliation",
                    "source_excerpt": f"Line {line.number}: {line.text.strip()}",
                    "details": "The source text may indicate an alias, alternate spelling, or misspelling.",
                    "requires_user_review": True,
                }
            )
        if re.search(r"\b(?:contradicts|retcon|previously|inconsistent|doesn't match|does not match)\b", lower):
            data["reconciliation_flags"].append(
                {
                    "flag_type": "possible_contradiction",
                    "source_excerpt": f"Line {line.number}: {line.text.strip()}",
                    "details": "The source text may conflict with earlier campaign information.",
                    "requires_user_review": True,
                }
            )

    for bucket, names in data["entities"].items():
        if not names:
            continue
        update_bucket = UPDATE_BUCKETS[bucket]
        updated_names = {
            update["entity_name"].lower()
            for update in data["updates"].get(update_bucket, [])
        }
        for name in names:
            if name.lower() not in updated_names:
                data["reconciliation_flags"].append(
                    {
                        "flag_type": "mentioned_without_durable_update",
                        "entity_name": name,
                        "entity_type": bucket,
                        "details": "Entity was mentioned, but no durable change was detected.",
                        "requires_user_review": False,
                    }
                )

    for bucket, names in data["entities"].items():
        for name in names:
            if is_malformed_entity_candidate(name):
                data["reconciliation_flags"].append(
                    {
                        "flag_type": "malformed_entity_name",
                        "entity_name": name,
                        "entity_type": bucket,
                        "details": "Entity candidate has malformed parenthetical text.",
                        "requires_user_review": True,
                    }
                )


def add_downstream_impacts(data: dict[str, Any]) -> None:
    impacts: dict[str, set[str]] = {}
    for updates in data["updates"].values():
        for update in updates:
            area = update["recommended_repository_area"]
            impacts.setdefault(area, set()).add(update["entity_name"])

    for area, entities in sorted(impacts.items()):
        data["downstream_file_impacts"].append(
            {
                "repository_area": area,
                "entities": unique_sorted(entities),
                "recommended_action": "Review staged extraction before updating any canon file.",
                "requires_user_review": True,
            }
        )


def add_user_decisions(data: dict[str, Any]) -> None:
    for flag in data["reconciliation_flags"]:
        if flag.get("requires_user_review"):
            if flag.get("flag_type") in {"mentioned_without_durable_update"}:
                continue
            field = flag.get("field") or flag.get("entity_name") or flag.get("flag_type")
            data["user_decisions_required"].append(
                {
                    "decision": f"Review {field}: {flag.get('details', 'Human review required.')}",
                    "source_excerpt": flag.get("source_excerpt", ""),
                }
            )

    for updates in data["updates"].values():
        for update in updates:
            if update["confidence"] != "high":
                data["user_decisions_required"].append(
                    {
                        "decision": f"Approve or reject {update['confidence']}-confidence update for {update['entity_name']}.",
                        "source_excerpt": update["source_excerpt"],
                    }
                )


def derive_output_dir(input_path: Path, override: str | None) -> Path:
    if override:
        return Path(override)

    session_dir = input_path.parent
    root = session_dir.parent if re.search(r"(?:^|\d+_)?sessions?$", session_dir.name, re.I) else session_dir
    return root / "10_ARCHIVE" / "extractions"


def markdown_list(values: list[Any], empty: str = "_None detected._") -> str:
    if not values:
        return empty
    lines: list[str] = []
    for value in values:
        if isinstance(value, dict):
            label = (
                value.get("entity_name")
                or value.get("repository_area")
                or value.get("flag_type")
                or value.get("decision")
                or value.get("category")
                or value.get("source_excerpt")
                or value.get("status")
            )
            lines.append(f"- **{label}**: {json.dumps(value, ensure_ascii=False)}")
        else:
            lines.append(f"- {value}")
    return "\n".join(lines)


def render_review(data: dict[str, Any], source_path: Path) -> str:
    identity = data["session_identity"]
    entity_sections = []
    for bucket, names in data["entities"].items():
        title = bucket.replace("_", " ").title()
        entity_sections.append(f"### {title}\n{markdown_list(names)}")

    update_sections = []
    for bucket, updates in data["updates"].items():
        title = bucket.replace("_", " ").title()
        update_sections.append(f"### {title}\n{markdown_list(updates)}")

    return "\n\n".join(
        [
            "# Session Extraction Review",
            f"Source: `{source_path}`",
            "## Session Identity",
            markdown_list([f"{key}: {value}" for key, value in identity.items()]),
            "## Extracted Entities",
            "\n\n".join(entity_sections),
            "## Proposed Updates",
            "\n\n".join(update_sections),
            "## Structured Session Updates",
            markdown_list(data["structured_session_updates"]),
            "## Retrofit Structured Updates",
            markdown_list(data["retrofit_structured_updates"]),
            "## Agnostic Structured Updates",
            markdown_list(data["agnostic_structured_updates"]),
            "## Preserved Fragile Details",
            markdown_list(data["preserved_fragile_details"]),
            "## Downstream File Impacts",
            markdown_list(data["downstream_file_impacts"]),
            "## Reconciliation Flags",
            markdown_list(data["reconciliation_flags"]),
            "## User Decisions Required",
            markdown_list(data["user_decisions_required"]),
        ]
    ) + "\n"


def extract(input_path: Path) -> dict[str, Any]:
    text = read_text(input_path)
    lines = [Line(number=index + 1, text=line) for index, line in enumerate(text.splitlines())]
    data = empty_extraction()

    extract_identity(data, input_path, text, lines)
    add_retrofit_structured_updates(data, lines)
    extract_entities(data, lines)
    add_updates(data, lines)
    add_section_based_updates(data, lines)
    add_reconciliation_flags(data, lines)
    add_downstream_impacts(data)
    add_user_decisions(data)
    data.pop("_skip_update_lines", None)

    return data


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create staged JSON and markdown extraction files from one finalized session log."
    )
    parser.add_argument("session_log", help="Path to one finalized .md or .txt session log.")
    parser.add_argument(
        "--output-dir",
        help="Optional extraction output directory. Defaults to <repo root>/10_ARCHIVE/extractions.",
    )
    args = parser.parse_args()

    input_path = Path(args.session_log).expanduser().resolve()
    if not input_path.exists():
        parser.error(f"Session log does not exist: {input_path}")
    if input_path.suffix.lower() not in {".md", ".txt"}:
        parser.error("Session log must be a plain .md or .txt file.")

    output_dir = derive_output_dir(input_path, args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    token = session_token(input_path, read_text(input_path))
    data = extract(input_path)

    json_path = output_dir / f"{token}_extraction.json"
    review_path = output_dir / f"{token}_extraction_review.md"

    json_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    review_path.write_text(render_review(data, input_path), encoding="utf-8")

    print(f"Wrote {json_path}")
    print(f"Wrote {review_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
