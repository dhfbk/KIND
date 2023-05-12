import argparse

parser = argparse.ArgumentParser(
    prog='Test extractor for Evalita 2023 NERMuD task',
    description='This script extracts data from Inception annotation')
parser.add_argument('input_folder')
parser.add_argument('output_folder')
parser.add_argument('dg_user')
parser.add_argument('wn_user')
parser.add_argument('fic_user')
args = parser.parse_args()

skipFiles = ["35994.tsv", "38378.tsv"]

import os
import re

fw_fic = open(os.path.join(args.output_folder, "FIC_test_nolabel.tsv"), "w")
fw_wn = open(os.path.join(args.output_folder, "WN_test_nolabel.tsv"), "w")
fw_adg = open(os.path.join(args.output_folder, "ADG_test_nolabel.tsv"), "w")

stats = {}
for label in ["WN", "FIC", "ADG"]:
	stats[label] = {"tokens": 0, "sentences": 0, "documents": 0}

inputFolder = os.path.join(args.input_folder, "annotation")
files = os.listdir(inputFolder)
for f in files:
	if f in skipFiles:
		continue

	buffer = None
	fileName = None
	label = None

	if f.startswith("dg"):
		buffer = fw_adg
		fileName = os.path.join(inputFolder, f, args.dg_user + ".tsv")
		label = "ADG"
	elif f.startswith("giordana"):
		buffer = fw_fic
		fileName = os.path.join(inputFolder, f, args.fic_user + ".tsv")
		label = "FIC"
	elif re.match(r"^[0-9].*", f):
		buffer = fw_wn
		fileName = os.path.join(inputFolder, f, args.wn_user + ".tsv")
		label = "WN"

	if label is None:
		print("Unknown file:", f)
		continue

	with open(fileName) as fo:
		stats[label]["documents"] += 1
		hasToken = False
		for line in fo:
			if line.startswith("#"):
				continue
			line = line.strip()
			if len(line) == 0:
				if hasToken:
					hasToken = False
					stats[label]["sentences"] += 1
					buffer.write("\n")
			else:
				hasToken = True
				parts = line.split("\t")
				token = parts[2]
				if token == "\\":
					token = ";"
				if label == "FIC" and re.match(r"[^-]+-[^-]+", token):
					token = token.replace("-", "")
				buffer.write(token)
				buffer.write("\n")
				stats[label]["tokens"] += 1

fw_fic.close()
fw_wn.close()
fw_adg.close()
print(stats)
