import argparse
import os
import re
import json
import random
from utils import tintToWebAnno

parser = argparse.ArgumentParser(
    prog='De Gasperi converter',
    description='This script converts the De Gasperi dataset from JSON to TSV')
parser.add_argument('json_folder')
parser.add_argument('out_folder')
parser.add_argument('--num', type=int, default=15)
parser.add_argument('--min_len', type=int, default=3000)
parser.add_argument('--max_len', type=int, default=8000)
parser.add_argument('--dg_folders', nargs='+')
parser.add_argument("--tint_url", help="Tint URL", type=str, default="http://dh-server.fbk.eu:8018/tint")
args = parser.parse_args()

filesRe = re.compile(r'([IV]+)\.html\.xml\.([0-9]+)\.txt\.tsv')
namesRe = re.compile(r'([IV]+)\.html_doc_number_([0-9]+)')

stats = {}
stats['toSkip'] = 0
stats['skipped'] = 0
stats['skipped_for_len'] = 0
stats['total'] = 0
stats['included'] = 0

skipFiles = set()
if args.dg_folders:
    for f in args.dg_folders:
        files = os.listdir(f)
        for fileName in files:
            m = filesRe.match(fileName)
            if m:
                skipFiles.add("%s.%s" % (m.group(1), m.group(2)))
stats['toSkip'] = len(skipFiles)

texts = {}
files = os.listdir(args.json_folder)
for f in files:
    if not f.endswith('.json'):
        continue
    fileName = os.path.join(args.json_folder, f)
    with open(fileName) as fo:
        content = json.load(fo)
        for fj in content['xml']['file']:
            url = fj['head']['url']
            m = namesRe.match(url)
            if m:
                thisID = "%s.%s" % (m.group(1), m.group(2))
                stats['total'] += 1
                if thisID in skipFiles:
                    stats['skipped'] += 1
                    continue
                content = ""
                if "content" in fj:
                    if type(fj['content']) is dict:
                        content = fj["content"]["original_text"]
                    else:
                        content = fj["content"]
                else:
                    if "original_text" in fj:
                        content = fj['original_text']

                if len(content) < args.min_len or len(content) > args.max_len:
                    stats['skipped_for_len'] += 1
                    continue

                stats['included'] += 1
                texts[thisID] = fj['head']['title'] + "\n" + content

if not os.path.exists(args.out_folder):
    os.makedirs(args.out_folder)

k = list(texts.keys())
extracted = random.sample(k, args.num)
for e in extracted:
    text = texts[e]
    tintToWebAnno(text, args.tint_url, os.path.join(args.out_folder, e + ".tsv"))

print(stats)
