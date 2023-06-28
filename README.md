# KIND (Kessler Italian Named-entities Dataset)

KIND is an Italian dataset for Named-Entity Recognition.

It contains more than one million tokens with the annotation covering three classes: person, location, and organization.
Most of the dataset (around 600K tokens) contains manual gold annotations in three different domains: news, literature, and political discourses.

For the construction of the dataset, we decide to use texts publicly available, under a license that permits both research and commercial use.

In particular we release four chapters with texts taken from: (i) Wikinews (WN) as a source of news texts belonging to the last decades; (ii) some Italian fiction books (FIC) in the public domain; (iii) writings and speeches from Italian politicians Aldo Moro (AM) and (iv) Alcide De Gasperi (ADG).

### Wikinews

Wikinews is a multi-language free-content project of collaborative journalism.
The Italian chapter contains [more than 11,000 news articles](https://it.wikinews.org/wiki/Speciale:Statistiche), released under the [Creative Commons Attribution 2.5 License](https://creativecommons.org/licenses/by/2.5/).

In building KIND, we randomly choose 1,000 articles evenly distributed in the last 20 years, for a total of 308,622 tokens.

### Literature

Regarding fiction literature, we annotate 86 book chapters taken from 10 books written by Italian authors, who all died more than 70 years ago, for a total of 192,448 tokens.
The plain texts are taken from the [Liber Liber website](https://www.liberliber.it/).

In particular, we choose: Il giorno delle Mésules (Ettore Castiglioni, 1993, 12,853 tokens), L'amante di Cesare (Augusto De Angelis, 1936, 13,464 tokens), Canne al vento (Grazia Deledda, 1913, 13,945 tokens), 1861-1911 - Cinquant’anni di vita nazionale ricordati ai fanciulli (Guido Fabiani, 1911, 10,801 tokens), Lettere dal carcere (Antonio Gramsci, 1947, 10,655), Anarchismo e democrazia (Errico Malatesta, 1974, 11,557 tokens), L'amore negato (Maria Messina, 1928, 31,115 tokens), La luna e i falò (Cesare Pavese, 1950, 10,705 tokens), La coscienza di Zeno (Italo Svevo, 1923, 56,364 tokens), Le cose piu grandi di lui (Luciano Zuccoli, 1922, 20,989 tokens).

In selecting works in the public domain, we favored texts as recent as possible, so that the model trained on this data can be used efficiently on novels written in the last years, since the language used in these novels is more likely to be similar to the language used in the novels of our days. 

### Aldo Moro's Works

Writings belonging to Aldo Moro have recently been collected by the University of Bologna and published on a platform called [Edizione Nazionale delle Opere di Aldo Moro](https://aldomorodigitale.unibo.it/).

The project is still ongoing and, by now, it contains 806 documents for a total of about one million tokens.

In the first release of KIND, we include 392,604 tokens from the Aldo Moro's works dataset, with silver annotations (see the reference below).

### Alcide De Gasperi's Writings

Finally, we annotate 158 document (150,632 tokens) from [Alcide Digitale](https://alcidedigitale.fbk.eu/), spanning 50 years of European history.

The complete corpus contains a comprehensive collection of Alcide De Gasperi’s public documents, 2,762 in total, written or transcribed between 1901 and 1954.

## Publications

This page refers to the dataset presented in the paper:

KIND: an Italian Multi-Domain Dataset for Named Entity Recognition. Teresa Paccosi and Alessio Palmero Aprosio, Proceedings of the 13th Conference on Language Resources and Evaluation 2022 (LREC 2022) [[arXiv](https://arxiv.org/abs/2112.15099)]

BibTeX:

```
@inproceedings{lrec2022kind,
    title = "{KIND}: an {I}talian Multi-Domain Dataset for Named Entity Recognition",
    author = "Paccosi, Teresa and Palmero Aprosio, Alessio",
    booktitle = "Proceedings of the Thirteenth Language Resources and Evaluation Conference",
    year = "2022",
    address = "Marseille, France",
    publisher = "European Language Resources Association",
    pages = "501--507"
}
```

Some [additional data](evalita-2023) has been annotated and made available for the [EVALITA 2023](https://www.evalita.it/campaigns/evalita-2023/) task. In case you use this dataset, you may cite:

NERMuD at EVALITA 2023: Overview of the Named-Entities Recognition on Multi-Domain Documents Task. Alessio Palmero Aprosio and Teresa Paccosi, Proceedings of the Eighth Evaluation Campaign of Natural Language Processing and Speech Tools for Italian. Final Workshop (EVALITA 2023)

BibTeX:

```
@inproceedings{evalita2023nermud,
    title={{NERMuD} at {EVALITA} 2023: Overview of the Named-Entities Recognition on Multi-Domain Documents Task},
    author={Palmero Aprosio, Alessio and Paccosi, Teresa},
    booktitle={Proceedings of the Eighth Evaluation Campaign of Natural Language Processing and Speech Tools for Italian. Final Workshop (EVALITA 2023)},
    publisher = {CEUR.org},
    year = {2023},
    month = {September},
    address = {Parma, Italy}
}
```

## License

The NER annotations in (i), (ii), and (iii) are released under the [Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) license](https://creativecommons.org/licenses/by-nc/4.0/).
Annotation from Alcide De Gasperi's writings are released under the [Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) license](https://creativecommons.org/licenses/by-nc-sa/4.0/).
