# Asset Operations System

## Status

**Locked for playtesting.** This document records the current rules for operating businesses and other durable assets in Shadowrun Third Edition. The system extends the Detailed Lifestyle framework without becoming a separate accounting game.

Rules should be applied consistently. New exceptions are created only when a concrete narrative case cannot be handled by an existing standard. The Asset Network layer for organizations larger than a single Opulent asset is deferred.

## Core Terms

An **asset** is a durable operation such as a business, clinic, safehouse, warehouse, theater company, bar, route, or similar organization.

The **Business Level** establishes the asset's monetary scale, base Operations Target Number, included operational profile, Asset Point price, Income value, and Surplus value.

The **Operational Rating Total** is the sum of Income, Comforts, Entertainment, Furnishings, Security, and Space. Area is never included.

## Business-Level Scale

Street is not a valid Business Level. The single-asset system begins at Squatter and ends at Opulent.

| Business Level | Level Rating | Monthly Value | Base Operations TN | Asset Point Price | Included Operational Points |
|---|---:|---:|---:|---:|---:|
| Squatter | 1 | 100 nuyen | 2 | 5,000 nuyen | 6 |
| Low | 2 | 1,000 nuyen | 3 | 10,000 nuyen | 7 |
| Middle | 3 | 5,000 nuyen | 4 | 15,000 nuyen | 8 |
| High | 4 | 10,000 nuyen | 5 | 20,000 nuyen | 9 |
| Luxury | 5 | 100,000 nuyen | 6 | 25,000 nuyen | 10 |
| Opulent | 6 | 500,000 nuyen | 7 | 30,000 nuyen | 11 |

The cost progression above Luxury continues the existing repeating multiplier cycle of x10, x5, x2. Opulent uses 500,000 nuyen monthly. The next financial basis above Opulent is 1,000,000 nuyen monthly, but it is not a supported single-asset operating level.

TN 7 is intentionally retained for Opulent. Under the Rule of Six, TN 7 has the same undamaged success probability as TN 6, but any +1 modifier raises it to TN 8. Opulent operations therefore have no margin for adversity.

## Business Property and Permanent Ownership

A business carries the financial basis of one lifestyle level above the level at which it operates.

| Business Operates At | Required Financial Basis |
|---|---|
| Squatter | Low |
| Low | Middle |
| Middle | High |
| High | Luxury |
| Luxury | Opulent |
| Opulent | Next extrapolated basis: 1,000,000 nuyen monthly |

A permanent purchase costs 100 times the required monthly financial basis. A permanently purchased business operates at its lower actual Business Level. No separate prepaid modifier is applied.

Example:

```text
Siberian Wolf permanent purchase basis: Middle
Siberian Wolf operating level: Low
Permanent business purchase: 5,000 nuyen x 100 = 500,000 nuyen
```

Permanent ownership removes the higher recurring financial burden. It does not lower the asset's designed operational ratings.

## Asset Profile

Every asset records:

- Area
- Income
- Comforts
- Entertainment
- Furnishings
- Security
- Space
- Asset Edges
- Asset Flaws
- Operational Condition
- External Condition
- Operational Surplus
- Social Capital Surplus

### Operational Categories

Income, Comforts, Entertainment, Furnishings, Security, and Space are operational ratings.

```text
Minimum category rating: 1
Maximum category rating: 6
```

Monthly required successes may exceed 6 because of Area pressure, Asset Flaws, or explicit situational requirements. Rating measures built capability; requirements above the rating measure pressure on that capability.

### Included Baseline

The base Business Level includes Rating 1 in every operational category and enough additional Income to meet that level's Income baseline.

| Business Level | Income | Comforts | Entertainment | Furnishings | Security | Space | Total Included |
|---|---:|---:|---:|---:|---:|---:|---:|
| Squatter | 1 | 1 | 1 | 1 | 1 | 1 | 6 |
| Low | 2 | 1 | 1 | 1 | 1 | 1 | 7 |
| Middle | 3 | 1 | 1 | 1 | 1 | 1 | 8 |
| High | 4 | 1 | 1 | 1 | 1 | 1 | 9 |
| Luxury | 5 | 1 | 1 | 1 | 1 | 1 | 10 |
| Opulent | 6 | 1 | 1 | 1 | 1 | 1 | 11 |

All operational points above the included baseline are purchased at the current Asset Point price.

## Initial Creation Cost

```text
Total Initial Cost =
Base business/property cost
+ Net purchased point cost
```

```text
Net Purchased Points =
Additional operational points above baseline
+ Asset Edge points
- Credited Asset Flaw points
```

Each Net Purchased Point costs the Business Level's Asset Point price.

Asset Flaw credit may offset only purchased operational points and Asset Edge points. It cannot reduce the base business/property cost or included baseline points. Flaw credit beyond the points available to offset is unused and never paid as cash.

## Area and Fixed Pressure

Area describes the environment surrounding the asset. It does not contribute to the Asset Pool and has no separate purchase price.

Before a player establishes or purchases an asset, the GM must disclose the Area rating and its fixed operational pressures. The asset profile records the affected category, added monthly requirement, narrative cause, and likely consequence.

| Area Rating | Fixed Pressure |
|---:|---|
| 1 | Two categories each receive +1 required monthly success |
| 2 | One category receives +1 required monthly success |
| 3 | No added requirement |
| 4 | No added requirement |
| 5 | One category receives +1 required monthly success |
| 6 | Two categories each receive +1 required monthly success |

An Area pressure:

- Adds +1 required monthly success to its assigned category.
- Does not increase the category rating.
- Does not generate Asset Pool dice.
- Does not count as a purchased Asset Point.
- Remains fixed unless the asset moves or the Area materially changes.

Owners may purchase operational points or Asset Edges to build capacity against Area pressure. If they choose to operate at a deficit, they accept the resulting scramble, Surplus expenditure, and Condition damage.

## Asset Pool

```text
Operational Rating Total =
Income + Comforts + Entertainment + Furnishings + Security + Space
```

```text
Base Weekly Asset Pool =
Operational Rating Total / 3, round down
```

The Asset Pool represents recurring institutional capacity. It refreshes for each weekly Operations Roll. Unused dice do not carry forward as dice.

Area, Surplus, management skills, Edge dice, and Flaw requirements are not included in the Operational Rating Total.

## Monthly Extended Operations Test

Operations are resolved as one monthly Extended Test made through four weekly rolls.

```text
Weekly Operations Roll =
Asset Pool
+ contributed operational-role dice
+ active 1-3 point Asset Edge dice
```

Each operational category requires monthly successes equal to its rating, plus fixed Area, Flaw, and situational requirements.

```text
Rating 1 requires 1 monthly success.
Rating 2 requires 2 monthly successes.
Rating 3 requires 3 monthly successes.
Rating 4 requires 4 monthly successes.
Rating 5 requires 5 monthly successes.
Rating 6 requires 6 monthly successes.
```

Successes accumulate through the four weekly rolls. The manager may assign weekly successes immediately to known requirements or repairs, or bank them as Operational Surplus or Social Capital Surplus according to the narrative use.

### Managerial Triage

The manager is not required to meet current requirements before repairing existing damage. Successes may be allocated among:

- Current category requirements
- Repairing Operational Condition
- Repairing External Condition
- Building Operational Surplus
- Building Social Capital Surplus

After allocation:

1. Identify unmet category requirements.
2. Spend matching Surplus where the manager chooses.
3. Each uncovered missing success causes one Condition box.
4. The current story determines which Condition track receives that damage.

The category identifies what fell short. The narrative consequence determines whether the failure damages Operational Condition or External Condition. There are no default category-to-track mappings. Area pressures and Flaws may predetermine a consequence through their descriptions.

## Operational Roles and Work Hours

Any skill may serve as an operational role when it genuinely applies to work performed for that specific asset. The GM approves applicability.

Leadership and Negotiation are broadly useful. Professional, Knowledge, social, and technical skills apply only when the work and asset support them. Intimidation is not routinely applicable merely because it exists on a character sheet.

Every skill is a separate role and requires its own committed hours. The same hours cannot generate dice from more than one skill. There are no free complementary-skill or synergy dice.

Example: a character who spends 40 hours negotiating with vendors and customers receives the full Negotiation contribution. Receiving a full Leadership contribution during the same week requires another 40 hours of leadership and staff-management work, for 80 total hours.

Each role provides dice according to hours personally committed to that role during the week:

| Hours Committed to One Role | Skill Contribution |
|---:|---:|
| 10 | 25%, round down |
| 20 | 50%, round down |
| 30 | 75%, round down |
| 40 | 100% |
| More than 40 | Allocate the additional hours to another role or continue the same role, subject to the total weekly workload limit |

Fractions always round down. A Rating 3 skill therefore contributes 0 dice at 10 hours, 1 die at 20 hours, 2 dice at 30 hours, and 3 dice at 40 hours.

Hours may be divided among any number of approved roles. Calculate each role separately, round each result down, and add the resulting dice to the weekly Operations Roll. Multiple contributors may perform roles for the same asset.

### Total Weekly Workload and Fatigue

A person may perform no more than 80 effective hours of asset work in one week. Hours above 80 provide no dice and cannot be allocated to another role.

| Total Asset Work in One Week | Fatigue Consequence |
|---:|---|
| 0-40 hours | None |
| 41-50 hours | Automatic Moderate Stun |
| 51-60 hours | Automatic Serious Stun |
| 61-70 hours | Automatic Moderate Physical damage |
| 71-80 hours | Automatic Serious Physical damage |
| More than 80 hours | Not permitted; no additional benefit |

The listed consequence replaces, rather than stacks with, the lower workload consequence. An 80-hour week causes Serious Physical damage, not Serious Physical damage plus Stun. Fatigue damage is automatic and unresisted. Recovery follows the standard SR3 rules for the applicable damage type.

Example: The Chin has Negotiation 3 and Local Neighborhood Knowledge 3. At 40 total hours, he may devote all 40 hours to one role for 3 dice, or divide the hours and calculate each reduced contribution separately. To roll both complete Rating 3 pools in the same week, he must devote 40 hours to each role, work 80 total hours, and suffer automatic Serious Physical damage.

## Condition Tracks

Assets have two ten-box Condition tracks.

### Operational Condition

Internal function, including physical damage, maintenance, equipment, staffing, supplies, utilities, repairs, logistics, and cash-flow strain. Physical damage is included here and is not a separate track.

### External Condition

Outside pressure, including reputation, heat, customers, community relations, gangs, authorities, corporations, political pressure, and visibility.

### Condition Modifiers

| Boxes Filled | Level | Operations TN Modifier |
|---:|---|---:|
| 0 | Uninjured | None |
| 1-2 | Light | +1 |
| 3-5 | Moderate | +2 |
| 6-9 | Serious | +3 |
| 10 on one track | Deadly / Crippled | +3 |

Modifiers from both tracks are cumulative, following the standard Shadowrun wound-modifier model. Condition never removes rating-generated Asset Pool dice. The Asset Pool represents the operation's durable institutional capacity and remains independent of the manager and the Condition tracks.

### Repair

```text
1 success repairs 1 Condition box.
```

Repair is per box, not per category or wound band. Repair takes effect at the end of the week in which the success is assigned. The repaired Condition level applies to the following weekly roll.

### One Track at 10

The asset remains in operation while only one track is maxed.

- The maxed track contributes +3 TN.
- The rating-generated Asset Pool remains available.
- Management dice remain available.
- Active 1-3 point Edge dice remain available.
- Active 4-6 point Edges continue generating assigned Surplus.
- Successes remain freely allocable among requirements and repair.

Repairing the maxed track to 9 at the end of a week reduces it to Serious for narrative and tracking purposes; its +3 TN modifier remains until it is repaired below 6.

### Both Tracks at 10

If both tracks reach 10, the asset ceases to exist as a functioning operation. It cannot be restored through ordinary repair. A future operation must be created and funded from scratch.

The failed operation loses its operational ratings, Edges, Flaws, Surplus, and Business Level. A unique narrative condition may persist at the site and become a new Flaw only when a replacement asset is created.

## Surplus

Assets have two banked success buffers:

```text
Operational Surplus: 0-10
Social Capital Surplus: 0-10
```

Operational Surplus covers shortfalls that would cause Operational Condition. Social Capital Surplus covers shortfalls that would cause External Condition.

One matching Surplus point covers one missing success or prevents one matching Condition box. It is spent when used. Surplus does not count as a rolled success for producing additional Surplus.

Surplus may be cashed out at any time after it is generated. The pool does not need to reach 10. The cap only prevents additional points from being banked.

### Surplus Purchase and Cash-Out

```text
Value per Surplus Point =
10% of the asset's monthly Business Level value
```

| Business Level | Value per Surplus Point |
|---|---:|
| Squatter | 10 nuyen |
| Low | 100 nuyen |
| Middle | 500 nuyen |
| High | 1,000 nuyen |
| Luxury | 10,000 nuyen |
| Opulent | 50,000 nuyen |

Owners may buy Operational or Social Capital Surplus directly at this value, up to the relevant pool's cap of 10. Purchased Surplus follows all normal rules. There are no temporary investment dice.

One complete ten-point pool therefore costs one month of the current Business Level's value.

## Durable Asset Edges

Asset Edges are purchased, durable improvements such as trained staff, equipment, automation, contracts, infrastructure, reputation, or institutional support.

```text
Maximum Asset Edge points: 10
```

```text
Edge Cost =
Edge Points x Current Asset Point Price
```

### Edge Effects

| Edge Points | Effect |
|---:|---|
| 1 | +1 die to every weekly Operations Roll |
| 2 | +2 dice to every weekly Operations Roll |
| 3 | +3 dice to every weekly Operations Roll |
| 4 | Generate 4 guaranteed Surplus per month |
| 5 | Generate 5 guaranteed Surplus per month |
| 6 | Generate 6 guaranteed Surplus per month |

A 4-6 point Edge is assigned to either Operational Surplus or Social Capital Surplus when purchased. Its generated Surplus enters that pool at the beginning of each month and remains subject to the cap of 10.

The generated Surplus is a guaranteed matching success equivalent against shortfalls. It does not add dice, create profit by itself, repair damage, or advance another project.

### Edge Implementation

```text
Implementation Time = 1 week per Edge Point
```

One-to-three-point Edge dice begin on the first weekly Operations Roll after implementation. Four-to-six-point Edges begin generating Surplus at the first monthly cycle after implementation, then remain synchronized monthly.

Flaws apply immediately. Edges require their implementation time even when purchased during initial creation.

### Edge Durability

Ordinary Condition damage does not automatically disable an Edge. It remains active until liquidated, destroyed or disabled by a specific narrative event, made inapplicable by a material change, or removed through play.

Narrative events may grant an Edge. The GM determines whether it activates immediately or uses normal implementation time.

### Edge Liquidation

| Liquidation Method | Proceeds |
|---|---:|
| Urgent liquidation | 25% of current value |
| Normal liquidation | 50% of current value |
| Prepared favorable sale | Up to 75% of current value |

Equipment may be sold, staff contracts terminated, facilities stripped, access transferred, and reputation leveraged or staked. Liquidation ends the Edge's mechanical benefit. Liquidating an Edge is separate from cashing out Surplus.

## Asset Flaws

```text
Maximum Asset Flaw points: 10
```

### Basic Flaw Effects

| Flaw Points | Effect |
|---:|---|
| 1 | +1 required monthly success |
| 2 | +2 required monthly successes |
| 3 | +3 required monthly successes |
| 4 | 4 automatic Condition damage per month |
| 5 | 5 automatic Condition damage per month |
| 6 | 6 automatic Condition damage per month |

A 1-3 point Flaw identifies its narrative cause and affected category. A 4-6 point Flaw identifies its narrative cause and affected Condition track.

Custom Flaws may be negotiated with the GM when the proposed effect cannot be represented by the basic ladder. A custom Flaw may consume as many as all 10 available Flaw points.

### Flaw Timing

Flaws are inherent and apply immediately when an asset is created or acquired.

- A 1-3 point Flaw adds its requirement during the first month.
- A 4-6 point Flaw inflicts its rating in starting Condition damage.
- Automatic Flaw damage is resolved again at the end of each month.
- Matching Surplus may prevent automatic Flaw damage one for one.
- Uncovered damage carries into the next month.

A high-value Flaw can strike twice before a large Edge comes online: once as starting damage and again at the end of the first operational month. That risk is intentional.

### Buying Off Flaws

A Flaw may be purchased off only after one complete operational month in which:

- All category requirements are met or fully covered.
- The Flaw's additional requirement or automatic damage is fully covered.
- Operational Condition ends at 0.
- External Condition ends at 0.
- No uncovered shortfall remains.
- The narrative cause has been addressed.

```text
Flaw Buyoff Cost =
Flaw Points x Current Asset Point Price
```

The Flaw's final monthly effect is resolved before removal. A Flaw acquired through play grants no monetary credit, refund, cash payment, or retroactive purchase discount, but uses the normal buyoff requirements.

## Operational Point Improvements and Liquidation

### Purchasing a Rating Point

```text
Operational Point Cost = Current Asset Point Price
Implementation Time = 1 week per point
```

Funding may occur during implementation. Committed funds cannot be withdrawn, converted to Surplus, or used for another purpose. If funding is incomplete when the scheduled time ends, implementation continues until fully funded. Abandoning the work forfeits committed funds.

The point activates only after both time and funding requirements are satisfied.

### Liquidating a Rating Point

| Liquidation Method | Proceeds |
|---|---:|
| Urgent liquidation | 25% of current point value |
| Normal liquidation | 50% of current point value |
| Prepared favorable sale | Up to 75% of current point value |

Liquidation reduces the category rating, monthly requirement, Operational Rating Total, and Asset Pool calculation. No category may be reduced below 1. Income may not be reduced below the current Business Level baseline.

## Business Level Scale-Up

All Asset Points use one price line. A point purchased at a lower level reaches the same final investment as a point purchased directly at the higher level because each adjacent level adds 5,000 nuyen per scalable point.

```text
Scalable Point Total =
Operational Rating Total
+ Asset Edge points
- Credited Asset Flaw points
```

Area pressure is not a purchased point and is not included.

Credited Flaw points are limited to the purchased points they actually offset. Unused Flaw credit does not reduce scaling.

```text
Scale-Up Cost =
Scalable Point Total
x 5,000 nuyen
x Business Levels Increased
```

```text
Scale-Up Implementation Time =
Scalable Point Total
x Business Levels Increased
in weeks
```

In addition to the point scale-up cost, the owner must fund or assume the next required business/property financial basis.

Funds may be committed throughout implementation. Committed funds are tied up and unavailable. If full funding is not met by the scheduled completion, the project extends until it is funded. If abandoned, all committed funds are lost.

The old Business Level remains active during implementation. Nothing from the new level activates until both time and funding are complete. At completion, the new Income baseline, Target Number, point value, Surplus value, and financial scale activate together.

The new included Income point is covered by the Business Level upgrade and is not separately purchased.

## Business Level Downgrade

Lowering Business Level returns no scale-up investment. Future costs, point values, Income value, Surplus value, and base Target Number change to the lower level. Existing ratings and Edges retain their point ratings but are revalued downward. No refund is issued.

Income above the new minimum may remain or be liquidated separately under the normal operational-point rules.

## Property Salvage After Total Collapse

Total collapse destroys the operation, not automatically the underlying real estate. If permanently owned property remains legally and physically recoverable, its maximum retained value is capped by the Area-equivalent Business Level.

```text
Maximum Permanent Property Value =
Area-equivalent monthly value x 100
```

Use the lower of the property level actually purchased and the Area-equivalent cap.

| Area-Equivalent Level | Maximum Permanent Property Value |
|---|---:|
| Squatter | 10,000 nuyen |
| Low | 100,000 nuyen |
| Middle | 500,000 nuyen |
| High | 1,000,000 nuyen |
| Luxury | 10,000,000 nuyen |
| Opulent | 50,000,000 nuyen |

The standard liquidation rates apply: 25% urgent, 50% normal, and up to 75% favorable. Destruction, seizure, contamination, or another narrative event may reduce or eliminate salvage.

## Playtest Targets

The rules above are locked for testing. Testing should focus on concrete operation rather than designing exceptions in advance.

The first test asset will be the Siberian Wolf. Testing should verify:

- Weekly and monthly dice volume
- Success allocation and managerial triage
- Area pressure
- Condition progression and recovery
- Surplus generation, purchase, use, and cash-out
- Edge and Flaw timing
- Management-hour contributions and overtime
- Creation cost and Business Level scaling

Confirmed starting facts for the Siberian Wolf playtest:

```text
Operating Business Level: Low
Permanent purchase basis: lifetime Middle lifestyle
Operator: The Chin
Area: 2
Ratings: Income 2, Comforts 2, Entertainment 1,
         Furnishings 1, Security 2, Space 2
Operational Rating Total: 10
Weekly Asset Pool: 3 dice
Approved operational roles: Negotiation 3,
                            Local Neighborhood Knowledge 3
Role hours must be committed separately.
No complementary-skill or synergy rule applies.
Initial business/property purchase: 500,000 nuyen
Three added operational points: 30,000 nuyen
Three attached guest apartments: 70,000 nuyen
Complete initial property investment: 600,000 nuyen
```

After testing, the Siberian Wolf will be converted into the first Asset Character Sheet. The Asset Network system remains deferred.
