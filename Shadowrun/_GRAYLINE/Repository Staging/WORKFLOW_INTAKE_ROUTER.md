# WORKFLOW_INTAKE_ROUTER.md

## 1. Router Status

ACTIVE ROUTER

This router governs Codex-side intake of workflow artifacts during rebuild staging.

## 2. Purpose

When a workflow artifact is provided, Codex must identify the artifact type, detect the workflow state, determine the next authorized action, and execute the next safe action automatically.

Codex must not ask "What do you want me to do with this?" when the artifact clearly implies the next workflow action.

## 3. Artifact Intake Rule

When the user uploads or references a workflow artifact, Codex must apply this router first before asking follow-up questions.

Codex may ask for user input only when the router detects missing answers, invalid answers, ambiguous artifact type, an approval boundary, a safety blocker, or a prohibited repository action.

## 4. Artifact Types And Routes

### USER_INPUT_REQUIRED_WORKSHEET_BLANK

Detected when a worksheet exists but required answer fields are blank.

State:
WAITING_FOR_USER_RESPONSES

Action:
Stop and tell the user to complete the worksheet.

### USER_INPUT_REQUIRED_WORKSHEET_COMPLETED

Detected when the Quick Answer Table or machine-readable response block contains valid answers.

State:
USER_RESPONSES_RECEIVED

Action:
Parse responses, validate answers, and create the approval result if valid.

### APPROVAL_RESULT

Detected when a completed approval result artifact exists.

State:
APPROVAL_RESULT_READY

Action:
Route to the next authorized state if safe and explicitly permitted by the approval result.

### EXTRACTION_OUTPUT

Detected when a valid extraction artifact is provided.

State:
EXTRACTION_COMPLETE

Action:
Route to proposed package generation if safe.

### PROPOSED_PACKAGE

Detected when a proposed repository change package is provided.

State:
PACKAGE_READY

Action:
Route to local validation if safe.

### VALIDATION_REPORT

Detected when a local validation report is provided.

State:
VALIDATION_COMPLETE

Action:
Route to diff planning if safe.

### DIFF_PLANNING_REPORT

Detected when a diff-planning report is provided.

State:
DIFF_PLANNING_COMPLETE

Action:
Route to no-op closure if no changes are needed, or stop for explicit write approval if changes are needed.

## 5. Worksheet Parsing Rule

For worksheets, Codex must inspect the Quick Answer Table first.

If the Quick Answer Table is completed clearly, Codex may parse answers from the table.

If the table is incomplete but the machine-readable response block is completed clearly, Codex may parse answers from the block.

Codex must not treat recommended answers as user answers.

Codex must not infer approval from blank answer fields.

## 6. Validation Rule

Valid answers are:

- APPROVE
- CORRECT
- REJECT
- DEFER
- GM-ONLY
- PLAYER-FACING SAFE
- MOVE
- CONSOLIDATE LATER

If an answer is not valid for the decision, Codex must stop and request correction.

If CORRECT, MOVE, DEFER, or CONSOLIDATE LATER requires notes and notes are missing, Codex must stop if the missing detail blocks safe continuation.

## 7. Automatic Action Rule

Codex must execute the next safe action automatically when all required responses are present, valid, and within the current workflow authorization.

Completed worksheets route to response parsing and approval result creation if valid.

Blank worksheets route to user completion and stop.

Approval results route to the next authorized state if safe.

Extraction outputs route to proposed package generation if valid.

Proposed packages route to local validation if safe.

Validation reports route to diff planning if safe.

Diff planning reports route to no-op closure or stop for explicit write approval.

## 8. Stop Conditions

Codex must stop for:

- Missing answers.
- Invalid answers.
- Unresolved GM-only or player-facing safety issue.
- Write approval requirement.
- Cleanup or deletion approval requirement.
- Ambiguous artifact type.
- Prohibited repository action.
- Missing required source or framework file.
- Source conflict.
- Unsafe campaign content action.

## 9. Required Router Response Format

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

## 10. Final Decision

ACCEPT
