# Frontend Spec Directory

This directory stores page-level specifications and acts as direct input for Gemini frontend work.

## Each page spec should include

- page goal
- primary user tasks
- information structure
- core components
- interaction rules
- loading, empty, and error states
- field sources
- related Figma link

## Recommended file names

- `dashboard.md`
- `card-list.md`
- `card-detail.md`
- `card-form.md`
- `storage-manager.md`

## Suggested template

```md
# Page Name

## Page Goal

## Primary User Tasks

## Information Structure

## Component Breakdown

## Interaction Rules

## State Design
- Loading state
- Empty state
- Error state

## Field Sources
- API:
- Mock:

## Figma

## Notes
```

## Collaboration Rules

- Do not start implementation before the page spec is clear enough
- If the page changes significantly, update this directory before changing code
- Keep this directory focused on UX structure and behavior, not backend implementation detail
