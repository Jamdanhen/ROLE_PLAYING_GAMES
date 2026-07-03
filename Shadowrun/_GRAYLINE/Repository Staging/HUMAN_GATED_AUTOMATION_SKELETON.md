# HUMAN_GATED_AUTOMATION_SKELETON.md

## 1. Status

ACTIVE FRAMEWORK

This file defines the compact human-gated automation skeleton for campaign repository rebuild workflows.

## 2. Purpose

Provide a reusable, machine-readable workflow pattern that keeps user decisions explicit before extraction, staged builds, repository updates, derived output generation, cleanup, or deletion.

## 3. Human-Gated Automation Principle

Automation may prepare structured artifacts, but user decisions control approval boundaries.

Codex must not treat recommendations, prior simulations, process-test outputs, or comparison artifacts as user approval.

## 4. Workflow State Machine

Valid flow:

SESSION SOURCE
-> WORKSHEET GENERATED
-> USER RESPONSE BLOCK COMPLETED
-> RESPONSE BLOCK PARSED
-> APPROVAL RESULT GENERATED
-> NEXT AUTHORIZED STAGE RUNS
-> STAGED BUILD OR NO-OP RESULT

Stable workflow states:

- SOURCE_RECEIVED
- SOURCE_CLASSIFIED
- WORKSHEET_REQUIRED
- WAITING_FOR_USER_RESPONSES
- USER_RESPONSES_RECEIVED
- APPROVAL_RESULT_READY
- APPROVED_FOR_EXTRACTION
- EXTRACTION_COMPLETE
- PACKAGE_READY
- VALIDATION_COMPLETE
- DIFF_PLANNING_COMPLETE
- READY_FOR_STAGED_BUILD
- STAGED_BUILD_COMPLETE
- NO_OP_COMPLETE
- STOPPED_BLOCKER

## 5. File Naming Standard

Workflow artifacts should include the session identifier, stage, and status where applicable.

User-decision worksheets must include USER_INPUT_REQUIRED in the filename or title.

Approval results must be separate from worksheets.

## 6. Worksheet Standard

A worksheet must request user input rather than present approval as complete.

It must clearly state that no content is approved until the user fills the response fields.

It must include a USER RESPONSE BLOCK near the top.

## 7. User Response Block Standard

Every user decision must have a blank answer field.

Use:

USER_RESPONSE_BLOCK_START

[Decision ID] USER ANSWER:

USER_RESPONSE_BLOCK_END

Codex must not fill in the user's answers.

## 8. Response Parsing Standard

Codex may parse the completed response block only after the user provides answers.

Missing, invalid, contradictory, or unsafe answers must stop continuation until resolved.

## 9. Approval Result Standard

Approval results may be generated only after valid user responses are received.

Approval results must distinguish approved, deferred, rejected, corrected, GM-only, player-facing-safe, move, and consolidation decisions.

## 10. Continuation Rule

Continuation is allowed only when required responses are valid and no blocker remains.

Next stages must remain within the explicit authorization granted by the user.

## 11. Stop Conditions

Stop for:

- Missing answers.
- Invalid answers.
- Unresolved GM-only or player-facing safety issue.
- Required write approval not granted.
- Deletion or cleanup requirement without separate approval.
- Source conflict.
- Unsafe repository action.
- Missing required framework, source, or control artifact.

## 12. Future Interface Compatibility

Artifacts should remain readable by humans and parseable by future tools or UI forms.

Decision IDs, allowed answers, and response blocks should remain stable.

## 13. Minimal Launcher Format

A workflow launcher should identify:

- Session identifier.
- Source path.
- Stage requested.
- Allowed writes, if any.
- Required framework files.
- Output file path.
- Stop conditions.
- Final status vocabulary.

## 14. No-Rework Rule

After a session is content-approved and built into staging, it should not require another approval pass unless new evidence, contradiction, user revision, invalid artifact, or safety issue appears.

## 15. Final Decision

ACCEPT
