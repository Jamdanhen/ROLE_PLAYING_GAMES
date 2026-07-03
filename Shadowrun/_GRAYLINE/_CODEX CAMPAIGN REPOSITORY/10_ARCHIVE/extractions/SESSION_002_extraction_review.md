# Session Extraction Review

Source: `C:\CAMPAIGN_REPOSITORY\02_SESSIONS\SESSION_002.MD`

## Session Identity

- session_number: 002
- real_world_date: 
- in_game_date: 
- in_game_time_passage: 
- primary_locations: []
- participating_pcs: []

## Extracted Entities

### Pcs
- Crate

### Npcs
- Delivered
- Hired
- Lost
- Mara
- Six
- Tonya (bartender
- UPDATED CANON VERSION

### Factions
_None detected._

### Locations
- Pier 12 (North Side
- Siberian Wolf

### Jobs
- Run

### Clues
_None detected._

### Threads
_None detected._

### Items Or Artifacts
- Crate

## Proposed Updates

### Npc Updates
- **UPDATED CANON VERSION**: {"entity_name": "UPDATED CANON VERSION", "entity_type": "npc", "update_type": "event", "update_text": "UPDATED CANON VERSION", "source_excerpt": "Line 3: UPDATED CANON VERSION", "confidence": "high", "recommended_repository_area": "NPC files", "requires_user_review": true}
- **Lost**: {"entity_name": "Lost", "entity_type": "npc", "update_type": "state_change", "update_text": "→ Lost crate shipment", "source_excerpt": "Line 163: → Lost crate shipment", "confidence": "high", "recommended_repository_area": "NPC files", "requires_user_review": true}
- **Hired**: {"entity_name": "Hired", "entity_type": "npc", "update_type": "decision", "update_text": "→ Hired by Mara", "source_excerpt": "Line 166: → Hired by Mara", "confidence": "high", "recommended_repository_area": "NPC files", "requires_user_review": true}
- **Mara**: {"entity_name": "Mara", "entity_type": "npc", "update_type": "decision", "update_text": "→ Hired by Mara", "source_excerpt": "Line 166: → Hired by Mara", "confidence": "high", "recommended_repository_area": "NPC files", "requires_user_review": true}
- **Delivered**: {"entity_name": "Delivered", "entity_type": "npc", "update_type": "resolution", "update_text": "Delivered via courier drop", "source_excerpt": "Line 256: - Delivered via courier drop", "confidence": "high", "recommended_repository_area": "NPC files", "requires_user_review": true}
- **Six**: {"entity_name": "Six", "entity_type": "npc", "update_type": "event", "update_text": "Six bodies recovered", "source_excerpt": "Line 264: - Six bodies recovered", "confidence": "high", "recommended_repository_area": "NPC files", "requires_user_review": true}

### Faction Updates
_None detected._

### Location Updates
_None detected._

### Pc Updates
- **Crate**: {"entity_name": "Crate", "entity_type": "pc", "update_type": "event", "update_text": "Crate secured in team possession", "source_excerpt": "Line 16: - Crate secured in team possession", "confidence": "high", "recommended_repository_area": "PC files", "requires_user_review": true}
- **Crate**: {"entity_name": "Crate", "entity_type": "pc", "update_type": "state_change", "update_text": "→ Lost crate shipment", "source_excerpt": "Line 163: → Lost crate shipment", "confidence": "high", "recommended_repository_area": "PC files", "requires_user_review": true}
- **Crate**: {"entity_name": "Crate", "entity_type": "pc", "update_type": "state_change", "update_text": "Crate moved to jet ski–sized drone craft", "source_excerpt": "Line 201: - Crate moved to jet ski–sized drone craft", "confidence": "high", "recommended_repository_area": "PC files", "requires_user_review": true}

### Job Updates
- **Run**: {"entity_name": "Run", "entity_type": "job", "update_type": "resolution", "update_text": "Run completed clean (externally", "source_excerpt": "Line 270: - Run completed clean (externally)", "confidence": "high", "recommended_repository_area": "Job files", "requires_user_review": true}

### Clue Updates
_None detected._

### Thread Updates
_None detected._

## Downstream File Impacts

- **Faction files**: {"repository_area": "Faction files", "entities": ["Boeing", "Burnouts gang", "Chinese Triads", "Lone Star", "Russian Mafia"], "recommended_action": "Legacy validation: review faction involvement before canon updates.", "requires_user_review": true}
- **Items or artifacts files**: {"repository_area": "Items or artifacts files", "entities": ["Crate"], "recommended_action": "Legacy validation: review crate possession, condition, and handoff before canon updates.", "requires_user_review": true}
- **Job files**: {"repository_area": "Job files", "entities": ["Run"], "recommended_action": "Review staged extraction before updating any canon file.", "requires_user_review": true}
- **Job files**: {"repository_area": "Job files", "entities": ["Crate recovery / delivery run"], "recommended_action": "Legacy validation: review run resolution, payment, and complications before canon updates.", "requires_user_review": true}
- **Location files**: {"repository_area": "Location files", "entities": ["Gray Line District", "North Side", "Pier 12", "Pier 15", "Rusty Spade", "Siberian Wolf", "South Side"], "recommended_action": "Legacy validation: review location appearances and state before canon updates.", "requires_user_review": true}
- **NPC files**: {"repository_area": "NPC files", "entities": ["Delivered", "Hired", "Lost", "Mara", "Six", "UPDATED CANON VERSION"], "recommended_action": "Review staged extraction before updating any canon file.", "requires_user_review": true}
- **NPC files**: {"repository_area": "NPC files", "entities": ["Blackjack", "Ivan", "Kestrel", "Louie", "Mara", "Skittles", "Snacks", "Toggle", "Tonya"], "recommended_action": "Legacy validation: review NPC state/contact updates before canon updates.", "requires_user_review": true}
- **PC files**: {"repository_area": "PC files", "entities": ["Crate"], "recommended_action": "Review staged extraction before updating any canon file.", "requires_user_review": true}
- **PC files**: {"repository_area": "PC files", "entities": ["Kilmer", "Switch", "The Chin"], "recommended_action": "Legacy validation: review participant/activity details before canon updates.", "requires_user_review": true}
- **Thread files**: {"repository_area": "Thread files", "entities": ["Blackjack missing", "Crate upstream consequences", "Triad pressure on smuggling routes"], "recommended_action": "Legacy validation: review open threads before canon updates.", "requires_user_review": true}

## Reconciliation Flags

- **missing_session_identity**: {"flag_type": "missing_session_identity", "field": "real_world_date", "details": "real_world_date was not clearly found in the session log.", "requires_user_review": true}
- **missing_session_identity**: {"flag_type": "missing_session_identity", "field": "in_game_date", "details": "in_game_date was not clearly found in the session log.", "requires_user_review": true}
- **missing_session_identity**: {"flag_type": "missing_session_identity", "field": "in_game_time_passage", "details": "in_game_time_passage was not clearly found in the session log.", "requires_user_review": true}
- **missing_session_identity**: {"flag_type": "missing_session_identity", "field": "primary_locations", "details": "primary_locations was not clearly found in the session log.", "requires_user_review": true}
- **missing_session_identity**: {"flag_type": "missing_session_identity", "field": "participating_pcs", "details": "participating_pcs was not clearly found in the session log.", "requires_user_review": true}
- **uncertain_source_text**: {"flag_type": "uncertain_source_text", "source_excerpt": "Line 203: - Destination unknown", "details": "The source text contains uncertainty language.", "requires_user_review": true}
- **Tonya (bartender**: {"flag_type": "mentioned_without_durable_update", "entity_name": "Tonya (bartender", "entity_type": "npcs", "details": "Entity was mentioned, but no durable change was detected.", "requires_user_review": false}
- **Pier 12 (North Side**: {"flag_type": "mentioned_without_durable_update", "entity_name": "Pier 12 (North Side", "entity_type": "locations", "details": "Entity was mentioned, but no durable change was detected.", "requires_user_review": false}
- **Siberian Wolf**: {"flag_type": "mentioned_without_durable_update", "entity_name": "Siberian Wolf", "entity_type": "locations", "details": "Entity was mentioned, but no durable change was detected.", "requires_user_review": false}
- **Crate**: {"flag_type": "mentioned_without_durable_update", "entity_name": "Crate", "entity_type": "items_or_artifacts", "details": "Entity was mentioned, but no durable change was detected.", "requires_user_review": false}
- **legacy_pre_standardization_format**: {"flag_type": "legacy_pre_standardization_format", "details": "SESSION_002 uses pre-standardization headings and separators; missing identity fields should be reviewed, not treated as extractor failure.", "requires_user_review": true}
- **Tonya (bartender**: {"flag_type": "malformed_entity_name", "entity_name": "Tonya (bartender", "entity_type": "npcs", "details": "Unclosed parenthetical; likely intended as Tonya with role bartender.", "requires_user_review": true}
- **Pier 12 (North Side**: {"flag_type": "malformed_entity_name", "entity_name": "Pier 12 (North Side", "entity_type": "locations", "details": "Unclosed parenthetical; likely intended as Pier 12 with North Side qualifier.", "requires_user_review": true}
- **UPDATED CANON VERSION**: {"flag_type": "malformed_entity_name", "entity_name": "UPDATED CANON VERSION", "entity_type": "npcs", "details": "Document status heading was detected as an NPC.", "requires_user_review": true}
- **Delivered**: {"flag_type": "malformed_entity_name", "entity_name": "Delivered", "entity_type": "npcs", "details": "Action/result word was detected as an NPC.", "requires_user_review": true}
- **Hired**: {"flag_type": "malformed_entity_name", "entity_name": "Hired", "entity_type": "npcs", "details": "Action/result word was detected as an NPC.", "requires_user_review": true}
- **Lost**: {"flag_type": "malformed_entity_name", "entity_name": "Lost", "entity_type": "npcs", "details": "Action/result word was detected as an NPC.", "requires_user_review": true}
- **Six**: {"flag_type": "malformed_entity_name", "entity_name": "Six", "entity_type": "npcs", "details": "Quantity from news report was detected as an NPC.", "requires_user_review": true}
- **Run**: {"flag_type": "malformed_entity_name", "entity_name": "Run", "entity_type": "jobs", "details": "Generic job/result label was detected as a job entity.", "requires_user_review": true}
- **Crate**: {"flag_type": "malformed_entity_name", "entity_name": "Crate", "entity_type": "pcs", "details": "Artifact/object was also detected as a PC.", "requires_user_review": true}
- **Crate**: {"flag_type": "possible_durable_update", "entity_name": "Crate", "entity_type": "items_or_artifacts", "source_excerpt": "Line 16: - Crate secured in team possession", "details": "Crate begins session secured by the team.", "requires_user_review": true}
- **Crate**: {"flag_type": "possible_durable_update", "entity_name": "Crate", "entity_type": "items_or_artifacts", "source_excerpt": "Line 20: → Banged up / scratched", "details": "Crate condition may matter for owner/upstream consequences.", "requires_user_review": true}
- **Blackjack**: {"flag_type": "possible_durable_update", "entity_name": "Blackjack", "entity_type": "npcs", "source_excerpt": "Line 153: - Payment increased:", "details": "Blackjack increases payment to 4,000¥ per runner and sets crate conditions.", "requires_user_review": true}
- **Team**: {"flag_type": "possible_durable_update", "entity_name": "Team", "entity_type": "pcs", "source_excerpt": "Line 179: - Team declines", "details": "Team declines to open the crate.", "requires_user_review": true}
- **Crate**: {"flag_type": "possible_durable_update", "entity_name": "Crate", "entity_type": "items_or_artifacts", "source_excerpt": "Line 207: - Crate transferred from Toggle → Mara", "details": "Crate appears transferred through Toggle to Mara/Boeing recovery.", "requires_user_review": true}
- **Lone Star**: {"flag_type": "possible_durable_update", "entity_name": "Lone Star", "entity_type": "factions", "source_excerpt": "Line 225: - Lone Star investigating:", "details": "Lone Star investigation expands to arson/deaths/possible murder charges.", "requires_user_review": true}
- **Run**: {"flag_type": "possible_durable_update", "entity_name": "Run", "entity_type": "jobs", "source_excerpt": "Line 270: - Run completed clean (externally)", "details": "Crate delivery run appears externally complete, with upstream complication risk.", "requires_user_review": true}
- **Ivan**: {"flag_type": "possible_durable_update", "entity_name": "Ivan", "entity_type": "npcs", "source_excerpt": "Line 289: - Request work from Tsar", "details": "Ivan/Russian Mafia contact gives Triad-monitoring directive.", "requires_user_review": true}
- **Blackjack**: {"flag_type": "possible_durable_update", "entity_name": "Blackjack", "entity_type": "npcs", "source_excerpt": "Line 329: - Missing / non-responsive (5 days)", "details": "Blackjack is missing or non-responsive for five days.", "requires_user_review": true}
- **fragile_reference**: {"flag_type": "fragile_reference", "source_excerpt": "Line 23: → Potential concern for original owner (Kestrel)", "details": "Original owner reference is not fully resolved in this session.", "requires_user_review": true}
- **fragile_reference**: {"flag_type": "fragile_reference", "source_excerpt": "Line 160: CHAIN OF RESPONSIBILITY (INFERRED)", "details": "Responsibility chain is explicitly inferred rather than confirmed.", "requires_user_review": true}
- **fragile_reference**: {"flag_type": "fragile_reference", "source_excerpt": "Line 203: - Destination unknown", "details": "Crate destination is unknown.", "requires_user_review": true}
- **fragile_reference**: {"flag_type": "fragile_reference", "source_excerpt": "Line 205: ASSUMED HANDOFF", "details": "Handoff from Toggle to Mara is labeled assumed.", "requires_user_review": true}
- **fragile_reference**: {"flag_type": "fragile_reference", "source_excerpt": "Line 272: → Crate condition may raise questions upstream", "details": "Upstream consequences are suggested but not confirmed.", "requires_user_review": true}
- **fragile_reference**: {"flag_type": "fragile_reference", "source_excerpt": "Line 292: - Chinese Triads pressuring smuggling routes", "details": "Triad pressure is reported but specific actors are not named.", "requires_user_review": true}

## User Decisions Required

- **Review real_world_date: real_world_date was not clearly found in the session log.**: {"decision": "Review real_world_date: real_world_date was not clearly found in the session log.", "source_excerpt": ""}
- **Review in_game_date: in_game_date was not clearly found in the session log.**: {"decision": "Review in_game_date: in_game_date was not clearly found in the session log.", "source_excerpt": ""}
- **Review in_game_time_passage: in_game_time_passage was not clearly found in the session log.**: {"decision": "Review in_game_time_passage: in_game_time_passage was not clearly found in the session log.", "source_excerpt": ""}
- **Review primary_locations: primary_locations was not clearly found in the session log.**: {"decision": "Review primary_locations: primary_locations was not clearly found in the session log.", "source_excerpt": ""}
- **Review participating_pcs: participating_pcs was not clearly found in the session log.**: {"decision": "Review participating_pcs: participating_pcs was not clearly found in the session log.", "source_excerpt": ""}
- **Review uncertain_source_text: The source text contains uncertainty language.**: {"decision": "Review uncertain_source_text: The source text contains uncertainty language.", "source_excerpt": "Line 203: - Destination unknown"}
- **Review legacy_pre_standardization_format: SESSION_002 uses pre-standardization headings and separators; missing identity fields should be reviewed, not treated as extractor failure.**: {"decision": "Review legacy_pre_standardization_format: SESSION_002 uses pre-standardization headings and separators; missing identity fields should be reviewed, not treated as extractor failure.", "source_excerpt": ""}
- **Review Tonya (bartender: Unclosed parenthetical; likely intended as Tonya with role bartender.**: {"decision": "Review Tonya (bartender: Unclosed parenthetical; likely intended as Tonya with role bartender.", "source_excerpt": ""}
- **Review Pier 12 (North Side: Unclosed parenthetical; likely intended as Pier 12 with North Side qualifier.**: {"decision": "Review Pier 12 (North Side: Unclosed parenthetical; likely intended as Pier 12 with North Side qualifier.", "source_excerpt": ""}
- **Review UPDATED CANON VERSION: Document status heading was detected as an NPC.**: {"decision": "Review UPDATED CANON VERSION: Document status heading was detected as an NPC.", "source_excerpt": ""}
- **Review Delivered: Action/result word was detected as an NPC.**: {"decision": "Review Delivered: Action/result word was detected as an NPC.", "source_excerpt": ""}
- **Review Hired: Action/result word was detected as an NPC.**: {"decision": "Review Hired: Action/result word was detected as an NPC.", "source_excerpt": ""}
- **Review Lost: Action/result word was detected as an NPC.**: {"decision": "Review Lost: Action/result word was detected as an NPC.", "source_excerpt": ""}
- **Review Six: Quantity from news report was detected as an NPC.**: {"decision": "Review Six: Quantity from news report was detected as an NPC.", "source_excerpt": ""}
- **Review Run: Generic job/result label was detected as a job entity.**: {"decision": "Review Run: Generic job/result label was detected as a job entity.", "source_excerpt": ""}
- **Review Crate: Artifact/object was also detected as a PC.**: {"decision": "Review Crate: Artifact/object was also detected as a PC.", "source_excerpt": ""}
- **Review Crate: Crate begins session secured by the team.**: {"decision": "Review Crate: Crate begins session secured by the team.", "source_excerpt": "Line 16: - Crate secured in team possession"}
- **Review Crate: Crate condition may matter for owner/upstream consequences.**: {"decision": "Review Crate: Crate condition may matter for owner/upstream consequences.", "source_excerpt": "Line 20: → Banged up / scratched"}
- **Review Blackjack: Blackjack increases payment to 4,000¥ per runner and sets crate conditions.**: {"decision": "Review Blackjack: Blackjack increases payment to 4,000¥ per runner and sets crate conditions.", "source_excerpt": "Line 153: - Payment increased:"}
- **Review Team: Team declines to open the crate.**: {"decision": "Review Team: Team declines to open the crate.", "source_excerpt": "Line 179: - Team declines"}
- **Review Crate: Crate appears transferred through Toggle to Mara/Boeing recovery.**: {"decision": "Review Crate: Crate appears transferred through Toggle to Mara/Boeing recovery.", "source_excerpt": "Line 207: - Crate transferred from Toggle → Mara"}
- **Review Lone Star: Lone Star investigation expands to arson/deaths/possible murder charges.**: {"decision": "Review Lone Star: Lone Star investigation expands to arson/deaths/possible murder charges.", "source_excerpt": "Line 225: - Lone Star investigating:"}
- **Review Run: Crate delivery run appears externally complete, with upstream complication risk.**: {"decision": "Review Run: Crate delivery run appears externally complete, with upstream complication risk.", "source_excerpt": "Line 270: - Run completed clean (externally)"}
- **Review Ivan: Ivan/Russian Mafia contact gives Triad-monitoring directive.**: {"decision": "Review Ivan: Ivan/Russian Mafia contact gives Triad-monitoring directive.", "source_excerpt": "Line 289: - Request work from Tsar"}
- **Review Blackjack: Blackjack is missing or non-responsive for five days.**: {"decision": "Review Blackjack: Blackjack is missing or non-responsive for five days.", "source_excerpt": "Line 329: - Missing / non-responsive (5 days)"}
- **Review fragile_reference: Original owner reference is not fully resolved in this session.**: {"decision": "Review fragile_reference: Original owner reference is not fully resolved in this session.", "source_excerpt": "Line 23: → Potential concern for original owner (Kestrel)"}
- **Review fragile_reference: Responsibility chain is explicitly inferred rather than confirmed.**: {"decision": "Review fragile_reference: Responsibility chain is explicitly inferred rather than confirmed.", "source_excerpt": "Line 160: CHAIN OF RESPONSIBILITY (INFERRED)"}
- **Review fragile_reference: Crate destination is unknown.**: {"decision": "Review fragile_reference: Crate destination is unknown.", "source_excerpt": "Line 203: - Destination unknown"}
- **Review fragile_reference: Handoff from Toggle to Mara is labeled assumed.**: {"decision": "Review fragile_reference: Handoff from Toggle to Mara is labeled assumed.", "source_excerpt": "Line 205: ASSUMED HANDOFF"}
- **Review fragile_reference: Upstream consequences are suggested but not confirmed.**: {"decision": "Review fragile_reference: Upstream consequences are suggested but not confirmed.", "source_excerpt": "Line 272: → Crate condition may raise questions upstream"}
- **Review fragile_reference: Triad pressure is reported but specific actors are not named.**: {"decision": "Review fragile_reference: Triad pressure is reported but specific actors are not named.", "source_excerpt": "Line 292: - Chinese Triads pressuring smuggling routes"}
