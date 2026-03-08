# UI Wireframe Proposal (Review Before Polished UI)

This is the proposed direction for v1 web pages.

## Layout System

- App shell: left sidebar + top utility bar + main content
- Dense data tables for list views
- Sticky filter bar for card list
- Right-side contextual detail panel on larger screens

## 1) Dashboard

Sections:
- Header: portfolio total value, cost basis, unrealized PnL
- KPI row:
  - total cards
  - total unique sets
  - valued today count
  - stale price count
- Valuation trend panel (simple line chart placeholder)
- Storage distribution panel (cards by top-level storage)
- Recent activity list (new cards, purchases, valuations)

## 2) Card List

- Top actions: add card, import CSV (future), refresh prices (future)
- Filter row: sport, player, team, brand, set, grading, tags, text search
- Sort controls: updated, value, pnl, year
- Main table columns:
  - thumbnail
  - card title
  - player/team
  - set/year/number
  - grade
  - qty
  - cost basis
  - latest value
  - unrealized pnl
  - storage

## 3) Card Detail

- Left: image gallery (primary + thumbnails)
- Middle: core card metadata blocks
- Right: valuation summary and quick actions
- Tab sections:
  - Purchase lots
  - Storage assignments
  - Price history
  - Tags and notes

## 4) Add/Edit Card

- Structured form grouped into:
  - Identity (title/year/card number/parallel)
  - Classification (sport/player/team/brand/set/type)
  - Grading
  - Notes
- Inline section for initial purchase lot (optional)
- Inline section for initial manual valuation (optional)

## 5) Storage Manager

- Split pane:
  - left tree view of storage hierarchy
  - right table of assigned cards + quantities
- Actions: add child position, rename, assign card, move assignment

## Interaction Notes
- Prioritize keyboard-friendly table/filter interactions
- Favor fewer clicks over decorative transitions
- Errors must be field-specific and actionable

## Review Questions
- Is the dense table-first approach aligned with your workflow?
- Do you want card detail as a dedicated page only, or optional slide-over from the list?
- Should dashboard prioritize trend chart or recent activity first?
