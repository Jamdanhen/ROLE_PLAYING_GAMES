# Role-Playing Games Current Waypoint

## September 22, 2026 coordinated RPG / Shadowrun checkpoint

Dispatch: `REGISTRY-2026-09-22-rpg`.

### Authority and synchronization scope

- Parent authority: `C:\ROLE_PLAYING GAMES`.
- Child authority: `C:\ROLE_PLAYING GAMES\Shadowrun`, within the same repository.
- Existing approved remote: `https://github.com/Jamdanhen/ROLE_PLAYING_GAMES.git`.
- Branch: `main`; one coordinated commit/push, no separate child push.
- Pre-checkpoint local HEAD, tracking branch and live remote main matched
  `9ad114989b9ec9dacf319ee21d66be59bfcbc3aa`.
- This is a scoped checkpoint, not a claim that all campaign material is synced.
  Final commit and live remote verification are reported in the task closeout
  and returned to the dispatching Registry task after push.

### Guidance and Registry freshness

Reviewed both Registry entries (`ROLE-PLAYING-GAMES.MD` and
`SHADOWRUN-CAMPAIGN.MD`), `PROJECT_WAYPOINT_SYNCHRONIZATION_RULE.MD`,
`REGISTRY_INHERITANCE_BLOCK.MD`, `USER_OUTPUT_FORMAT_GUIDANCE.MD`, the approved
phone-display protocol, and root, Shadowrun and Grayline local guidance.

Registry HEAD, tracking branch and live remote main matched
`13cc1489020659345165aacc0807fb2ded647176` at review. Its pending approved
phone-display/seed rollout and registration records were reviewed as current
local guidance; they do not contradict or block this narrow waypoint. This task
does not edit, stage, commit or push Registry files.

Both local inheritance sections retain the approved defaults and local overrides.
The September 22 phone-display hook is already installed in the root and child
AGENTS files and is included without duplication or substantive rewriting.
Only that approved addition is staged from the child AGENTS file: the separate
pre-existing session-correction-placement change is left in the working tree
for its owning lane, not swept into this commit.

### Completed table-reference work

The September 19 player one-sheet and GM-screen panel are saved locally at:

```text
Shadowrun\_GRAYLINE\Table Aids\output\pdf\Grayline_Player_One_Sheet_20260919.pdf
Shadowrun\_GRAYLINE\Table Aids\output\pdf\Grayline_GM_Screen_Panel_20260919.pdf
```

Both were rendered and visually checked when created, and validated as one-page
portrait US Letter documents. Portrait is the user's default unless landscape
is explicitly requested. They record the agreed skill-only, normally TN 5 rules;
Attribute + Skill / Willpower-soak experiments are not adopted.

The complete generation source is included at its existing location:
`Shadowrun\_GRAYLINE\Table Aids\tmp\pdfs\build_table_references.py`.
Despite the directory name, retain this tracked source for reproduction. It uses
Python, ReportLab and pypdf; ordinary execution creates the two PDFs when absent
and refuses to replace existing PDFs unless `--replace-generated` is supplied.
No PDFs were regenerated during this waypoint.

The existing `.gitignore` excludes all PDFs, ZIPs and System_Reference libraries.
It is unchanged; the two generated PDFs remain local-only, with the reviewed
generator providing reproducible repository content. No sourcebooks, reference
archives, preview images, campaign secrets or unrelated material are staged.

Local output SHA-256 at waypoint review:

- Player: `BC0C85018A8A535263A32B07E0FF96065AFA9311E76D608CEB7AA4C8197275A3`
- GM: `2297BEC8F90A2BF9A727D1FB6897599B72DA2C8AEBB33CDCAE3B2C14950F6C38`

### Intentionally unfinished / excluded

Initial full status contained 523 entries: 423 tracked deletions, 7 modified
tracked files and 93 untracked files, with an empty index. Mixed campaign
reorganization, character sheets, master notes, sessions, correction addenda,
maps, recovered OneDrive intake, legacy removals and unpromoted drafts remain
outside this waypoint. Existing changes are neither approved nor reverted here.
Generated preview PNGs remain local and uncommitted.

Visible task review found no competing active writer rooted in this repository.
The active Grayline V3 application task has its own authority and read-only
access to this legacy campaign area; it is not part of this commit/push.
The earlier Campaign Archive System routing discrepancy remains unresolved;
this checkpoint does not change project routing or external project authority.

Resume table play from the two local portrait PDFs. Other campaign changes
require their owning lane's scoped completion review before synchronization.

## September 17, 2026 scoped checkpoint

Authority remains `C:\ROLE_PLAYING GAMES`; the approved ROLE_PLAYING_GAMES
GitHub remote and main branch are unchanged. Registry entry, inherited guidance,
output format, waypoint rule and root AGENTS were checked. Current inheritance
and local overrides are preserved. Live remote main matched local main.

The user explicitly excluded busy Grayline work. This checkpoint therefore
includes this root waypoint record only. The mixed Shadowrun worktree contains
482 status entries at review, including modifications, deletions, recovered
intake and reorganization. None is staged, restored, removed or approved here.
No Grayline repository, worker, campaign file or utility is modified or pushed.

The saved ROLE_PLAYING GAMES app route points to the Shadowrun child folder
within this repository, not OneDrive. Root AGENTS still describes the old
Campaign Archive System route; that historical routing discrepancy is flagged
for an owning-project decision, not changed while Grayline is active.

Prior Asset Operations checkpoint below remains the last reviewed substantive
snapshot. This new record does not mean the mixed campaign work is synchronized.
Final push verification is recorded in the Registry sweep report.

## Historical substantive checkpoint

Date: 2026-08-22

## Active Authority

The durable local authority remains:

```text
C:\ROLE_PLAYING GAMES
```

The approved GitHub remote remains:

```text
https://github.com/Jamdanhen/ROLE_PLAYING_GAMES.git
```

Role Playing Games remains the umbrella repository. The work completed in this
waypoint belongs to the Shadowrun campaign child area.

## Guidance and Registry Freshness

Waypoint creation checked:

```text
C:\CRUCIBLE_REGISTRY\AGENTS.MD
C:\CRUCIBLE_REGISTRY\REGISTRY_INHERITANCE_BLOCK.MD
C:\CRUCIBLE_REGISTRY\USER_OUTPUT_FORMAT_GUIDANCE.MD
C:\CRUCIBLE_REGISTRY\PROJECT_WAYPOINT_SYNCHRONIZATION_RULE.MD
C:\CRUCIBLE_REGISTRY\entries\ROLE-PLAYING-GAMES.MD
C:\ROLE_PLAYING GAMES\AGENTS.md
C:\ROLE_PLAYING GAMES\Shadowrun\AGENTS.md
```

The Registry repository and `origin/main` are aligned at commit `28d6c91`.
The Role-Playing Games inheritance block matches the current approved Registry
block; no root guidance refresh was required.

## Completed Work in This Waypoint

This waypoint records the completed Shadowrun Asset Operations sheet work:

- `Shadowrun_3E_Modular_Character_Sheet_With_Assets_PDF_Export_20260731.html`
  is the current modular character-and-assets sheet with browser-local saving,
  JSON import/export, and printable PDF export.
- `Shadowrun_3E_The_Chin_Siberian_Wolf_Six_Month_Simulation_20260814.html`
  is a separate prefilled replay edition. It preserves the blank master and
  contains only The Chin and Siberian Wolf information needed to reproduce the
  six-month Asset Operations playtest at the table.
- The replay edition records the relevant skills, asset ratings, Condition,
  weekly availability, dice pools, Target Numbers, requirements, pressures,
  historical rolls, support spending, outcomes, and instructions for clearing
  the recorded results and rerunning the test.
- The replay edition uses its own browser-storage key, so it does not overwrite
  or interfere with the blank application.

## Verification

- JavaScript syntax validation passed for the replay edition.
- Browser verification confirmed The Chin, both Rating 3 operational skills,
  the Siberian Wolf, Asset Pool 3, Requirement 10, six monthly trackers, Month
  1's 180 total hours and 15 historical successes, and Month 6's recorded TN
  and ending state.
- The browser reported no page errors during the verification pass.

## Git Scope

Branch:

```text
main
```

Tracking:

```text
origin/main
```

The waypoint commit is intentionally limited to:

```text
CURRENT_WAYPOINT.md
Shadowrun\Character_Sheets\Desktop_Character_Sheets\Sheets\Shadowrun_3E_Modular_Character_Sheet_With_Assets_PDF_Export_20260731.html
Shadowrun\Character_Sheets\Desktop_Character_Sheets\Sheets\Shadowrun_3E_The_Chin_Siberian_Wolf_Six_Month_Simulation_20260814.html
```

## Intentionally Unfinished or Outside Scope

The working tree also contains a large, mixed Shadowrun change set that was not
reviewed as one completed operation. It includes tracked deletions, reorganized
character files, modified master notes and session drafts, correction addenda,
campaign-reference material, maps, unpromoted drafts, legacy repository and
archive-mirror removals, and a recovered OneDrive intake folder.

Those changes remain uncommitted and unsynchronized. This waypoint does not
approve, reverse, clean up, or otherwise decide them. OneDrive recovery material
remains intake/reference material rather than project authority.

## Resume Point

Resume Asset Operations play from the PDF-export modular sheet or the prefilled
Chin/Siberian Wolf replay sheet. Resolve the remaining Shadowrun working-tree
changes only through their owning campaign or file-organization lane.
