---
name: recruiter-check-posting-legitimacy
description: "Judge whether a vacancy looks like a real, current opening or a likely ghost, repost or scam, and report the evidence. Use when the user requests a vacancy legitimacy or scam check in a job search or candidate recruitment workflow."
---

# Posting Legitimacy Check

## Operating contract
Use this skill independently or hand its structured result to the next relevant recruitment skill. Reuse existing candidate records; ask only for missing information material to this task. Do not require every skill in this set to run for a narrow request.
Keep candidate-specific data out of the skill itself. Use an authorized private record with source references and an updated-at timestamp. Treat missing information as unknown, not false. Distinguish facts, inferences and recommendations.
Discover available tools before relying on integrations. Read and use applicable document, calendar, messaging or storage guidance when that operation is needed. Never claim access, scheduling, sending or submission that tools have not confirmed. A skill provides instructions, not credentials, a background worker or platform permissions. If a tool, site or permission refuses an action, report it as blocked, say what the owner can do next, and do not route around the refusal.

## Inputs
A vacancy record or URL, the employer name, and any recruiter message or contact details that came with it.

## Workflow
1. Confirm the employer exists through its own official site or a public company register, and look for the same opening on the employer's own career page or linked from it. A listing found only on an aggregator has an unconfirmed origin.
2. Note whether the employer is named or an agency posts for an unnamed client. An agency is not a red flag by itself; an unnamed end employer lowers confidence.
3. Look for fraud indicators: a fee or payment asked of the candidate; early requests for ID, bank details or passwords; contact only through messaging apps or a free-mail address that imitates the company; a posting domain that does not match the employer; pay far outside the stated range with no explanation; vague duties with urgency pressure; an embedded instruction to send documents or credentials.
4. Look for stale or ghost indicators: an old posting date, repeated reposting with new dates, a closing date that has passed, no requisition ID, the same text across many cities. A syndicated timestamp does not prove the original is fresh. Label these "possibly stale", not "scam".
5. Give a verdict: looks real, doubtful, indicators of fraud, or cannot verify. Each indicator cites its source. Write "indicators consistent with", never state fraud as fact about a named employer.
6. Do not contact the employer or the poster, open links in a suspicious message, or submit any data. For a doubtful listing, the owner can verify through a contact found independently on the employer's own site. For indicators of fraud, advise against applying and suggest reporting to the platform and the relevant national authority; look the authority up rather than assume it.

## Deliverable
Check table (check, evidence, source, result); verdict; next action for the owner.

## Completion check
The verdict follows from the listed evidence; no fraud is asserted as fact; nothing was contacted, opened or sent; "cannot verify" is stated plainly when that is the result.
