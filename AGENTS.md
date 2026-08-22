# Role-Playing Games Project Guidance

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

This folder organizes role-playing game projects. Individual campaigns and systems retain their own local authority when they have a specific project folder.

## Shadowrun Utilities Saved Project Lane

Codex may expose a saved local project named `Shadowrun Utilities` with this
repository as its root:

`C:\ROLE_PLAYING GAMES`

That saved Codex project is a routing and working lane. It is not a declaration
that `C:\ROLE_PLAYING GAMES` has become a standalone Role Playing Games project,
and it does not make Shadowrun Utilities the owner of every file in this
repository.

Use this lane for Shadowrun / Grayline utility work, indexing support,
tool-local maintenance, and handoff work that must start from the C-drive RPG
repository.

Primary authority boundaries:

- Shadowrun campaign material:
  `C:\ROLE_PLAYING GAMES\Shadowrun`
- Shadowrun / Grayline utility scripts and tool-local guidance:
  `C:\ROLE_PLAYING GAMES\Shadowrun\_GRAYLINE\Tools`
- Campaign archive app, registry, schemas, tests, and runtime tooling:
  `C:\Campaign_Archive_System`

On startup in this saved Codex project:

1. Treat `C:\ROLE_PLAYING GAMES` as the repository root and C-drive authority.
2. Read this file first.
3. For Shadowrun campaign work, also read:
   `C:\ROLE_PLAYING GAMES\Shadowrun\AGENTS.md`
4. For Shadowrun / Grayline utility work, also read:
   `C:\ROLE_PLAYING GAMES\Shadowrun\_GRAYLINE\Tools\AGENTS.md`
5. If the requested work belongs to `C:\Campaign_Archive_System`, stop and say
   that the Campaign Archive System project owns that substance.

OneDrive, OneNote, sync folders, mirrors, and old interface folders are not
authority for this lane unless the user explicitly says otherwise. They may be
display, access, mirror, export, or historical-reference surfaces only.

When the user says `establish waypoint` or `create a waypoint` in this saved
Codex project, perform the Registry waypoint sequence for the active authority
boundary. Commit and push only the scoped, completed files that belong to the
active lane. If the repository contains unrelated uncommitted Shadowrun campaign
work, leave it untouched and report it as intentionally outside the waypoint
scope.

Do not move, rename, delete, merge, clean up, archive, restructure, or restore
files in this repository unless the user explicitly approves that exact file
operation.
