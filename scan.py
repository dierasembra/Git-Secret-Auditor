import os, re, json, regex

def load_patterns(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def scan_file(path, patterns):
    results = []
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            for i, line in enumerate(f, start=1):
                for name, pat in patterns.items():
                    if regex.search(pat, line):
                        results.append({'file': path, 'line': i, 'match_name': name, 'match': line.strip()[:200]})
    except Exception:
        pass
    return results

def scan_tree(root, patterns, exts=None):
    findings = []
    for dirpath, dirs, files in os.walk(root):
        # skip .git by default
        if '.git' in dirpath.split(os.sep):
            continue
        for fn in files:
            if exts and not any(fn.endswith(e) for e in exts):
                continue
            path = os.path.join(dirpath, fn)
            findings.extend(scan_file(path, patterns))
    return findings
