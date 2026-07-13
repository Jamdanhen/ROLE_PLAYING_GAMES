# Role-Playing Games Current Waypoint

Date: 2026-07-13

## Active Authority

The local project authority is:

```text
C:\ROLE_PLAYING GAMES
```

The approved GitHub remote is:

```text
https://github.com/Jamdanhen/ROLE_PLAYING_GAMES.git
```

## Guidance Checked

Waypoint creation checked:

```text
C:\ROLE_PLAYING GAMES\AGENTS.md
C:\CRUCIBLE_REGISTRY\AGENTS.MD
C:\CRUCIBLE_REGISTRY\PROJECT_WAYPOINT_SYNCHRONIZATION_RULE.MD
C:\CRUCIBLE_REGISTRY\entries\ROLE-PLAYING-GAMES.MD
```

The project inherits Crucible Registry operating defaults while preserving
local Role-Playing Games authority and local child-project boundaries.

## Current Folder Role

`C:\ROLE_PLAYING GAMES` is the umbrella workspace for tabletop role-playing
game material.

Current top-level project areas observed:

- `Cypher`
- `Dungeons and Dragons`
- `Other Systems`
- `Shadowrun`

Shadowrun remains a child project area with its own local guidance and campaign
substance. This waypoint does not reorganize or reinterpret Shadowrun content.

## Current Git State

The repository is connected to GitHub, but it is not clean.

Observed state at waypoint creation:

- branch: `main`
- tracking: `origin/main`
- uncommitted deletions exist under `Shadowrun/Character_Sheets`
- untracked project guidance exists at `AGENTS.md` and `Shadowrun/AGENTS.md`
- untracked Shadowrun character-sheet, campaign-design, handout, session, and
  archive-mirror files exist

This waypoint does not commit or push the Role-Playing Games repository because
the dirty worktree contains substantive project files that require a separate
review/commit decision.

## Boundary

This waypoint is a management and Registry handoff point only.

It does not authorize:

- moving files
- deleting files
- restoring deleted files
- renaming files
- cleaning the repository
- committing current RPG worktree changes
- pushing Role-Playing Games changes to GitHub
- changing Shadowrun campaign structure
- splitting Shadowrun into a separate repository

## Registry Push Target

The Registry entry to update is:

```text
C:\CRUCIBLE_REGISTRY\entries\ROLE-PLAYING-GAMES.MD
```

Registry should record:

- `C:\ROLE_PLAYING GAMES` remains the authority location
- the GitHub remote remains `https://github.com/Jamdanhen/ROLE_PLAYING_GAMES`
- the project is active
- the local worktree is dirty and needs a separate review before commit/push
- Shadowrun remains a child project area under this repository unless the owner
  later approves a split

## Next Real Decision

The next decision is whether to review the dirty Role-Playing Games worktree for
a controlled commit/push.

Recommended next lane:

1. classify the current changed/untracked files
2. separate completed project guidance from active Shadowrun working material
3. decide what should be committed, restored, ignored, or deferred
4. only then commit and push `ROLE_PLAYING_GAMES`

