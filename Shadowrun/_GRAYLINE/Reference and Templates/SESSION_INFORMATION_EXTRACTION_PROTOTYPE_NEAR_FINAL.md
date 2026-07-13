# Session Information Extraction Prototype - Near Final Draft

Status:
NEAR FINAL EXTRACTION PROTOTYPE

Purpose:
Preserve the successful Session 009 master-log structure as the preferred working format for extracting session information from raw transcript, dictation, or table-recall material.

This structure is intended to create one rich session artifact that can later feed:

- Canon session records.
- Player-facing recaps.
- NPC, faction, location, thread, and resource extraction.
- Reconciliation review.
- Future table prep.

It is not itself an automated repository update format. It is the preferred pre-extraction master log format.

## Use When

Use this prototype when raw session material contains enough information to produce a detailed session record, especially when the source includes:

- Long table transcripts.
- Dictation with multiple scenes.
- Mixed table talk and in-character events.
- Mechanical/resource changes.
- Contact and thread movement.
- GM-only knowledge mixed with player-facing events.
- Uncertain spellings, dates, identities, or timeline details.

## Core Principles

- Preserve table texture without turning the log into a transcript.
- Organize by scenes first, then extract facts from the scene record.
- Keep uncertainty visible instead of forcing canon.
- Separate player-facing facts from GM-only explanations.
- Record downstream update targets without performing repository updates.
- Preserve fragile details: quotes, numbers, names, signals, timestamps, behavior cues, and unresolved hooks.
- Make one artifact useful for canon review, player recap, extraction, and prep.

## Required Structure

### Title

Use:

```text
# Session [NUMBER] - [Short Descriptive Title]
```

### Status

Use one of:

```text
MASTER SESSION LOG DRAFT / FULL DETAIL / SCENE-BY-SCENE
```

```text
MASTER SESSION LOG / READY FOR RECONCILIATION
```

```text
MASTER SESSION LOG / READY FOR EXTRACTION REVIEW
```

### Source

Identify the source material clearly:

- Transcript file.
- Dictation file.
- Response worksheet.
- Prior review artifact.
- Table memory notes.

### Authority Note

State that the file is a generated session-log artifact and does not update canon/repository files by itself.

## Required Sections

### Session Facts

Include:

- Real-world session date.
- In-game date.
- Session number.
- Primary locations.
- Primary active PCs.
- Major NPCs / contacts involved.

If any field is missing, mark it as unknown or unresolved.

### Summary

Write a strong overview of the session's dramatic and operational movement.

The summary should answer:

- What kind of session was this?
- What pressure clocks or major problems shaped it?
- What changed by the end?
- What must the next workflow care about?

### Opening State

Capture the state at the start of play:

- Active clocks.
- Pending contacts.
- Previous-session fallout.
- PC/NPC physical status.
- Ongoing jobs.
- Known risks.
- Immediate table decisions.

### Scene-By-Scene Sections

The main body should be organized as numbered scenes:

```text
## Scene 1 - [Scene Name]
## Scene 2 - [Scene Name]
## Scene 3 - [Scene Name]
```

Each scene should include:

- What happened.
- Who was involved.
- Important decisions.
- Important quotes or signals.
- Resource/mechanical changes.
- New information learned.
- What remains unresolved.

Scenes should follow play order, not later extraction category order.

### Confirmed / Strongly Supported Facts

List facts that the source supports clearly enough to carry forward.

These should be concise, extraction-friendly bullets.

### Uncertain / Needs Reconciliation

List only unresolved items that matter for canon, extraction, or future prep.

Examples:

- Spelling ambiguity.
- Conflicting date.
- Missing identity.
- Unclear player-facing vs GM-only boundary.
- Unresolved NPC fate.
- Unclear payment or resource amount.
- Transcript phrase that may be misheard.

### GM-Only / Caution Items

Separate facts that should not automatically enter player-facing output.

Use for:

- Behind-the-scenes motives.
- Hidden AI/system logic.
- True faction knowledge not yet revealed.
- NPC inner state.
- Future plot hooks not disclosed.
- Interpretive explanations that players have not confirmed.

### Mechanical / Resource Changes

Track:

- Money.
- Karma.
- Gear.
- Loot.
- Credsticks.
- Contacts gained or activated.
- Injuries or medical status.
- Property upgrades.
- Vehicles.
- Job payments and pending bonuses.

If values are provisional or subject to later database adjustment, say so here.

### NPC / Contact Updates

Use one subsection per NPC/contact.

Each update should answer:

- Who are they?
- What did they do this session?
- What changed?
- What do they know?
- What remains unresolved?

### Thread / Job Updates

Use one subsection per active thread/job.

Each update should answer:

- Status at session start.
- What happened this session.
- Current status.
- Next likely action.
- Whether the thread is open, resolved, deferred, or GM-only.

### Player-Facing Safe Summary

Create a concise version that can be used as the basis for player recap.

Rules:

- Do not reveal GM-only motives or hidden systems.
- Do not resolve uncertain facts.
- Keep it readable and table-useful.
- Include what the characters experienced.

### Final Session Summary

End with a strong prose summary of what the session means structurally.

This is not a player recap. It is the extraction/review-facing final synthesis.

## Optional Sections

Use these only when helpful:

- Downstream File Update List.
- Reconciliation Decisions.
- Player Theories.
- Fragile Detail Preservation.
- Timeline Table.
- Scene Index.
- Open Questions For User.
- Player-Facing Redactions.

## Extraction Notes

After drafting the master log, extraction should be able to pull:

- Session identity.
- Chronology.
- NPC updates.
- Faction updates.
- Location updates.
- PC updates.
- Mechanical/resource changes.
- Job/thread updates.
- Clues.
- Open questions.
- GM-only facts.
- Player-facing recap material.

The master log should not require the user to re-answer already captured details.

## Copy-Ready Skeleton

```markdown
# Session [NUMBER] - [Short Title]

Status:
MASTER SESSION LOG DRAFT / FULL DETAIL / SCENE-BY-SCENE

Source:
[Source file / transcript / dictation / worksheet]

Authority Note:
This file is a generated session-log draft from source material. It does not update canon repository files and does not perform extraction. Any uncertain transcription, date, naming, or player-facing boundary issue is labeled rather than silently resolved.

## Session Facts

Real-world session date:
[Date or unknown]

In-game date:
[Date / window]

Session number:
[Number]

Primary locations:
[Locations]

Primary active PCs:
[PCs]

Major NPCs / contacts involved:
[NPCs / contacts]

## Summary

[High-level session summary.]

## Opening State

[Start-of-session state, active clocks, prior fallout, pending contacts, and immediate pressures.]

## Scene 1 - [Scene Name]

[Scene details.]

## Scene 2 - [Scene Name]

[Scene details.]

## Scene 3 - [Scene Name]

[Continue as needed.]

## Confirmed / Strongly Supported Facts

- [Fact]
- [Fact]
- [Fact]

## Uncertain / Needs Reconciliation

- [Unresolved item]
- [Unresolved item]
- [Unresolved item]

## GM-Only / Caution Items

- [GM-only fact or caution]
- [GM-only fact or caution]
- [GM-only fact or caution]

## Mechanical / Resource Changes

Money:

- [Money change]

Loot / Gear:

- [Gear change]

Karma:

- [Karma change]

Other:

- [Other resource/mechanical change]

## NPC / Contact Updates

### [NPC / Contact Name]

[Update.]

### [NPC / Contact Name]

[Update.]

## Thread / Job Updates

### [Thread / Job Name]

[Update.]

### [Thread / Job Name]

[Update.]

## Player-Facing Safe Summary

[Player-safe recap basis.]

## Final Session Summary

[Extraction/review-facing final synthesis.]
```

## Near-Final Decision

This prototype should be treated as the preferred default format for future full-detail session extraction drafts unless a specific workflow test or user instruction requires a narrower artifact.

