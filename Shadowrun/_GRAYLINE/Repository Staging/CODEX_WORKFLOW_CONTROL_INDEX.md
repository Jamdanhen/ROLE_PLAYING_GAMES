# CODEX_WORKFLOW_CONTROL_INDEX.md

## 1. Control Index Status

This is the active Codex-side workflow control index for rebuild staging.

## 2. Active Framework Files

Codex must load and apply:

- `HUMAN_GATED_AUTOMATION_SKELETON.md`
- `USER_INPUT_REQUIRED_WORKSHEET_TEMPLATE.md`
- `WORKFLOW_INTAKE_ROUTER.md`

## 3. Artifact Intake Rule

When the user uploads or references a workflow artifact, Codex must apply `WORKFLOW_INTAKE_ROUTER.md` first.

## 4. User Burden Rule

The user provides source material, completed worksheets, corrections, approvals, and blocker resolutions.

The user should not provide internal execution commands.

## 5. Session 000 Rule

If the user provides a completed Session 000 worksheet, Codex must detect whether the Quick Answer Table has answers.

- If blank, stop and ask the user to complete it.
- If completed, parse answers and create:
  `C:\CAMPAIGN_REPOSITORY_REBUILD_STAGING\10_ARCHIVE\workflow_runs\SESSION_000\SESSION_000_APPROVAL_RESULT.md`

## 6. Required Router Response Format

ROUTER DETECTED INPUT:
[input type]

DETECTED STATE:
[state]

AUTOMATIC ACTION TAKEN:
[action]

OUTPUT CREATED:
[path or NONE]

NEXT STATE:
[state]

USER ACTION REQUIRED:
[action or NONE]

STOPPED:
YES / NO

STOP REASON:
[reason or NONE]

## 7. Repository Protection

The router and control index do not authorize repository write execution by themselves.

Campaign content, canon, session, NPC, faction, location, PC, thread, player-facing, extraction, cleanup, deletion, and staged build actions require the appropriate workflow stage and explicit authorization.

## 8. Final Decision

ACCEPT
