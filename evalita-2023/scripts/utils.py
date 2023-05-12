from webanno_tsv import Document, Annotation
from dataclasses import replace
import requests
import json

def tintToWebAnno(text, tint_url, outFile, allowedTags={"PER", "LOC", "ORG", "O"}, neutralTag="O", span="custom.Span", field="label"):
    layer_defs = [(span, [field])]

    myobj = {'text' : text}
    x = requests.post(tint_url, data = myobj)
    data = json.loads(x.text)

    sentences = []
    rawAnnotations = []
    tokenID = 0
    previousNER = "O"
    nerStartID = 0
    for sentence in data['sentences']:
        tokens = []
        ners = []
        for token in sentence['tokens']:
            ner = token['ner']
            if ner not in allowedTags:
                ner = neutralTag
            if (not token['isMultiwordToken']) or token['isMultiwordFirstToken']:
                tokens.append(token['originalText'].replace(" ", "_"))
                if ner != neutralTag and previousNER == neutralTag:
                    nerStartID = tokenID
                if ner != neutralTag and previousNER != neutralTag and previousNER != ner:
                    rawAnnotations.append((nerStartID, tokenID, span, field, previousNER))
                    nerStartID = tokenID
                if ner == neutralTag and previousNER != neutralTag:
                    rawAnnotations.append((nerStartID, tokenID, span, field, previousNER))
                tokenID += 1
                previousNER = ner
        sentences.append(tokens)

    doc = Document.from_token_lists(sentences)

    annotations = []
    for a in rawAnnotations:
        ann = Annotation(tokens=doc.tokens[a[0]:a[1]], layer=a[2], field=a[3], label=a[4])
        annotations.append(ann)

    doc = replace(doc, annotations=annotations, layer_defs=layer_defs)
    tsvString = doc.tsv()

    with open(outFile, "w") as fw:
        fw.write(tsvString)
