import argparse

parser = argparse.ArgumentParser(
    prog='Evaluation script',
    description='This script evaluate the NER results.')
parser.add_argument('gold_file')
parser.add_argument('pred_file')
args = parser.parse_args()

import re
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import classification_report
import numpy as np

blankNer = "O"
prefixRe = re.compile(r"[A-Z]-")
pipeRe = re.compile(r"\|.*")

def loadLabels(fileName):
    labels = []
    with open(fileName, "r") as f:
        for line in f:
            line = line.strip()
            if len(line) == 0:
                continue
            parts = line.split("\t")
            if len(parts) != 2:
                print("ERROR!")
                continue
            label = parts[1].upper().strip()
            label = prefixRe.sub("", label)
            label = pipeRe.sub("", label)
            labels.append(label)
    return labels

gold_labels = loadLabels(args.gold_file)
pred_labels = loadLabels(args.pred_file)

conversionMap = {"O": 0, "PER": 1, "LOC": 2, "ORG": 3}
sortedLabels = ["O", "PER", "LOC", "ORG"]

gold_nums = [conversionMap[v] for v in gold_labels]
pred_nums = [conversionMap[v] for v in pred_labels]

okLabels = [1, 2, 3]
okLabelsDesc = ["PER", "LOC", "ORG"]
print(classification_report(gold_nums, pred_nums, labels=okLabels, target_names=okLabelsDesc, zero_division=0))

exit()

# These lines print the LaTeX code for the results
# Just comment the "exit" command to make it visible

micro = precision_recall_fscore_support(gold_nums, pred_nums, average='micro', labels=okLabels)[:3]
macro = precision_recall_fscore_support(gold_nums, pred_nums, average='macro', labels=okLabels)[:3]
results = precision_recall_fscore_support(gold_nums, pred_nums, average=None, labels=okLabels)
results = np.delete(results, len(results) - 1, axis=0)
results = np.transpose(results)

roundAcc = 2
tableLabels = {}
tableLabels["Micro"] = "%s & %s & %s" % (round(micro[0], roundAcc), round(micro[1], roundAcc), round(micro[2], roundAcc))
tableLabels["Macro"] = "%s & %s & %s" % (round(macro[0], roundAcc), round(macro[1], roundAcc), round(macro[2], roundAcc))
for i, l in enumerate(okLabels):
    tableLabels[l] = "%s & %s & %s" % (round(results[i][0], roundAcc), round(results[i][1], roundAcc), round(results[i][2], roundAcc))

print(tableLabels[1], "&", tableLabels[2], "&", tableLabels[3], "&", tableLabels["Micro"], "&", tableLabels["Macro"])

