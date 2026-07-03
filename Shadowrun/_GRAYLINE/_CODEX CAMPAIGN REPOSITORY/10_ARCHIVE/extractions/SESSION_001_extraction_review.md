# Session Extraction Review

Source: `C:\CAMPAIGN_REPOSITORY\02_SESSIONS\SESSION_001.MD`

## Session Identity

- session_number: 001
- real_world_date: 
- in_game_date: May 24, 2057
- in_game_time_passage: 
- primary_locations: ['Siberian Wolf (Bar + Apartments']
- participating_pcs: []

## Extracted Entities

### Pcs
_None detected._

### Npcs
- Bikes
- Burnouts
- Crate
- Delivered
- Kestrel
- LOOT RECOVERED
- Origin
- Siberian Wolf
- Squatter
- Switch
- The Chin

### Factions
_None detected._

### Locations
- Siberian Wolf (Bar + Apartments

### Jobs
_None detected._

### Clues
_None detected._

### Threads
_None detected._

### Items Or Artifacts
_None detected._

## Proposed Updates

### Npc Updates
- **Delivered**: {"entity_name": "Delivered", "entity_type": "npc", "update_type": "resolution", "update_text": "Delivered via Switch to The Chin", "source_excerpt": "Line 26: - Delivered via Switch to The Chin", "confidence": "high", "recommended_repository_area": "NPC files", "requires_user_review": true}
- **Switch**: {"entity_name": "Switch", "entity_type": "npc", "update_type": "resolution", "update_text": "Delivered via Switch to The Chin", "source_excerpt": "Line 26: - Delivered via Switch to The Chin", "confidence": "high", "recommended_repository_area": "NPC files", "requires_user_review": true}
- **The Chin**: {"entity_name": "The Chin", "entity_type": "npc", "update_type": "resolution", "update_text": "Delivered via Switch to The Chin", "source_excerpt": "Line 26: - Delivered via Switch to The Chin", "confidence": "high", "recommended_repository_area": "NPC files", "requires_user_review": true}
- **Siberian Wolf**: {"entity_name": "Siberian Wolf", "entity_type": "npc", "update_type": "event", "update_text": "• Squatter status at Siberian Wolf secured", "source_excerpt": "Line 30: • Squatter status at Siberian Wolf secured", "confidence": "high", "recommended_repository_area": "NPC files", "requires_user_review": true}
- **Squatter**: {"entity_name": "Squatter", "entity_type": "npc", "update_type": "event", "update_text": "• Squatter status at Siberian Wolf secured", "source_excerpt": "Line 30: • Squatter status at Siberian Wolf secured", "confidence": "high", "recommended_repository_area": "NPC files", "requires_user_review": true}
- **Burnouts**: {"entity_name": "Burnouts", "entity_type": "npc", "update_type": "event", "update_text": "Burnouts stole cargo more dangerous than weapons", "source_excerpt": "Line 34: - Burnouts stole cargo more dangerous than weapons", "confidence": "high", "recommended_repository_area": "NPC files", "requires_user_review": true}
- **The Chin**: {"entity_name": "The Chin", "entity_type": "npc", "update_type": "event", "update_text": "• The Chin (exposed, elevated", "source_excerpt": "Line 84: • The Chin (exposed, elevated)", "confidence": "high", "recommended_repository_area": "NPC files", "requires_user_review": true}
- **Bikes**: {"entity_name": "Bikes", "entity_type": "npc", "update_type": "resolution", "update_text": "Bikes destroyed", "source_excerpt": "Line 101: - Bikes destroyed", "confidence": "high", "recommended_repository_area": "NPC files", "requires_user_review": true}
- **Crate**: {"entity_name": "Crate", "entity_type": "npc", "update_type": "event", "update_text": "Crate located and secured", "source_excerpt": "Line 106: - Crate located and secured", "confidence": "high", "recommended_repository_area": "NPC files", "requires_user_review": true}
- **Crate**: {"entity_name": "Crate", "entity_type": "npc", "update_type": "event", "update_text": "✔ Crate recovered", "source_excerpt": "Line 130: ✔ Crate recovered", "confidence": "high", "recommended_repository_area": "NPC files", "requires_user_review": true}
- **Kestrel**: {"entity_name": "Kestrel", "entity_type": "npc", "update_type": "discovery", "update_text": "✔ Origin partially identified (Kestrel markings", "source_excerpt": "Line 132: ✔ Origin partially identified (Kestrel markings)", "confidence": "high", "recommended_repository_area": "NPC files", "requires_user_review": true}
- **Origin**: {"entity_name": "Origin", "entity_type": "npc", "update_type": "discovery", "update_text": "✔ Origin partially identified (Kestrel markings", "source_excerpt": "Line 132: ✔ Origin partially identified (Kestrel markings)", "confidence": "high", "recommended_repository_area": "NPC files", "requires_user_review": true}
- **LOOT RECOVERED**: {"entity_name": "LOOT RECOVERED", "entity_type": "npc", "update_type": "event", "update_text": "LOOT RECOVERED", "source_excerpt": "Line 135: [ LOOT RECOVERED ]", "confidence": "high", "recommended_repository_area": "NPC files", "requires_user_review": true}

### Faction Updates
_None detected._

### Location Updates
_None detected._

### Pc Updates
_None detected._

### Job Updates
_None detected._

### Clue Updates
_None detected._

### Thread Updates
_None detected._

## Downstream File Impacts

- **NPC files**: {"repository_area": "NPC files", "entities": ["Bikes", "Burnouts", "Crate", "Delivered", "Kestrel", "LOOT RECOVERED", "Origin", "Siberian Wolf", "Squatter", "Switch", "The Chin"], "recommended_action": "Review staged extraction before updating any canon file.", "requires_user_review": true}

## Reconciliation Flags

- **missing_session_identity**: {"flag_type": "missing_session_identity", "field": "real_world_date", "details": "real_world_date was not clearly found in the session log.", "requires_user_review": true}
- **missing_session_identity**: {"flag_type": "missing_session_identity", "field": "in_game_time_passage", "details": "in_game_time_passage was not clearly found in the session log.", "requires_user_review": true}
- **missing_session_identity**: {"flag_type": "missing_session_identity", "field": "participating_pcs", "details": "participating_pcs was not clearly found in the session log.", "requires_user_review": true}
- **uncertain_source_text**: {"flag_type": "uncertain_source_text", "source_excerpt": "Line 24: - Origin: Unknown", "details": "The source text contains uncertainty language.", "requires_user_review": true}
- **Siberian Wolf (Bar + Apartments**: {"flag_type": "mentioned_without_durable_update", "entity_name": "Siberian Wolf (Bar + Apartments", "entity_type": "locations", "details": "Entity was mentioned, but no durable change was detected.", "requires_user_review": false}

## User Decisions Required

- **Review real_world_date: real_world_date was not clearly found in the session log.**: {"decision": "Review real_world_date: real_world_date was not clearly found in the session log.", "source_excerpt": ""}
- **Review in_game_time_passage: in_game_time_passage was not clearly found in the session log.**: {"decision": "Review in_game_time_passage: in_game_time_passage was not clearly found in the session log.", "source_excerpt": ""}
- **Review participating_pcs: participating_pcs was not clearly found in the session log.**: {"decision": "Review participating_pcs: participating_pcs was not clearly found in the session log.", "source_excerpt": ""}
- **Review uncertain_source_text: The source text contains uncertainty language.**: {"decision": "Review uncertain_source_text: The source text contains uncertainty language.", "source_excerpt": "Line 24: - Origin: Unknown"}
