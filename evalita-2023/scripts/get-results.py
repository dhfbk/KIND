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

# labels = set()
# labels.update(gold_labels)
# labels.update(pred_labels)

# conversionMap = {}
# conversionMap[blankNer] = 0
# sortedLabels = ["O"]
# i = 0
# for l in labels:
#     if l != blankNer:
#         i += 1
#         conversionMap[l] = i
#         sortedLabels.append(l)

gold_nums = [conversionMap[v] for v in gold_labels]
pred_nums = [conversionMap[v] for v in pred_labels]

print(classification_report(gold_nums, pred_nums, target_names=sortedLabels, zero_division=0))
exit()

# print(sortedLabels)
# cm = confusion_matrix(gold_nums, pred_nums)
# print(cm)

# for k in conversionMap:
#     if k == blankNer:
#         continue
#     print(k)
#     print(precision_recall_fscore_support(gold_nums, pred_nums, average="micro", labels=[conversionMap[k]]))
