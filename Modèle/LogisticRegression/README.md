# Analyse des Performances du Modèle LogisticRegression

## Résultats du Modèle LogisticRegression

**Précision:** 0.78 | **Rappel:** 0.44 | **AUC:** 0.72

## Matrice de Confusion

|               | Prédit Pas de Fraude | Prédit Fraude |
| ------------- | -------------------- | ------------- |
| **Réel Pas de Fraude** | 1270700 | 201 |
| **Réel Fraude** | 911 | 712 |

## Rapport de Classification

|                | Précision | Recall | F1-Score | Support |
| -------------- | --------- | ------ | -------- | ------- |
| **Pas de Fraude**   | 1.00      | 1.00   | 1.00     | 1270901 |
| **Fraude**         | 0.78      | 0.44   | 0.56     | 1623    |

### Interprétation

Le modèle LogisticRegression présente une précision de 0.78, indiquant une fiabilité d'environ 78% lorsqu'il prédit une fraude. Son rappel est de 0.44, montrant une capacité à capturer environ 44% de toutes les transactions frauduleuses.

L'AUC est de 0.72, indiquant une capacité de discrimination acceptable du modèle.

### Matrice de Confusion

La matrice de confusion montre un nombre élevé de vrais négatifs (transactions non frauduleuses) correctement classées, mais un nombre relativement élevé de faux négatifs (fraudes manquées).

### Rapport de Classification

Le rapport de classification met en évidence une précision modérée et un rappel relativement bas, indiquant une performance moyenne du modèle.

### Implications Pratiques

- Le modèle LogisticRegression est efficace pour identifier les transactions non frauduleuses.
- Cependant, il manque une proportion significative de transactions frauduleuses en raison du rappel relativement bas.
- Les performances globales du modèle peuvent bénéficier d'améliorations pour une détection plus exhaustive des fraudes.

![Matrice de Confusion.](https://github.com/SebastienCherki/G2_P5-ML/blob/main/Mod%C3%A8le/LogisticRegression/Matrice%20de%20Confusion.png)
![Courbe ROC](https://github.com/SebastienCherki/G2_P5-ML/blob/main/Mod%C3%A8le/LogisticRegression/ROC.png)
