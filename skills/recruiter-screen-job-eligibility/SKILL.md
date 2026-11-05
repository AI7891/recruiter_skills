---
name: recruiter-screen-job-eligibility
description: "Screen vacancies for work authorization, mandatory credentials, location, language and availability requirements. Use when the user requests job eligibility screening in a job search or candidate recruitment workflow."
---

# Job Eligibility Screening

## Operating contract
Use this skill independently or hand its structured result to the next relevant recruitment skill. Reuse existing candidate records; ask only for missing information material to this task. Do not require all sixteen skills to run for a narrow request.
Keep candidate-specific data out of the skill itself. Use an authorized private record with source references and an updated-at timestamp. Treat missing information as unknown, not false. Distinguish facts, inferences and recommendations.
Discover available tools before relying on integrations. Read and use applicable document, calendar, messaging or storage guidance when that operation is needed. Never claim access, scheduling, sending or submission that tools have not confirmed. A skill provides instructions, not credentials, a background worker or platform permissions. If a tool, site or permission refuses an action, report it as blocked, say what the owner can do next, and do not route around the refusal.

## Inputs
Current vacancy, candidate constraints and explicitly provided eligibility facts.

## Workflow
1. Extract exact mandatory wording and distinguish preferences.
2. Classify each gate as pass, fail or unknown using evidence; unknown is never an automatic rejection.
3. Check current official jurisdiction sources for legal or licensing requirements; distinguish law from employer preference and cite dates.
4. Explain blockers and permitted clarification routes; do not infer nationality or authorization from name or residence.

## Deliverable
Gate table (requirement, source, candidate evidence, status); eligible, blocked or needs clarification decision.

## Completion check
Legal claims use current authoritative sources; only confirmed hard failures block progression.
