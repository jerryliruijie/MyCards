# MyCards API

## Commands

```bash
pip install -e .[dev]
alembic upgrade head
python -m app.db.seed
uvicorn app.main:app --reload --port 8000
```

## Notes
- Auth is intentionally deferred in v1.
- Pricing adapters are behind `app/integrations/pricing`.
- Historical `PriceSnapshot` rows are append-only by design.
