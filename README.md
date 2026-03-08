# MyCards

MyCards is an open-source personal collectibles vault focused on sports cards, TCG cards, and other collectible cards.

It is intentionally:
- Personal-use first
- Web-first for fast iteration
- Modular but lightweight
- Easy to self-host

## Stack

- Frontend: Next.js + TypeScript + Tailwind CSS
- Backend API: FastAPI + SQLModel
- Database: PostgreSQL
- Background jobs: lightweight Python worker (extensible)
- Image storage: local filesystem in development, pluggable provider for S3 later

## Monorepo Layout

- `apps/api`: FastAPI backend
- `apps/web`: Next.js web frontend
- `docs`: product and architecture docs
- `.github/workflows`: CI pipelines
- `infra`: optional infra templates and local setup helpers

## Architecture Summary

The backend is split into layers:
- `models`: SQLModel entities and relational constraints
- `repositories`: persistence logic
- `services`: domain logic and composition
- `api/routes`: HTTP routers
- `integrations/pricing`: provider adapter interface + mock provider

Key decisions:
- A `Card` is independent from any single purchase or price source
- Price history is append-only with provider/source awareness
- Storage positions are hierarchical (parent-child)
- Manual valuation is first-class for user override and one-off estimates

## Quick Start (Development)

### 1. Prerequisites

- Python 3.12+
- Node.js 20+
- PostgreSQL 15+

### 2. Backend

```bash
cd apps/api
python -m venv .venv
. .venv/Scripts/activate  # Windows PowerShell: .\.venv\Scripts\Activate.ps1
pip install -e .[dev]
copy .env.example .env
alembic upgrade head
python -m app.db.seed
uvicorn app.main:app --reload --port 8000
```

### 3. Frontend

```bash
cd apps/web
npm install
copy .env.example .env.local
npm run dev
```

Open:
- Web: `http://localhost:3000`
- API docs: `http://localhost:8000/docs`

## Environment Variables

### API (`apps/api/.env`)

- `DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/mycards`
- `STORAGE_DIR=./storage`

### Web (`apps/web/.env.local`)

- `NEXT_PUBLIC_API_BASE_URL=http://localhost:8000/api/v1`

## Milestones (v1 foundation)

- [x] Product docs + data model + roadmap
- [x] Domain model + migration scaffolding
- [x] FastAPI endpoint scaffolding for core inventory workflows
- [x] Pricing provider interface + mock implementation
- [x] Next.js web scaffolding + typed API client
- [x] Wireframe proposal for UI review before polished UI

## Non-goals

- Marketplace
- Auctions
- Social features
- Heavy enterprise auth/multi-tenant complexity in v1

## Future-facing Notes

- API and DB already include a minimal `User` for future multi-user migration.
- Pricing integrations are behind an adapter interface, so real providers can be added without rewriting domain logic.
- Auth is intentionally optional in v1 and marked with explicit TODOs.
