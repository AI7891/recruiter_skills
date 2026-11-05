---
name: recruiter-execute-track-applications
description: "Complete authorized job applications and maintain a deduplicated application record. Use when the user requests application execution and tracking in a job search or candidate recruitment workflow."
---

# Application Execution and Tracking

## Operating contract
Use this skill independently or hand its structured result to the next relevant recruitment skill. Reuse existing candidate records; ask only for missing information material to this task. Do not require all sixteen skills to run for a narrow request.
Keep candidate-specific data out of the skill itself. Use an authorized private record with source references and an updated-at timestamp. Treat missing information as unknown, not false. Distinguish facts, inferences and recommendations.
Discover available tools before relying on integrations. Read and use applicable document, calendar, messaging or storage guidance when that operation is needed. Never claim access, scheduling, sending or submission that tools have not confirmed. A skill provides instructions, not credentials, a background worker or platform permissions. If a tool, site or permission refuses an action, report it as blocked, say what the owner can do next, and do not route around the refusal.

## Inputs
Approved application materials, vacancy identity, required answers and submission authorization.

## Workflow
1. Check the tracker for an existing application using employer plus requisition ID.
2. Verify the live destination and record the exact document versions and field answers.
3. Complete supported forms within authorization; stop only for consequential unknowns, required declarations or unsupported access.
4. Never guess identity, authorization, salary, disability or demographic responses; let the candidate control optional sensitive answers.
5. On submission record confirmation and timestamp. If a timeout creates uncertainty, check receipts before retrying; never claim submission from a clicked button alone.

## Deliverable
Application record (job ID, employer, URL, versions, status, timestamp, confirmation, next action); unresolved fields.

## Completion check
Use draft, ready, submitted, submission-unknown, rejected, interview, offer, withdrawn or closed statuses accurately; do not bypass CAPTCHA.
