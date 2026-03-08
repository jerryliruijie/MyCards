# Product Spec

## Product Name
MyCards - Personal Collectibles Vault

## Purpose
A personal inventory and portfolio tracker for sports cards, TCG cards, and other collectible cards.

## Core Jobs to be Done
- Track cards and associated metadata in a structured inventory
- Store multiple card images
- Track acquisition cost and fees through purchase lots
- Organize cards into physical/portfolio storage positions
- Track historical valuations from manual and external sources
- Compute card-level and portfolio-level unrealized PnL

## Non-goals
- Marketplace and listings
- Auction engine
- Social interactions
- Heavy enterprise auth/tenant features

## User Profile (v1)
- Primary: single owner/operator
- Secondary (future): additional users via incremental auth and ownership rules

## Domain Principles
- `Card` is the collectible entity; it is not bound to a purchase lot or single price source.
- Price snapshots are append-only and source-aware.
- Manual valuation remains available even after auto pricing integrations.
- Structured columns are preferred over opaque JSON for core filter/search fields.

## v1 Features

### Inventory
- Card CRUD
- Card core info includes: custom title, image, buy price, and manually entered current market price
- Search/filter by sport, player, team, brand, set, card type, grading company, tags
- Multi-image support

### Cost Basis
- Purchase lot CRUD per card
- Cost + fees + quantity-aware records

### Storage
- Hierarchical storage positions
- Assign card quantities to storage positions

### Pricing + Valuation
- Manual valuation entries
- Price snapshots by source/provider
- Portfolio summary with:
  - total cost basis
  - latest valuation
  - unrealized PnL (absolute + percentage)

### Tags
- Tag CRUD
- Card-tag assignment

## API Style
- RESTful JSON endpoints under `/api/v1`
- Helpful validation errors
- Clear route grouping by aggregate root

## Performance and Scale (v1)
- Designed for personal collection size (hundreds to low tens of thousands of records)
- Avoid premature optimization
- Add indexes on common filtering fields and snapshot lookup paths

## Security (v1)
- Auth optional
- Include minimal user-ready schema for future migration
- Add TODO markers where auth boundaries will later apply

## UI Scope (v1)
- Dashboard
- Card list
- Card detail
- Add/edit card
- Storage manager

## Design Workflow Rule
Before polished UI implementation for major screens, produce wireframes/page specs for review.

