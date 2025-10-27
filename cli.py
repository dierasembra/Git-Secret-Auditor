import argparse, json, os
from .scan import load_patterns, scan_tree
from .history_scan import scan_history

def main():
    parser = argparse.ArgumentParser(prog='gsa')
    parser.add_argument('scan', nargs='?')
    parser.add_argument('--path', default='.', help='Path to repo')
    parser.add_argument('--out', default='gsa_report.json', help='Output file')
    parser.add_argument('--history', type=int, help='Scan last N commits of history')
    parser.add_argument('--ext', action='append', help='Only scan files with these extensions (e.g. --ext .py)')

    args = parser.parse_args()
    patterns = load_patterns(os.path.join(os.path.dirname(__file__), 'patterns.json'))
    report = {'tree_findings': [], 'history_findings': []}
    report['tree_findings'] = scan_tree(args.path, patterns, exts=args.ext)
    if args.history:
        report['history_findings'] = scan_history(args.path, patterns, max_commits=args.history)
    with open(args.out, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print('Report written to', args.out)

if __name__ == '__main__':
    main()
