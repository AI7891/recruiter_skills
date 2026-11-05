---
name: recruiter-diagnose-job-search-funnel
description: "Analyze job-search outcomes and identify evidence-backed improvements to targeting, applications and interviews. Use when the user requests funnel diagnosis and improvement in a job search or candidate recruitment workflow."
---

# Funnel Diagnosis and Improvement

## Operating contract
Use this skill independently or hand its structured result to the next relevant recruitment skill. Reuse existing candidate records; ask only for missing information material to this task. Do not require all sixteen skills to run for a narrow request.
Keep candidate-specific data out of the skill itself. Use an authorized private record with source references and an updated-at timestamp. Treat missing information as unknown, not false. Distinguish facts, inferences and recommendations.
Discover available tools before relying on integrations. Read and use applicable document, calendar, messaging or storage guidance when that operation is needed. Never claim access, scheduling, sending or submission that tools have not confirmed. A skill provides instructions, not credentials, a background worker or platform permissions. If a tool, site or permission refuses an action, report it as blocked, say what the owner can do next, and do not route around the refusal.

## Inputs
Dated application events, role families, sources, outcomes and candidate time where recorded.

## Workflow
1. Deduplicate applications and distinguish pending from completed outcomes; choose comparable date cohorts.
2. Calculate stage conversions with explicit numerators, denominators and observation windows. Treat offers per hour only when time records exist.
3. Segment by role, channel or application variant only when sample size supports a useful comparison.
4. Separate descriptive association from causation; show small samples and avoid treating recent pending applications as failures.
5. Identify the most plausible bottleneck and propose one measurable change with an evaluation window; use scripts for nontrivial calculations.

## Deliverable
Funnel table (counts, conversion, cohort age); limitations; prioritized hypothesis and experiment.

## Completion check
Zero denominators display unavailable; no fabricated benchmarks or causal claims from tiny samples.
