# Shadowrun Campaign Project Guidance

## Crucible Registry Inheritance

This project is organized by the Crucible Registry.

Before acting, check the applicable project guidance and use the Crucible
Ecosystem Operating Standards as inherited default behavior unless this local
project guidance explicitly overrides or specializes them.

Inherited defaults include:

- work from meaningful decision point to meaningful decision point
- do not create micro-approval loops
- continue through safe implied work inside an approved lane
- stop only at real decision, authority, source-modification, or safety
  boundaries
- provide a concrete next action or real pause boundary in closeouts
- when user approval or direction is needed, provide short, separate,
  copyable `ADD TO CHAT` blocks; each block must contain one action only and
  must include the expected output
- when the user asks for a generated artifact or content output, provide the
  artifact itself in the appropriate readable or copyable format, not an `ADD
  TO CHAT` approval block
- keep project substance inside the owning project
- preserve local project authority and local overrides
- treat the C drive as the default source of truth for durable project files
  until another source of truth is explicitly identified; treat OneDrive,
  sync folders, mirrors, and interface folders as copies only
- when the user says `establish waypoint` or `create a waypoint`, follow the
  Registry Project Waypoint Synchronization Rule, including current Registry
  guidance review, inherited-guidance refresh, local state review, commit, push
  to GitHub when connected, alignment confirmation, and notation of any
  intentionally unfinished work
- protect user files from unapproved move, rename, delete, merge, overwrite,
  cleanup, or restructure operations

Local project guidance controls when it is more specific.

## OpenAI API Opportunity Review

When a requested feature could benefit from the OpenAI API, explain the
practical benefit, estimate its cost against Jamie's monthly API credits,
and flag it before implementation. Do not create work merely to consume credits.

Apply this to concrete requested features and active project needs, not
speculative work or a standing search for ways to spend credits. Check current
benefit eligibility, remaining credits when available, and current official
pricing at the time of the proposal. Do not assume a fixed allowance, continued
eligibility, or that an app subscription includes API usage. If account details
are unavailable, say so and make the estimate conditional rather than inventing
a balance. State usage assumptions and distinguish estimated gross cost from
any verified eligible credit coverage.

This is an opportunity-identification and explanation rule only. It does not
authorize API activation, spending, purchase of credits, credential changes,
data transmission, or API implementation. Obtain explicit approval for the
proposed implementation and cost boundary before proceeding. Preserve local
authority, privacy requirements, and overrides.

## Sparky Delegation - Included-Allocation Helper

For bounded routine work inside an already-approved project lane, consider the
shared Spark helper when delegation is likely to save main-task usage or time
after handoff and review costs. Prefer a direct calculator or script when simpler.
Do not delegate ordinary conversation or create work to consume spare allocation.

Before dispatch, read the current rule and verified worker route at
`C:\CRUCIBLE_REGISTRY\SPARKY_DELEGATION_RULE.MD`.
Explicitly select `gpt-5.3-codex-spark`, confirm included allocation remains,
verify the worker identity and working directory, and do not interrupt a busy job.
If the route, tools, or allocation cannot be verified, report the limitation;
do not silently substitute a model, buy credits, use paid APIs, or redeem resets.

Send a unique job ID, requesting project, minimum inputs, permitted reads/writes,
expected output, validation checks, and stopping condition. Shared jobs default
to supplied-input, read-only assistance. File-changing work needs an explicitly
authorized project-scoped assignment and suitable execution context.
Delegation does not expand permissions or authorize onward delegation.

Keep project substance, decisions, terminology, and local overrides with the
owning project. Do not import another job's history as authority or turn Registry
hosting into permission to read or modify other projects. The requester must
retrieve, match, and validate the result. Completion without a visible result
is not success; follow the rule's bounded retrieval fallback, never blind retries.

## Dictation And Established Terminology Safeguard

Before interpreting unfamiliar wording as a new term, compare it with:

- established project vocabulary
- current project doctrine
- immediate conversational context
- likely voice-dictation or transcription substitutions

When the intended established term is clear from context, use the established
term, continue without unnecessary confirmation, and do not repeat or formalize
the transcription error.

When the wording could genuinely indicate either a new term or an established
term, pause before analyzing or documenting it and ask exactly: `Is this a new
term?` Identify the likely established term when useful.

When the user clearly introduces a new term intentionally, treat it as a
candidate unless the user explicitly adopts or locks it. Do not canonize a term
merely because it appeared in discussion.

Never create analysis, rules, categories, doctrine, project files, Registry
entries, or waypoint content around a probable transcription artifact.

Preserve this project's established terminology, local guidance, substantive
content, and local overrides.

## Project Boundary

This project owns Shadowrun campaign material and campaign-specific extraction outputs. The broader Data Extraction Project may generalize methods later, but it does not own Shadowrun campaign substance.


## Phone Image Display

Adopted by Jamie on 2026-09-22. For an image requested on a phone, including
the in-chat phone preview, follow:
C:\CRUCIBLE_REGISTRY\PHONE_IMAGE_DISPLAY_PROTOCOL.MD

Complete necessary prose and authorized file work first. Reuse the requested
local image; generate or edit only when actually requested. Call native
tools.view_image with its actual absolute path, then emit the returned image
with image(preview.image_url). Leave that native preview as the final output,
ending with an empty final response where supported. Do not append a Markdown
image embed, filesystem link, caption, success announcement, continuation block,
or further tool work after the preview. Tool success alone is not proof that
the phone displayed the image. Respect higher-level tool requirements.

This is display guidance only. Preserve the project's style, canon, character
and scale rules, creative workflow, privacy, participant access, and local
authority. In Comics it does not authorize ANY drawing-style, color, realism,
character, canon, reference, or creative-workflow change. It grants no new
permission for file moves, publication, mirrors, sandbox resets, or permission
changes. Ordinary non-image output rules remain unchanged.
