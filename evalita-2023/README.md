# Data for the NERMuD shared task (Evalita 2023)

This folder contains data to be used for the [NERMuD shared task](https://nermud.fbk.eu/) organized
at [Evalita 2023](https://www.evalita.it/campaigns/evalita-2023/).

The dataset contains the Wikinews, fiction, and De Gasperi subsets of [KIND](https://github.com/dhfbk/KIND), where test data is used for development.
The annotated test set for the task will be released after the evaluation window closes.

## Content of the dataset

| File                        |    Sentences |    Tokens |    LOC |    PER |    ORG |
|:----------------------------|-------------:|----------:|-------:|-------:|-------:|
| WN_train.tsv                |       10,912 |   249,077 |  6,862 |  8,928 |  7,593 |
| WN_dev.tsv                  |        2,594 |    59,220 |  1,711 |  1,802 |  1,823 |
| WN_test.tsv                 |        2,094 |    56,519 |  1,310 |  2,322 |  1,992 |
| FIC_train.tsv               |       11,423 |   170,942 |    733 |  3,439 |    182 |
| FIC_dev.tsv                 |        1,051 |    21,506 |    463 |    636 |    284 |
| FIC_test.tsv                |        1,516 |    27,190 |     37 |    443 |      1 |
| ADG_train.tsv               |        5,147 |   123,504 |  1,046 |  1,129 |  2,396 |
| ADG_dev.tsv                 |        1,122 |    27,128 |    274 |    253 |    533 |
| ADG_test.tsv                |          521 |    13,905 |    107 |    226 |    326 |

| Set                         |    Sentences |    Tokens |    LOC |    PER |    ORG |
|:----------------------------|-------------:|----------:|-------:|-------:|-------:|
| Total train                 |       27,482 |   543,523 |  8,641 | 13,496 | 10,171 |
| Total dev                   |        4,767 |   107,854 |  2,448 |  2,691 |  2,640 |
| Total test                  |        4,131 |    97,614 |  1,454 |  2,991 |  2,319 |
| Total                       |       36,380 |   748,991 | 12,543 | 19,178 | 15,130 |

