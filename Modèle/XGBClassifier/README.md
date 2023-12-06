# Analyse des Performances du Modèle XGBClassifier

## Résultats du Modèle XGBClassifier

**Précision:** 0.96 | **Rappel:** 0.86 | **AUC:** 1.00

## Matrice de Confusion

|               | Prédit Pas de Fraude | Prédit Fraude |
| ------------- | -------------------- | ------------- |
| **Réel Pas de Fraude** | 1270847 | 54 |
| **Réel Fraude** | 225 | 1398 |

## Rapport de Classification

|                | Précision | Recall | F1-Score | Support |
| -------------- | --------- | ------ | -------- | ------- |
| **Pas de Fraude**   | 1.00      | 1.00   | 1.00     | 1270901 |
| **Fraude**         | 0.96      | 0.86   | 0.91     | 1623    |

### Interprétation

Le modèle XGBClassifier présente une précision de 0.96, indiquant une fiabilité d'environ 96% lorsqu'il prédit une fraude. Son rappel est élevé à 0.86, montrant une capacité à capturer environ 86% de toutes les transactions frauduleuses.

L'AUC est parfait à 1.00, indiquant une capacité de discrimination exceptionnelle du modèle.

### Matrice de Confusion

La matrice de confusion montre un nombre élevé de vrais négatifs (transactions non frauduleuses) correctement classées, et très peu de faux négatifs (fraudes manquées).

### Rapport de Classification

Le rapport de classification met en évidence une précision élevée et un rappel élevé, indiquant une performance exceptionnelle du modèle.

### Implications Pratiques

- Le modèle XGBClassifier est extrêmement fiable pour identifier les transactions non frauduleuses.
- Il capture une proportion élevée de transactions frauduleuses.
- Les performances exceptionnelles suggèrent une robustesse et une capacité de discrimination optimale du modèle.

![Matrice de Confusion.](https://github.com/SebastienCherki/G2_P5-ML/blob/main/Mod%C3%A8le/XGBClassifier/Matrice%20de%20Confusion.png)
![Courbe ROC](https://github.com/SebastienCherki/G2_P5-ML/blob/main/Mod%C3%A8le/XGBClassifier/ROC.png)
