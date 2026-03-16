# API Contract Directory

This directory stores shared contracts for frontend and backend work. Codex uses it to implement backend behavior, and Gemini uses it to integrate real data without guessing field shapes.

## Each contract should include

- business purpose
- request path and method
- path and query parameters
- request body
- response body
- field definitions
- error cases
- mock examples

## Recommended file names

- `cards-list.md`
- `card-detail.md`
- `card-create.md`
- `portfolio-summary.md`
- `storage-tree.md`

## Suggested template

```md
# Contract Name

## Business Purpose

## Request
- Method:
- Path:

## Params

## Body

## Response

## Field Definitions

## Error Cases

## Mock Example
```

## Collaboration Rules

- Once a field name is documented here, frontend code should not rename it casually
- During integration, fix mismatches against this directory instead of relying on chat-only agreements
- If backend behavior changes, update this directory before or with the code change
