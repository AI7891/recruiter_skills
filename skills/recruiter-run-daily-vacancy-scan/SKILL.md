---
name: recruiter-run-daily-vacancy-scan
description: "Run a recurring vacancy screening for primary and fallback role tiers and report only what is new, verified and eligible. Use when the user requests a daily or scheduled job scan in a job search or candidate recruitment workflow."
---

# Daily Vacancy Scan

## Operating contract
Use this skill independently or hand its structured result to the next relevant recruitment skill. Reuse existing candidate records; ask only for missing information material to this task. Do not require all sixteen skills to run for a narrow request.
Keep candidate-specific data out of the skill itself. Use an authorized private record with source references and an updated-at timestamp. Treat missing information as unknown, not false. Distinguish facts, inferences and recommendations.
Discover available tools before relying on integrations. Read and use applicable document, calendar, messaging or storage guidance when that operation is needed. Never claim access, scheduling, sending or submission that tools have not confirmed. A skill provides instructions, not credentials, a background worker or platform permissions. If a tool, site or permission refuses an action, report it as blocked, say what the owner can do next, and do not route around the refusal.

## Inputs
Role tiers (primary targets and fallback targets), location, languages, hard constraints, permitted sources, the list of vacancies already reported, and where that list is kept.

## Workflow
1. State the scope at the top of the report: tiers, location, languages, sources and the reading taken for anything ambiguous. In a scheduled or unattended run, do not stall on a question: take the most reasonable reading and say so. Stop only for a decision that cannot be undone.
2. Never create or open accounts, sign in for the candidate, handle passwords or CAPTCHAs, scrape LinkedIn or apply. Use public employer career pages, permitted feeds, authorized alert emails and listings the user supplies.
3. Search each tier with recruiter-discover-verify-vacancies: original employer source, requisition ID, posting date, open status and checked-at time.
4. Gate each new vacancy with recruiter-screen-job-eligibility. A confirmed mandatory failure goes under Excluded with its reason; an unknown stays under Needs your answer; neither is hidden.
5. Compare with the list of already reported vacancies by employer and requisition ID, otherwise normalized title and location. Report only new vacancies, plus status changes (closed, changed requirements) for ones reported earlier.
6. Order each tier with recruiter-prioritize-applications rules. Show the primary tier first and the fallback tier separately; do not draft applications or letters unless asked.
7. Record every source that could not be reached, with the reason, as blocked. Never fill a gap with invented or aggregator-only listings. A run with no new vacancies is a valid result and is reported as such.
8. Update the already-reported list with the run time and the vacancies found. Keep it to vacancy data and no candidate documents or credentials. If the list cannot be stored, say it was not saved.

## Deliverable
Dated report: scope and assumptions; new verified vacancies per tier (canonical URL, status, checked-at, gate result, next action); excluded with reasons; needs your answer; blocked sources; changes to earlier vacancies; list update status.

## Completion check
No fabricated vacancy, URL or date; every listing carries its original source and checked-at time; no account created or used; nothing sent or submitted; an empty or partial run is stated plainly.
