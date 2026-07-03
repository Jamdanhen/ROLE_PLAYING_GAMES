# Codex Extraction Specification 001

Artifact Type:
PROJECT ARCHITECT / AUTOMATION SPECIFICATION

Purpose:
Define the repeatable Codex procedure for converting an accepted session log into campaign repository updates without manual duplicate summaries, promotion packets, review chains, or user copy/paste maintenance.

Status:
ACTIVE SPECIFICATION

Control Sources:
- Project_Architect_Checkpoint_001.md
- Project_Outline_Current_State_001.md
- Simplified_Workflow_Test_SESSION_000.md
- PRIMARY PROJECT RULE — CONTROL ARTIFACT ROLE LOCK

Core Directive:
Reduce user clerical burden.

Codex must extract, reconcile, and update repository files from accepted source material. Codex must not create unnecessary intermediate artifacts.

## 1. Accepted Session Log Input Standard

A session log is eligible for Codex extraction only if it has one of the following statuses:

- ACCEPT
- Canon-stable
- Approved for promotion
- Directly authorized by user for extraction

A valid accepted session log should include enough of the following to support extraction:

- Session number
- Session title
- Real-world session date, if available
- In-game date
- Primary location
- Participating PCs
- Major NPCs
- Active factions
- Important locations
- Events
- Consequences
- Threads / clues / jobs
- GM-only material
- Player-facing facts
- Downstream file update notes, if available

Codex must treat the accepted session log as the extraction input.

Codex must not restart review unless a critical blocker prevents extraction.

## 2. Repository Target Map

Codex should update the campaign repository using the established structure:

CAMPAIGN_REPOSITORY/
  00_INDEX/
  01_CANON/
  02_SESSIONS/
  03_NPCS/
  04_FACTIONS/
  05_LOCATIONS/
  06_PCS/
  07_CLUES_JOBS_THREADS/
  08_TABLE_READY/
  09_PLAYER_FACING/
  10_ARCHIVE/

Repository targets:

01_CANON:
- Store durable canon facts confirmed by accepted session logs.
- Preserve session-level consequences.
- Do not include unresolved speculation as canon unless clearly marked.

02_SESSIONS:
- Store the accepted full session log.
- Maintain session identity and chronology.

03_NPCS:
- Update NPC files with confirmed appearances, actions, status changes, relationships, and follow-up needs.
- Do not create NPC files for PCs.

04_FACTIONS:
- Update faction files with clock movement, exposure, actions, losses, pressure changes, and current posture.

05_LOCATIONS:
- Update location files with damage, ownership, status, hidden elements, reputation changes, and event history.

06_PCS:
- Update PC files with confirmed actions, story consequences, relationship changes, heat, obligations, and status changes.

07_CLUES_JOBS_THREADS:
- Update threads, clues, jobs, mysteries, hidden arcs, callbacks, and unresolved hooks.
- Preserve dormant, active, resolved, and GM-only statuses.

08_TABLE_READY:
- Create or update compact table-ready references only when operationally useful.
- Avoid decorative formatting or excessive spacing.
- Do not expand into unnecessary prep.

09_PLAYER_FACING:
- Maintain derived player-facing views only.
- Do not manually create separate summary documents unless explicitly requested as a handout.
- Filter GM-only content.

10_ARCHIVE:
- Move superseded drafts, obsolete versions, or pre-promotion materials out of active repository space.
- Do not delete unless explicitly instructed.

## 3. Extraction Rules

Codex must extract only confirmed information from the accepted session log.

For each extracted item, Codex should determine:

- Entity type
- Repository target
- Existing file match
- New fact
- Changed fact
- Conflict
- GM-only status
- Player-facing eligibility
- Follow-up requirement

Entity types include:

- Session
- PC
- NPC
- Faction
- Location
- Thread
- Clue
- Job
- Item
- Vehicle
- Organization
- Contact
- Event
- Consequence
- Clock
- Heat source
- Table-ready reference
- Player-facing derived fact

Codex should preserve exact names, spellings, dates, and status locks.

Codex must not normalize away fragile details.

Codex must not convert uncertain details into confirmed canon.

Codex must not treat GM-only facts as player-facing.

## 4. Update-Versus-Duplicate Rule

Codex must update existing repository files when a matching file already exists.

Codex must not create duplicate files for the same entity unless the user explicitly requests a split.

Before creating a new file, Codex should check for:

- Exact name match
- Known alias
- Prior spelling variant
- Existing folder entry
- Cross-reference in index
- Existing related file

If an existing file is found:
- Update that file.
- Add the new session-derived facts.
- Preserve previous durable facts unless directly contradicted.
- Mark conflicts instead of overwriting unclear material.

If no existing file is found:
- Create a new file only in the correct repository folder.
- Use the established naming convention if available.
- Keep the file compact and extraction-based.

Duplicate-prevention rule:
If the same fact appears in multiple places, Codex should store it once in the proper source file and allow other outputs to reference or derive from it.

## 5. GM-Only Protection Rules

GM-only material must remain protected.

Any content marked with any of the following must be treated as restricted:

- [GM ONLY]
- GM-only
- hidden
- secret
- not player-facing
- not known to runners
- unknown to PCs
- unrevealed
- dormant hidden arc

GM-only material may be stored in internal repository files where appropriate.

GM-only material must not be included in player-facing derived output unless explicitly revealed in play or explicitly authorized by the user.

When updating player-facing material, Codex must filter out:

- hidden identities
- hidden locations
- hidden object contents
- hidden motives
- hidden faction actions
- hidden callbacks
- hidden AI/emergence material
- unrevealed consequences
- unrevealed source of threats
- any fact explicitly marked [GM ONLY]

GM-only facts should retain their restriction label in internal files.

## 6. Player-Facing Derived Output Rule

Player-facing material is a derived output, not a separate hand-authored summary document by default.

Codex should generate player-facing views from accepted source material by:

- Including only facts known to the players or PCs.
- Excluding GM-only content.
- Excluding unrevealed causes, identities, and hidden mechanics.
- Keeping wording concise and table-usable.
- Avoiding duplicate manually maintained summaries.

Player-facing output may exist as:
- generated view
- derived extract
- temporary table handout
- player-facing repository section

Player-facing output must not become a second source of truth.

If player-facing material is created for table use, it must remain downstream of the source-controlled repository material.

## 7. Conflict Reporting Rules

Codex must report conflicts only when they affect extraction, canon integrity, or repository correctness.

Decision-relevant conflicts include:

- PC accidentally classified as NPC
- faction spelling mismatch
- date contradiction
- session chronology contradiction
- GM-only content appearing in player-facing output
- same entity split across duplicate files
- unresolved canon contradiction
- missing source file required for update
- repository structure mismatch
- unclear whether fact is confirmed or speculative

Codex must not create a worksheet for minor issues.

Minor issues should be recorded as cautions and extraction should proceed when safe.

Conflict report format:

CONFLICT:
- Issue:
- Affected file/entity:
- Source text:
- Existing repository text:
- Recommended action:
- Blocking status: BLOCKER / NON-BLOCKING

Only BLOCKER conflicts should stop extraction.

## 8. Change Report Format

After extraction, Codex should produce one compact change report.

The change report should not become a review artifact.

Required format:

Extraction Change Report

Source:
- [session log name]

Result:
- COMPLETE / PARTIAL / STOPPED

Files Updated:
- [path/file]
- [path/file]

Files Created:
- [path/file]
- [path/file]

Files Archived:
- [path/file]
- [path/file]

Conflicts:
- None
or
- [compact conflict list]

GM-Only Protections Applied:
- [brief list]

Player-Facing Derived Output:
- None
or
- [derived view / generated output path]

Next Required User Action:
- None
or
- [specific blocker only]

The change report must remain compact.

Do not create a second review step from the change report.

## 9. Stop Conditions

Codex must stop extraction only for critical blockers.

Critical blockers include:

- Source file is unreadable.
- Repository target structure is unavailable.
- Existing file conflict would overwrite canon without user decision.
- GM-only material cannot be safely separated from player-facing output.
- Entity identity cannot be resolved and would create duplicate or incorrect records.
- User explicitly says stop.
- Extraction would require manual copy/paste across multiple artifacts by the user.

Non-blockers include:

- Minor wording issues.
- Formatting cleanup.
- Optional table-ready references.
- Missing decorative structure.
- Minor uncertainty that can be labeled.
- Downstream update that can be deferred without damaging canon.

If extraction stops, Codex must report:

STOP

Reason:
- [specific blocker]

Required user decision:
- [single narrow question or action]

Do not produce a worksheet unless the blocker cannot be resolved with one direct question.

## 10. Codex Execution Checklist

Before extraction:
- Confirm the source session log is accepted or authorized.
- Identify session number and title.
- Identify repository root.
- Identify existing entity files.
- Identify GM-only markings.
- Identify player-facing eligibility.
- Identify downstream targets.

During extraction:
- Update existing files before creating new ones.
- Preserve exact names, spellings, dates, and canon locks.
- Protect GM-only material.
- Maintain PC/NPC separation.
- Update threads and clocks.
- Avoid duplicate summaries.
- Avoid artifact chains.
- Record conflicts only when decision-relevant.

After extraction:
- Produce one compact change report.
- Do not create another review artifact.
- Do not create a worksheet unless there is a critical blocker.
- Do not ask the user to manually cut and paste between artifacts.
- End with COMPLETE, PARTIAL, or STOPPED.

## 11. Session 0 Pilot Extraction Notes

Session 0 is the first validated extraction pilot.

Accepted source:
Master_Session log 0.docx

Validation artifact:
Simplified_Workflow_Test_SESSION_000.md

Status:
ACCEPT

Session 0 locked details:
- The Chin is a PC.
- The Chin must never be treated as an NPC.
- Correct faction spelling is Brigada 12.
- Session 0 occurs on March 18, 2057.
- Session 1 begins on May 24, 2057.
- The time jump explains cleanup, body disposal, repairs, and Grayline damage control.
- Spectre enters around 4:00 PM.
- At this stage, runners do not know Spectre’s identity.
- At this stage, runners do not know the hard drive exists.
- At this stage, runners do not know the Kestrel connection.
- Hard drive material is GM-only.
- Trace callback material is GM-only.
- AI emergence material is GM-only.

Session 0 expected extraction targets:

01_CANON:
- Revised Session 0 canon entry.

02_SESSIONS:
- Accepted Session 0 log.

03_NPCS:
- Hubcap.
- Spectre.
- Kestrel Captain.
- Kestrel Enforcers.

04_FACTIONS:
- Brigada 12.
- Kestrel Defense Systems.
- Grayline local network.

05_LOCATIONS:
- Siberian Wolf.
- Wolf restroom.
- Grayline Docks.

06_PCS:
- The Chin.
- Switch.
- Kilmer.

07_CLUES_JOBS_THREADS:
- Spectre thread.
- GM-only hidden hard drive thread.
- GM-only trace callback thread.
- Kestrel investigation thread.
- GM-only AI emergence path.
- Wolf reputation thread.
- Time jump / cleanup / repair / Grayline damage control note.

08_TABLE_READY:
- Optional Kestrel tactical team deceased/reference block.

09_PLAYER_FACING:
- Derived redacted view only.
- No manually created separate summary document.

10_ARCHIVE:
- Older Session 0 drafts after promotion.

## 12. Anti-Spiral Requirement

Codex extraction must not become another workflow chain.

After extraction, the result must be one of:

COMPLETE:
Extraction succeeded.

PARTIAL:
Extraction succeeded except for listed non-blocking deferred items.

STOPPED:
Extraction halted due to a critical blocker.

Codex must not automatically generate:
- another review
- another worksheet
- another checkpoint
- another outline
- another promotion packet
- another summary document
- another clarification artifact

## 13. Primary Operating Rule

The purpose of this specification is to make repository maintenance easier.

If the process increases user clerical burden, duplicate maintenance, or manual copy/paste, the process is failing.

When in doubt:
- update existing repository files
- preserve fragile details
- protect GM-only material
- derive player-facing output
- produce one compact change report
- stop artifact sprawl