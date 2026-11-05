# Security policy

## What to report

- **Malicious or unsafe instructions** inside a skill: text that tells an agent to exfiltrate data, read credentials, run unexpected commands, contact unlisted URLs, or bypass user authorization.
- **Accidental sensitive-data exposure** in this repository: real candidate records, CVs, contact details, tokens, passwords or private documents.
- Weaknesses in the validator or CI workflow that let unreviewed content reach `Dev`.

## How to report privately

Do not open a public issue or pull request that contains the details.

1. Use GitHub's private vulnerability reporting: open the **Security** tab of this repository and choose **Report a vulnerability** (`https://github.com/AI7891/recruiter_skills/security/advisories/new`).
2. If that button is not available, the feature has not been enabled yet. Open a public issue that says only "Security report: please provide a private contact channel". Do not include the issue details, the data, or any secret. The maintainer will arrange a private channel.

There is no maintainer email address published here, and none should be guessed.

If you exposed a credential, revoke or rotate it at the provider first, then report. Removing it from the latest commit does not remove it from history.

## What to expect

This is a small project maintained by one person. Reports are handled on a best-effort basis; there is no guaranteed response time. Confirmed issues are fixed in a new commit and, where relevant, a new release. Published releases are never rewritten.

## Scope and limits

The skills are natural-language instructions. Automated checks in this repository verify structure only; they cannot prove that instructions are safe. Prompt-level safeguards supplement, and do not replace, the permissions and sandboxing of the agent client you run them in. Disable external write tools when testing with untrusted vacancy text.
