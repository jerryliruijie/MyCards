# Project Structure Proposal

## Why this structure

A lightweight monorepo keeps product docs, backend, and frontend aligned without introducing heavy tooling.

## Layout

- `apps/api`
  - `app/models`: SQLModel entities (domain persistence shape)
  - `app/repositories`: DB access concerns
  - `app/services`: domain/application logic
  - `app/api/routes`: HTTP routing
  - `app/integrations`: external adapters (pricing provider boundary)
  - `app/workers`: background job entry points
  - `alembic`: migration scripts
- `apps/web`
  - `app`: Next.js app router pages
  - `components`: reusable UI blocks
  - `lib`: typed API client and helpers
  - `types`: shared frontend types
- `docs`
  - Product, roadmap, data model, wireframes, technical decisions
- `infra`
  - Local infrastructure templates (`docker-compose`)

## Fit with project goals

- Fast solo iteration: low ceremony, straightforward folders
- Future mobile support: API/domain is independent from web rendering
- Pricing extensibility: provider adapter pattern is isolated
- Maintainability: small modules with explicit boundaries
