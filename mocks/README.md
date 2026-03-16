# Mock Data Directory

This directory stores sample data, example responses, and temporary frontend placeholders used before real backend integration is complete.

## Purpose

- support frontend work before backend implementation is finished
- keep review data stable and repeatable
- expose contract problems early

## Recommended contents

- sample list responses
- sample detail responses
- empty state examples
- error response examples

## Collaboration Rules

- Mock field names should stay close to `docs/api-contracts`
- Mock data is transitional and should not replace the real contract long term
- Once an API is implemented, keep mocks as test samples rather than as the primary source of page logic
