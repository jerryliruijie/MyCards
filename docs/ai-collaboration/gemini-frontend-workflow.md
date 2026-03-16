# Gemini Frontend Workflow

## Scope

This file defines how Gemini should work inside this repository so frontend output can be integrated into the real project rather than becoming an isolated demo.

## Allowed Paths

- `apps/web/app`
- `apps/web/components`
- `apps/web/lib`
- `apps/web/types`
- `docs/frontend-specs`
- `mocks`

## Restricted Paths

- `apps/api`
- `infra`
- database migration files
- pricing provider adapters
- scripts related to deployment, database setup, or background jobs

If a change needs to cross these boundaries, document it in `docs/api-contracts` first.

## Required Input Sources

Before Gemini starts implementation, it must read these sources in order:

1. The matching page spec in `docs/frontend-specs`
2. The matching API contract in `docs/api-contracts`
3. The matching mock data in `mocks`
4. The Figma link or node reference if design input exists

If any of these are missing, create the missing documentation first instead of jumping straight into code.

## Output Requirements

- Reuse the existing Next.js structure whenever possible
- Keep component names clear and files focused
- Route API calls through `apps/web/lib`
- Do not hardcode backend URLs inside pages or components
- Reuse types from `apps/web/types` whenever possible
- A page should remain previewable with mock data before the real backend is connected

## Handoff Format

When Gemini delivers frontend work, it should always state:

- which pages or components changed
- which API fields are required
- which parts still depend on mock data
- which interactions still need backend support

## Do Not

- do not redesign the whole product language without approval
- do not add heavy state management unless the repo already uses it
- do not introduce large UI frameworks without approval
- do not rename API fields at the page layer
- do not mix demo data directly into the real API client implementation

## Recommended Collaboration Loop

1. Finalize the page spec
2. Let Gemini implement the page and components
3. Let Codex define or refine the API contract
4. Let Codex implement backend behavior and real data integration
5. Limit frontend follow-up work to integration fixes instead of redoing the design
