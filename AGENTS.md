# AGENTS.md

## Project philosophy
- Lightweight
- Personal-use first
- Easy to maintain
- Fast iteration
- Avoid over-engineering

## Architecture
- Web-first development
- Backend API and database are the long-term foundation
- Pricing integrations must use provider adapters
- Preserve historical price snapshots
- Keep manual price entry supported

## Workflow
- Create meaningful commits after each completed feature or milestone
- Use clear commit messages
- Do not create noisy micro-commits
- Do not squash commits when merging into master
- Preserve readable development history

## Frontend
- Before major UI implementation, show a wireframe/mockup/spec for review
- Prioritize usability and clean information-dense layout
- Avoid flashy but impractical UI

## Anti-goals
- No marketplace
- No social feed
- No heavy enterprise auth in v1
- No unnecessary complexity
