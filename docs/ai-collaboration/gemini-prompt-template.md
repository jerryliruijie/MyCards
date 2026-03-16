# Gemini Prompt Templates

Use these templates to keep Gemini focused on frontend work that fits this repository.

## Page Implementation Template

```md
You are responsible only for frontend implementation in this repository. Do not design backend APIs, database schema, deployment, or infrastructure changes.

Project context:
- Product: MyCards
- Stack: Next.js + TypeScript + Tailwind CSS
- Goal: a personal collectible card management app focused on usability, information density, and maintainability

Your boundaries:
- Only modify `apps/web`, `docs/frontend-specs`, and `mocks`
- Do not modify `apps/api`, `infra`, or database-related code
- Do not add heavy UI frameworks or complex state management

You must read these inputs first:
- `docs/frontend-specs/<page-doc>.md`
- `docs/api-contracts/<contract-doc>.md`
- `mocks/<mock-file-or-doc>`

Task:
- Page or component: <name>
- Figma: <link or none>
- Goal: <one-sentence description>

Implementation requirements:
- Reuse the existing directory structure and components where possible
- Keep component structure clear and maintainable
- Route API calls through `apps/web/lib`
- If backend support is not ready, use mock data but preserve a clean path to real API integration
- Do not rename fields defined by the backend contract

When you finish, report:
- which files changed
- which fields the UI depends on
- which parts still use mock data
- whether backend support is still missing for any interaction
```

## Page Review Template

```md
Review this page only from a frontend perspective. Do not implement backend changes.

Check for:
- clarity of information hierarchy
- suitability for frequent use
- quality of component decomposition
- maintainability of the styling approach
- readiness for real API integration

Inputs:
- Page spec: `docs/frontend-specs/<page-doc>.md`
- Figma: <link or none>
- Current implementation files: <file list>

Return:
- key problems
- suggested changes
- whether the page is ready for implementation or integration
```
