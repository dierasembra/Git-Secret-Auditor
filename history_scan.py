from git import Repo
import os, regex, json

def scan_history(repo_path, patterns, max_commits=100):
    repo = Repo(repo_path)
    findings = []
    for i, commit in enumerate(repo.iter_commits('HEAD', max_count=max_commits)):
        for diff in commit.stats.files.keys():
            try:
                blob = commit.tree / diff
                content = blob.data_stream.read().decode('utf-8', errors='ignore').splitlines()
                for lineno, line in enumerate(content, start=1):
                    for name, pat in patterns.items():
                        if regex.search(pat, line):
                            findings.append({'commit': commit.hexsha, 'file': diff, 'line': lineno, 'match_name': name, 'match': line.strip()[:200]})
            except Exception:
                continue
    return findings
