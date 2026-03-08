# Data Model

## Notes
- All major entities include `created_at` and `updated_at` timestamps where useful.
- `user_id` exists on key entities for future multi-user support, but v1 runs single-user by default.
- IDs are UUIDs for client/API friendliness and mobile-forward compatibility.

## Core reference entities
- User
- Sport
- Team
- Player
- Brand
- CardSet
- CardType
- GradingCompany
- PriceSource
- Tag

## Card aggregate

### Card
Represents the collectible object.

Key fields:
- `id`, `user_id`
- `title`, `description`
- `sport_id`, `team_id`, `player_id`
- `brand_id`, `set_id`, `card_type_id`
- `year`, `card_number`, `parallel`
- `grading_company_id`, `grade`, `serial_number`
- `condition_notes`

Constraints:
- Not coupled to any one purchase lot
- Not coupled to any one price provider

### CardImage
- multiple images per card
- `storage_key` is provider-agnostic path/key
- `is_primary` and `sort_order` support deterministic display

### CardTag
- many-to-many relationship between `Card` and `Tag`

## Cost basis entities

### PurchaseLot
- one card can have many purchase lots
- captures `purchased_at`, `quantity`, `unit_price`, `fees`, `tax`, `shipping`
- supports accurate total cost basis

### SaleLot (stub)
- included for future realized PnL and inventory reduction workflows

## Storage entities

### StoragePosition
- hierarchical location model (`parent_id`)
- examples: `Room -> Cabinet -> Box -> Slot`

### CardStorageAssignment
- maps quantity of a card to a position
- supports split storage across multiple positions

## Valuation entities

### PriceSnapshot
- append-only valuation record
- source-aware via `price_source_id`
- provider payload metadata available in optional note/metadata columns

### ManualValuation
- explicit manual price points
- can be used for override workflows and trusted local estimates

## Portfolio logic inputs

- Cost basis = sum of purchase lot totals per card
- Latest valuation = latest snapshot per card across enabled sources, with manual valuation fallback
- Unrealized PnL = latest valuation - cost basis

## Indexing recommendations
- `card(user_id, sport_id, player_id, set_id, card_type_id)`
- `price_snapshot(card_id, captured_at desc)`
- `purchase_lot(card_id, purchased_at desc)`
- `storage_position(parent_id)`
- `card_tag(tag_id, card_id)`
