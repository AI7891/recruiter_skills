---
name: recruiter-prioritize-applications
description: "Rank a shortlist of jobs by evidence-backed fit, candidate preferences and preparation effort. Use when the user requests application prioritization in a job search or candidate recruitment workflow."
---

# Application Prioritization

## Operating contract
Use this skill independently or hand its structured result to the next relevant recruitment skill. Reuse existing candidate records; ask only for missing information material to this task. Do not require every skill in this set to run for a narrow request.
Keep candidate-specific data out of the skill itself. Use an authorized private record with source references and an updated-at timestamp. Treat missing information as unknown, not false. Distinguish facts, inferences and recommendations.
Discover available tools before relying on integrations. Read and use applicable document, calendar, messaging or storage guidance when that operation is needed. Never claim access, scheduling, sending or submission that tools have not confirmed. A skill provides instructions, not credentials, a background worker or platform permissions. If a tool, site or permission refuses an action, report it as blocked, say what the owner can do next, and do not route around the refusal.

## Inputs
Verified vacancies, eligibility decisions, fit matrices and candidate time budget.

## Workflow
1. Remove confirmed blockers and closed listings; keep uncertain cases in a clarification queue. A mandatory requirement that a stated candidate fact contradicts (for example a required Dutch C1 against a recorded Dutch A2) is a confirmed blocker even when no eligibility decision was supplied: list it as removed with the requirement and the fact. A missing or unknown fact is never a blocker.
2. Rank remaining opportunities by relevant evidence, preference alignment, verified freshness and effort.
3. Use transparent ordinal ratings by default; if numeric weights are useful, disclose assumptions and label the result a priority score, never a probability.
4. Do not invent applicant counts, referral strength or employer responsiveness.
5. Allocate the available work budget to the highest-value applications and explain meaningful tradeoffs.
6. When vacancies are unverified, label the ranking provisional: it is a preparation order, not an instruction to submit. A vacancy whose legitimacy check came back doubtful or fraud-indicated is not ranked; list it separately with the reason.

## Deliverable
Ordered shortlist (priority, evidence, uncertainty, estimated effort, next action); clarification queue.

## Completion check
Ranking is reproducible from visible inputs and respects candidate hard constraints; removed items are listed with their reason; no unverified vacancy is presented as ready to apply.
