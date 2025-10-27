# Git Secret Auditor

Git Secret Auditor is a lightweight security tool that scans a Git repository (working tree or history) to detect potential leaked secrets such as API keys, passwords, tokens, and private keys. It's built for maintainers and security engineers to quickly find and remediate accidental leaks before or after commits.

This repository is ready for GitHub Sponsors — includes CLI, sample repo, CI workflow, and report output.

## Features
- Scan current files (working tree) for common secret patterns (API keys, AWS keys, private keys, passwords)
- Optionally scan Git history (recent commits) for secrets
- Generate a JSON and human-readable report with filename, line number, match, and severity
- Configurable patterns in `gsa/patterns.json`
- GitHub Action example to run on PRs

## Install
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage
Scan working directory:
```bash
python -m gsa.cli scan --path path/to/repo --out report.json
```

Scan Git history (last N commits):
```bash
python -m gsa.cli scan --path path/to/repo --history 50 --out history_report.json
```

## Remediation tips
- Rotate any leaked keys immediately.
- Force-remove secrets from Git history using `git filter-repo` or `git filter-branch`.
- Add patterns to `.gitignore` and use pre-commit hooks to block future leaks.

## Sponsor
If this tool helps you catch leaks earlier, please consider sponsoring the project on GitHub Sponsors ❤️

## License
MIT
