# Shadowrun Grayline Tools Guidance

## Authority Boundary

This folder contains Shadowrun / Grayline utility scripts, tooling helpers,
test harnesses, and tool-local notes.

The active structured authority for registry records, schemas, tools, tests,
app code, and project guidance is:

`C:\Campaign_Archive_System`

The active Grayline campaign organization root is:

`C:\ROLE_PLAYING GAMES\Shadowrun\_GRAYLINE`

Do not create a second durable campaign registry, NPC database, faction
database, relationship database, session database, or canon store in this
`Tools` folder.

## Registry Waypoint Inheritance

Tooling work inherits the current registry waypoint and lifecycle boundaries:

- Registry records, schemas, app code, tests, and validated update paths belong
  under `C:\Campaign_Archive_System`.
- Generated mirrors are derived output only.
- Draft campaign content is not campaign truth.
- Recommendations, extracted data, chat notes, generated reports, and test
  output are not owner approval.
- Promotion into accepted or canonical records requires explicit owner approval
  and the validated registry update path.
- Prior states, evidence, corrections, and supersession history must be
  preserved by the registry workflow when a real promotion occurs.

If a tool needs to write structured registry data, stop unless the active
command explicitly authorizes that write through the Campaign Archive System
validated update path.

## Shadowrun Tooling Boundaries

Tools in this folder may:

- Read approved local source files when the user authorizes the task.
- Produce local utilities, extraction helpers, validators, conversion scripts,
  and test scripts.
- Produce review-only reports when explicitly requested.
- Write tool-local files inside this folder when the user has authorized tool
  creation or maintenance.

Tools in this folder must not:

- Modify source session logs unless explicitly authorized.
- Modify canon, NPC, faction, location, PC, clue, job, thread, handout, map, or
  player-facing campaign content unless explicitly authorized for that exact
  operation.
- Promote extracted or inferred information automatically.
- Create duplicate primary campaign records.
- Treat extraction artifacts as source of truth.
- Treat `_CAMPAIGN_ARCHIVE_MIRROR` or generated table outputs as authority.
- Write outside the approved project boundary for the active command.

## Artifact Placement

Infer artifact placement from artifact type:

- Tools, scripts, tool tests, and tool-local guidance:
  `C:\ROLE_PLAYING GAMES\Shadowrun\_GRAYLINE\Tools`
- Campaign-authored rules and mechanics:
  `C:\ROLE_PLAYING GAMES\Shadowrun\_GRAYLINE\Campaign Design`
- Undeveloped NPCs, factions, locations, hooks, encounters, future ideas, and
  unpromoted campaign drafts:
  `C:\ROLE_PLAYING GAMES\Shadowrun\_GRAYLINE\Session Development Workspace\Unpromoted Campaign Drafts`
- Accepted session sources:
  `C:\ROLE_PLAYING GAMES\Shadowrun\_GRAYLINE\Sessions`
- Session-specific work and GM planning:
  `C:\ROLE_PLAYING GAMES\Shadowrun\_GRAYLINE\Session Development Workspace\Session NNN`
- Readable dossiers and handouts:
  `C:\ROLE_PLAYING GAMES\Shadowrun\_GRAYLINE\Handouts and Dossiers`
- Visual assets:
  `C:\ROLE_PLAYING GAMES\Shadowrun\_GRAYLINE\Maps` or
  `C:\ROLE_PLAYING GAMES\Shadowrun\_GRAYLINE\Character Pictures`

When placement is unclear, inspect the existing `_GRAYLINE` folder structure
and use the closest existing folder. Do not create new top-level folders unless
the user explicitly approves that placement.

## Promotion Routing

Every generated or processed artifact must retain its lifecycle state:

- `DRAFT` remains unpromoted and is not campaign truth.
- `PROPOSED` or `REVIEW` enters owner-review or pending-intake workflow with
  source anchors and provenance.
- `ACCEPTED` requires explicit owner approval and is written once through the
  validated registry path.
- `CANONICAL` requires separate explicit authority or ratification.
- `REJECTED`, `PARKED`, `SUPERSEDED`, and `DISCARDED` remain preserved in the
  appropriate review or audit location and do not appear in normal
  owner-facing views.

Promotion must perform duplicate resolution, provenance validation, visibility
validation, rollback snapshot creation, one source-truth update, generated-view
refresh, and a completion receipt.

Extractors must never promote content automatically, create duplicate primary
records, or treat recommendations, prior chat, drafts, generated reports, or
test results as owner approval.

Unresolved new entities must route to a new-dossier or owner-review workflow
rather than being silently created as primary records.

## Safety Defaults

Prefer read-only inspection and explicit reports until write approval is clear.

Keep commits narrowly scoped. If the working tree contains unrelated user or
project changes, stage only the files required by the active task.
