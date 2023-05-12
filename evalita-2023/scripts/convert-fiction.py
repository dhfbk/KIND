import argparse
import os
from utils import tintToWebAnno

parser = argparse.ArgumentParser(
    prog='Fiction converter',
    description='This script converts the fiction files to WebAnno TSV')
parser.add_argument('txt_folder')
parser.add_argument('out_folder')
parser.add_argument("--tint_url", help="Tint URL", type=str, default="http://dh-server.fbk.eu:8018/tint")
args = parser.parse_args()

files = os.listdir(args.txt_folder)
for f in files:
    if not f.endswith('.txt'):
        continue
    with open(os.path.join(args.txt_folder, f)) as fp:
        text = fp.read()
        tintToWebAnno(text, args.tint_url, os.path.join(args.out_folder, f + ".tsv"))
