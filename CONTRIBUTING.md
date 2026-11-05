# Contributing

Thanks for helping improve these skills. This project ships instructions that agents follow, so review is stricter than for ordinary documentation.

## Never commit

- Real candidate records, CVs, contact details, interview notes or offer documents. Use clearly synthetic examples.
- Secrets of any kind: passwords, tokens, API keys, session cookies, private keys.

If you committed one by mistake, do not just delete it: follow [SECURITY.md](SECURITY.md).

## Pull request process

1. Fork or branch from the latest `Dev` and open a pull request targeting `Dev`.
2. Keep each PR focused and describe the behavior change in plain language.
3. All checks must pass, in particular **Validate skills**.
4. The maintainer reviews the full diff before merge. Do not request merges that bypass checks.

## Required validation

Run locally before opening a PR (Python 3.10+):

```
python3 -m pip install --require-hashes -r tools/requirements.txt
python3 -I -m unittest discover -s tests -v
python3 -I tools/validate_skills.py .
```

The validator enforces the seventeen expected skill directories, valid and unique names matching folder names, nonempty descriptions, required files, safe YAML, no symlinks, executable files, traversal paths, unexpected binaries or unapproved files under `skills/`, size limits, and flags credential-like text (without printing it).

Each skill keeps the same `## Operating contract` section. If you change it, change it in all seventeen `SKILL.md` files; the validator rejects drift. Skills are installed one directory at a time, so each must stay self-contained and must not reference files outside its own directory.

## Instruction review expectations

Structural checks cannot tell whether natural-language instructions are safe. Reviewers read every changed instruction line and look specifically for:

- new URLs, shell commands or scripts;
- requests for credentials, tokens or personal data;
- transfers of data to external destinations;
- instructions that weaken authorization, confirmation or untrusted-content handling;
- claims of guarantees (for example employment outcomes or platform access).

Explain in the PR why any such change is needed.

## Adding or removing a skill

The set is fixed at seventeen skills. Changing the set means updating `EXPECTED_SKILLS` in `tools/validate_skills.py`, the README and the tests in the same PR, and needs explicit maintainer agreement.

## Code owners and review

`.github/CODEOWNERS` assigns the maintainer to `skills/` and `.github/`. Whether that is enforced depends on the `Dev` branch ruleset. An author cannot independently review their own PR, so until a second reviewer exists the pull request and passing-check requirements are the main gate.

## License

By contributing you agree that your contribution is licensed under the [MIT License](LICENSE).
