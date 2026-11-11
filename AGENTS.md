# Project development rules

## Scope
- These rules apply to the entire CyberLab project, including frontend,
  backend, laboratory environments, and infrastructure configuration.
- Follow the existing project conventions unless a change is justified.

## Project context
- CyberLab is an educational cybersecurity platform using React,
  TypeScript, FastAPI, PostgreSQL, and Docker.
- Vulnerable behavior belongs exclusively in isolated laboratory
  environments, never in the platform itself.
- Read README.md and relevant existing code before proposing changes.
- Do not invent requirements. Ask for clarification when ambiguity
  materially affects functionality, architecture, or security.

## Collaboration
- Do not execute commands or modify files unless explicitly authorized.
- By default, provide code and instructions for the user to apply.
- Explain the purpose of changes and work in small, reviewable steps.
- If required context is unavailable under the current authorization,
  ask the user to provide the relevant files or command output.

## Modular architecture
- Maintain a modular structure with clear responsibilities and boundaries.
- Keep business logic separate from API handlers, UI components,
  database access, and infrastructure operations.
- Keep modules focused and avoid circular dependencies.
- Avoid unnecessary abstractions and premature generalization.

## Code reuse and redundancy
- Inspect existing code before implementing new functionality.
- Reuse or extend suitable existing implementations instead of duplicating them.
- Check that reused code is correct and appropriate for the new use case.
- Extract shared logic when repetition represents the same responsibility.
- Do not force unrelated behavior into a shared abstraction.
- Remove code made obsolete by a change.

## Tests
- Add or update tests for new behavior and bug fixes.
- Test observable behavior rather than internal implementation details.
- Cover normal behavior, relevant edge cases, and expected failures.
- Add regression tests for fixed bugs where practical.
- Use integration tests when correctness depends on interactions between
  the database, API, or container management.
- Keep tests isolated, repeatable, and independent of execution order.
- When command execution is authorized, run relevant tests before
  considering a change complete.
- Otherwise, provide the test commands for the user to run and request
  the results. Mark validation as pending until results are available.
- Report which tests were run and any checks that remain unverified.

## Concurrency and race conditions
- Review operations that access shared state for potential race conditions.
- Pay particular attention to concurrent requests, database updates,
  lab creation, resource allocation, session expiration, and cleanup.
- Prefer atomic operations, database constraints, and transactions
  where they provide the required guarantees.
- Do not rely solely on in-process locks when multiple workers or
  application instances may access the same state.
- Make retried or repeated operations idempotent where appropriate.
- Handle partial failures and avoid leaking containers or allocated resources.
- Add concurrency tests for identified risks where practical.
- Document remaining concurrency assumptions and limitations.

## Security
- Never commit secrets or include them in logs, examples, or test fixtures.
- Validate external input and enforce authorization on protected resources.
- Enforce ownership checks for lab sessions, findings, and reports.
- Allow cross-user access only through explicitly defined and authorized roles.
- Treat lab containers and their output as untrusted.
- Never expose the Docker socket or host-sensitive directories to labs.
- Apply explicit resource limits, network isolation, and expiration to labs.
- Do not disable security controls to make an implementation work.

## Dependencies and database changes
- Prefer existing project dependencies when they meet the requirement.
- Explain the need before introducing a new dependency.
- Verify library-specific guidance against current official documentation.
- Record dependency changes in the project's dependency files.
- Use versioned migrations for database schema changes.
- Identify destructive changes and obtain explicit approval before
  applying them.

## Completion criteria
- Confirm that changes preserve module boundaries and reuse suitable code.
- Check for unnecessary duplication and obsolete code.
- Review relevant failure paths and concurrency risks.
- Update affected tests and documentation.
- Do not claim that tests passed or that race conditions are absent
  without supporting verification.
- Clearly distinguish implemented changes from proposed changes,
  and verified behavior from assumptions.