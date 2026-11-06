---
name: recruiter-run-daily-vacancy-scan
description: "Run a recurring vacancy screening for primary and fallback role tiers and report only what is new, verified and eligible. Use when the user requests a daily or scheduled job scan in a job search or candidate recruitment workflow."
---

# Daily Vacancy Scan

## Operating contract
Use this skill independently or hand its structured result to the next relevant recruitment skill. Reuse existing candidate records; ask only for missing information material to this task. Do not require every skill in this set to run for a narrow request.
Keep candidate-specific data out of the skill itself. Use an authorized private record with source references and an updated-at timestamp. Treat missing information as unknown, not false. Distinguish facts, inferences and recommendations.
Discover available tools before relying on integrations. Read and use applicable document, calendar, messaging or storage guidance when that operation is needed. Never claim access, scheduling, sending or submission that tools have not confirmed. A skill provides instructions, not credentials, a background worker or platform permissions. If a tool, site or permission refuses an action, report it as blocked, say what the owner can do next, and do not route around the refusal.

## Inputs
Role tiers (primary targets and fallback targets), location, languages, hard constraints, permitted sources, the list of vacancies already reported, the source ledger, and where both are kept.

## Workflow
1. State the scope at the top of the report: tiers, location, languages, sources and the reading taken for anything ambiguous. In a scheduled or unattended run, do not stall on a question: take the most reasonable reading and say so. Stop only for a decision that cannot be undone.
2. Never create or open accounts, sign in for the candidate, handle passwords or CAPTCHAs, scrape LinkedIn or apply. Use public employer career pages, permitted feeds, authorized alert emails and listings the user supplies.
3. Read the source ledger (source, last reached, last blocked, reason, times blocked in a row). Search official employer career pages and sources that worked in recent runs first. Retry a source that has been blocked in several runs only occasionally, or when the owner supplies access. Never bypass a block.
4. Search each tier with recruiter-discover-verify-vacancies: original employer source, requisition ID, posting date, open status and checked-at time.
5. For each new vacancy, build the requirements record with recruiter-extract-vacancy-requirements, then run recruiter-check-posting-legitimacy. A doubtful or fraud-indicated listing goes under Not recommended with its reasons and is not ranked.
6. Gate each remaining vacancy with recruiter-screen-job-eligibility. A confirmed mandatory failure goes under Excluded with its reason; an unknown stays under Needs your answer; neither is hidden.
7. Compare with the already-reported list by job identity: employer plus requisition ID, otherwise normalized employer, title and location. The same role found on several boards is one job with every source listed. A repost under a new date with the same identity is not new; mark it reposted. Report only new jobs, plus status changes (closed, changed requirements or closing date) for ones reported earlier.
8. Order each tier with recruiter-prioritize-applications rules. Show the primary tier first and the fallback tier separately; do not draft applications or letters unless asked.
9. Record every source that could not be reached, with the reason, as blocked, and update the ledger. Never fill a gap with invented or aggregator-only listings. A run with no new vacancies is a valid result and is reported as such.
10. Update the already-reported list and the ledger with the run time. Keep both to vacancy and source data, with no candidate documents or credentials. If either cannot be stored, say it was not saved.

## Deliverable
Dated report: scope and assumptions; new verified vacancies per tier (canonical URL, all sources, status, checked-at, legitimacy result, gate result, next action); not recommended and excluded, each with reasons; needs your answer; blocked sources and ledger changes; changes to earlier vacancies; list and ledger update status.

## Completion check
No fabricated vacancy, URL or date; every listing carries its original source and checked-at time; no account created or used; no unchecked listing ranked; nothing sent or submitted; an empty or partial run is stated plainly.
