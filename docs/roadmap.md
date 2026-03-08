# Roadmap

## Guiding constraints
- Keep the codebase easy to run and maintain solo
- Prefer clear modular boundaries over framework-heavy indirection
- Preserve forward compatibility for mobile client and real pricing providers

## Phase 0 - Foundation (this pass)
- Monorepo setup (`apps/api`, `apps/web`, `docs`)
- Product docs + data model docs
- FastAPI and Next.js scaffolds
- Core domain models and initial migration
- Initial inventory/portfolio API endpoints
- Pricing provider adapter interface + mock provider
- Seed data and local development setup
- Lint/test setup and GitHub Actions
- Wireframe proposal for UI review

## Phase 1 - Core usability
- Better card list filtering and pagination
- Add/edit workflows with stronger form validation
- Card image upload management UX
- Storage hierarchy management UX improvements
- Dashboard summary cards and trend view
- CSV export/import for backup and migration

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
