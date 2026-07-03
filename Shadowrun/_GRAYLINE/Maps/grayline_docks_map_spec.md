# Grayline Docks Operational Map Specification

## Purpose
Create a black-and-white, blueprint-style operational district map for the Grayline Docks area in Tacoma's industrial sector for a Shadowrun 3rd Edition campaign.

This is not a tactical combat map. It is a district relationship and movement map.

## Style Requirements
- Black-and-white only.
- Blueprint / line-art style.
- Minimal shading.
- Printer-friendly.
- Clean labels.
- Hex overlay preferred if readable.
- Industrial schematic feel.
- Avoid clutter.
- Map should clearly communicate district layout from west to east and north to south.

## Orientation
- North is at the top.
- The Duwamish River runs roughly north-south through the district.
- The map should be readable as a west-to-east cross-section with additional southward dock movement.

## Core Geography
Grayline is divided by the Duwamish River.

### West Bank
The west side of the river contains:
1. Burnout Territory.
2. Rundown industrial district.
3. West-side dockfront.
4. Northern west dockfront commercial strip.
5. West-side docks.

The west bank is poorer, more decayed, and less controlled than the east bank.

### East Bank
The east side of the river contains:
1. East-side Grayline docks.
2. Rail spur along the dock territory.
3. Dock access road.
4. Industrial business fronts.
5. Alley behind the business fronts.
6. Rear side of the industrial block.
7. Street.
8. Wolf Block, one block inland from the docks.
9. Southern waterfront zones farther south: Cargo Pier, then Container Maze.

## West Bank Detail

### Burnout Territory
- Industrial and rundown.
- Derelict buildings.
- Poor utility access.
- Burned warehouse / burned-down warehouse where the crate was recovered.
- Controlled or heavily influenced by the Burnout gang.

### Northern West Dockfront Commercial Strip
Located on the northern part of the west dockfront.

Include:
- Stuffer Shack.
- Pawn shop.
- Liquor store.
- Small low-end commercial buildings.

This area serves Burnouts, truckers, dock workers, bridge traffic, and locals.

### West-Side Docks
- Industrial dockfront along the river.
- Smaller and rougher than the east-side docks.
- Active enough to matter, but less stable than the east bank.

## River and Bridge

### Duwamish River
- Runs north-south.
- Industrial waterway.
- Divides west bank and east bank.
- Wide enough for cargo traffic.

### Bridge
- Primary crossing between west bank and east bank.
- Choke point.
- Observation point.
- Natural boundary between Burnout influence and Grayline dock influence.

## East Bank Detail

### East-Side Grayline Docks
Immediately east of the river.

Include:
- Working docks.
- Cargo activity.
- Dock frontage.
- Pier structures.
- Industrial seawall edge.

### Rail Spur
- Runs along the east-side dock territory.
- Used for light freight.
- Should be parallel or near-parallel to the waterfront/dock access structure.

### Dock Access Road
- Main working road serving docks and freight businesses.
- Runs through the east-bank dock area.
- Connects to cargo pier and southern dock areas.

### Industrial Business Fronts
Located inland from the dock access road.

Include businesses such as:
- Freight offices.
- Warehouse offices.
- Machine shops.
- Repair facilities.
- Loading contractors.
- Dock support services.

### Alley and Rear Service Access
Behind the industrial business fronts:
- Alley network.
- Rear doors.
- Loading access.
- Service entrances.
- Back side of industrial buildings.

### Street
A street separates the rear service side of the dockside industrial block from the next inland block.

## Wolf Block

### Position
- East bank.
- One block inland from the docks.
- Not on the waterfront.
- Not behind or inside the container maze.
- The Wolf Block is part of the living working neighborhood, not the cargo terminal.

### Character
- Mixed-use industrial block.
- Mostly two-story buildings.
- Ground floors contain small businesses, workshops, storage, and offices.
- Upper floors contain apartments, lofts, and temporary housing.

### Siberian Wolf
- Located mid-block on Wolf Block.
- Two-story structure.
- Dive bar / community hub / neutral ground / meeting place.
- Not directly on a corner.
- Not directly waterfront-facing.

### South End of Wolf Block
At the southern tip of Wolf Block, include:
- Electronics repair store.
- Telecom kiosk outside.
- This is the location where Donnie's car was found.

## Southern East-Bank Dock Movement
From the east-side docks, if traveling south along the waterfront by a few blocks, the order is:

1. Cargo Pier.
2. Beginning of the Container Maze.
3. Southern edge of Brigata 12 territory.

### Cargo Pier
- Located south along the east-bank waterfront.
- Comes before the Container Maze.
- Large cargo facility.
- Cargo staging.
- Warehouses.
- Loading zones.
- Dock frontage.

### Container Maze
- Located south of the Cargo Pier.
- Dockside feature, not inland.
- Dense cargo container storage area.
- Stacked containers.
- Narrow corridors.
- Blind corners.
- Hard to navigate.
- Smuggling routes and hidden storage.
- Marks the edge of Brigata 12 territory.

### Brigata 12 Territory
- Brigata 12 controls or strongly influences the east-bank Grayline dock area.
- The beginning of the Container Maze marks the southern edge of established Brigata 12 control.
- North of the Container Maze: stronger Brigata 12 influence.
- South of the Container Maze: weaker control and greater uncertainty.

## Required Labels
Use these exact labels where possible:

- GRAYLINE DOCKS
- TACOMA INDUSTRIAL SECTOR
- DUWAMISH RIVER
- WEST BANK
- BURNOUT TERRITORY
- BURNED WAREHOUSE / CRATE RECOVERY SITE
- NORTHERN WEST DOCKFRONT COMMERCIAL STRIP
- STUFFER SHACK
- PAWN SHOP
- LIQUOR STORE
- WEST SIDE DOCKS
- BRIDGE / CHECKPOINT CROSSING
- EAST BANK
- EAST-SIDE GRAYLINE DOCKS
- RAIL SPUR
- DOCK ACCESS ROAD
- INDUSTRIAL BUSINESS FRONTS
- ALLEY
- REAR SERVICE ACCESS
- STREET
- WOLF BLOCK
- SIBERIAN WOLF
- ELECTRONICS REPAIR STORE
- TELECOM KIOSK
- DONNIE'S CAR LOCATION
- CARGO PIER
- CONTAINER MAZE
- SOUTHERN EDGE OF BRIGATA 12 TERRITORY

## Important Negative Constraints
Do not place the Container Maze between the Cargo Pier and the Wolf Block as an inland barrier.
Do not place the Siberian Wolf on the dockfront.
Do not place the Siberian Wolf inside the Container Maze.
Do not place the Stuffer Shack on the east bank.
Do not make the west bank more developed than the east bank.
Do not make this a detailed tactical combat map.

## Simple Layout Logic
West to east:

Burnout industrial district -> west dockfront commercial strip and west docks -> Duwamish River -> east-side docks -> rail spur -> dock access road -> industrial business fronts -> alley -> rear service access -> street -> Wolf Block with Siberian Wolf.

Southward along east-side waterfront:

East-side Grayline Docks -> Cargo Pier -> Container Maze -> southern edge of Brigata 12 territory.

## Suggested ASCII Blocking

```text
WEST                                                        EAST

[BURNOUT TERRITORY]
[rundown industrial blocks]
[burned warehouse / crate recovery site]

[NORTHERN WEST DOCKFRONT COMMERCIAL STRIP]
[Stuffer Shack] [Pawn Shop] [Liquor Store]

[WEST SIDE DOCKS]

==================== DUWAMISH RIVER ====================

[EAST-SIDE GRAYLINE DOCKS]
[RAIL SPUR]
[DOCK ACCESS ROAD]
[INDUSTRIAL BUSINESS FRONTS]
[ALLEY]
[REAR SERVICE ACCESS]
[STREET]

[WOLF BLOCK]
        [SIBERIAN WOLF - mid-block]
        [Electronics Repair Store + Telecom Kiosk]
        [Donnie's Car Location]

South along east-bank waterfront:

[EAST-SIDE GRAYLINE DOCKS]
        ↓
[CARGO PIER]
        ↓
[CONTAINER MAZE]
        ↓
[SOUTHERN EDGE OF BRIGATA 12 TERRITORY]
```

## One-Sentence Map Summary
Grayline is an industrial district split by the Duwamish River: the west bank is Burnout-controlled decay with the Stuffer Shack on the northern west dockfront, while the east bank holds the working Grayline docks, rail spur, dock access road, industrial fronts, and the Wolf Block one block inland; farther south along the east waterfront, the Cargo Pier leads into the Container Maze, which marks the southern edge of Brigata 12 territory.
