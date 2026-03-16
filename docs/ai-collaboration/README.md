# AI Collaboration Guide

This document set defines the working boundary between `Gemini for frontend` and `Codex for backend` so different agents do not repeatedly overwrite the same layer of the project.

## Goals

- Enable parallel frontend and backend work
- Keep directory ownership explicit
- Standardize handoff format
- Reduce rework and style drift

## Documents

- `gemini-frontend-workflow.md`: workflow and boundaries for Gemini frontend work
- `gemini-prompt-template.md`: reusable prompt templates for Gemini

## Default Ownership

- Gemini:
  - page structure
  - component decomposition
  - styles and interaction behavior
  - frontend implementation with mock data
- Codex:
  - data model
  - API routes and schemas
  - business services and repositories
  - provider adapters
  - backend integration and contract alignment

## Required Rules

- Gemini should not modify `apps/api` by default
- Codex should not lead visual page design by default
- All frontend requests should be written in `docs/frontend-specs` first
- All API contracts should be written in `docs/api-contracts` first
- Page-level integration should use `mocks` before real backend data is ready

## Recommended Sequence

1. Define page goals, fields, interactions, and Figma links in `docs/frontend-specs`
2. Define request and response contracts in `docs/api-contracts`
3. Let Gemini build the frontend using the page spec and mock data
4. Let Codex implement backend behavior against the contract
5. During integration, fix contract and data issues instead of restarting the page design
