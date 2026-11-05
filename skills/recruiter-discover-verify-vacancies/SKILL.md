---
name: recruiter-discover-verify-vacancies
description: "Find live job openings and verify freshness, authenticity and duplicates for defined candidate targets. Use when the user requests vacancy discovery and verification in a job search or candidate recruitment workflow."
---

# Vacancy Discovery and Verification

## Operating contract
Use this skill independently or hand its structured result to the next relevant recruitment skill. Reuse existing candidate records; ask only for missing information material to this task. Do not require all sixteen skills to run for a narrow request.
Keep candidate-specific data out of the skill itself. Use an authorized private record with source references and an updated-at timestamp. Treat missing information as unknown, not false. Distinguish facts, inferences and recommendations.
Discover available tools before relying on integrations. Read and use applicable document, calendar, messaging or storage guidance when that operation is needed. Never claim access, scheduling, sending or submission that tools have not confirmed. A skill provides instructions, not credentials, a background worker or platform permissions. If a tool, site or permission refuses an action, report it as blocked, say what the owner can do next, and do not route around the refusal.

## Inputs
Target roles, locations, constraints and permitted search sources.

## Workflow
1. Search employer career sites and permitted feeds; use relevant languages and role synonyms.
2. Capture original employer URL, requisition ID, title, location, posting date when available and checked-at time.
3. Verify open status on the original source; label inaccessible or unconfirmed listings instead of calling them live.
4. Deduplicate by employer and requisition ID, otherwise normalized title/location; flag conflicting remote claims or suspicious payment requests.
5. Respect source access restrictions; do not bypass sign-in, CAPTCHA or scrape LinkedIn. Use user-supplied vacancies or authorized alert emails when needed.
6. When a page cannot be fetched or needs a permission, record the lead as unverified (fetch blocked) with the reason, and ask the owner for the link, the page text or the permission. Do not replace the original source with an aggregator or cached copy to look complete.
7. For a recurring search, use recruiter-run-daily-vacancy-scan.

## Deliverable
Verified vacancy table with canonical URLs, source dates, status, duplicate grouping and uncertainty.

## Completion check
No fabricated vacancies or dates; syndicated timestamps do not establish original freshness; every unverified lead says why.
