# Technical Decisions

## 1. Monorepo (`apps/api` + `apps/web`)
Chosen for shared product context, synchronized docs, and easier single-developer iteration.

## 2. SQLModel + PostgreSQL
SQLModel gives typed models with low ceremony while retaining SQLAlchemy/Alembic flexibility.

## 3. Layered backend
- `models` for domain persistence schema
- `repositories` for data access
- `services` for domain logic
- `api/routes` for transport
This keeps endpoint handlers small and testable.

## 4. Pricing provider adapter boundary
Pricing access goes through adapter interfaces in `app/integrations/pricing`.
This avoids coupling the card domain to any one provider and keeps future provider additions incremental.

## 5. Append-only price history
`PriceSnapshot` rows are never overwritten to preserve historical analytics and source traceability.

## 6. Future-ready single-user design
A minimal `User` model and `user_id` foreign keys exist now, but auth is deferred for v1 simplicity.
