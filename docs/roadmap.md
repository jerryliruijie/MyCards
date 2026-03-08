# Roadmap

## Guiding constraints
- Keep the codebase easy to run and maintain solo
- Prefer clear modular boundaries over framework-heavy indirection
- Preserve forward compatibility for mobile client and real pricing providers

## Phase 0 - Foundation (completed)
- [x] Monorepo setup (`apps/api`, `apps/web`, `docs`)
- [x] Product docs + data model docs
- [x] FastAPI and Next.js scaffolds
- [x] Core domain models and initial migration
- [x] Initial inventory/portfolio API endpoints
- [x] Pricing provider adapter interface + mock provider
- [x] Seed data and local development setup
- [x] Lint/test setup and GitHub Actions
- [x] Wireframe proposal for UI review
- [x] Core card info flow (custom title, image, buy price, manual market price)
- [x] Local image upload + media serving (`/media`)

## Phase 1 - Core usability (in progress)
- [ ] Better card list filtering, sorting, and pagination
- [ ] Add/edit workflows with stronger form validation
- [ ] Card image management UX (multi-image, primary switch, delete, reorder)
- [ ] Storage hierarchy management UX improvements
- [ ] Dashboard summary cards and trend view
- [ ] CSV export/import for backup and migration

## Phase 2 - Pricing maturity
- Scheduled price ingestion job runner
- Additional provider adapters (with feature flags)
- Source confidence metadata and reconciliation view
- Price freshness indicators and stale warnings

## Phase 3 - Personal operations quality
- Backup/restore command set
- Attachments lifecycle cleanup tools
- Basic auth + ownership enforcement (optional toggle)
- iPhone packaging strategy (PWA first, then native wrapper if needed)

## Out-of-scope until explicitly requested
- Marketplace capabilities
- Social feeds or public profiles
- Enterprise role and permission systems
