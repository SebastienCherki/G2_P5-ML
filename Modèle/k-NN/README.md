# Analyse des Performances du Modèle k-NN

## Résultats du Modèle k-NN

**Précision:** 0.88 | **Rappel:** 0.54 | **AUC:** 0.77

## Matrice de Confusion

|               | Prédit Pas de Fraude | Prédit Fraude |
| ------------- | -------------------- | ------------- |
| **Réel Pas de Fraude** | 1270786 | 115 |
| **Réel Fraude** | 739 | 884 |

## Rapport de Classification

|                | Précision | Recall | F1-Score | Support |
| -------------- | --------- | ------ | -------- | ------- |
| **Pas de Fraude**   | 1.00      | 1.00   | 1.00     | 1270901 |
| **Fraude**         | 0.88      | 0.54   | 0.67     | 1623    |

### Interprétation

Le modèle k-NN présente une précision de 0.88, indiquant une fiabilité d'environ 88% lorsqu'il prédit une fraude. Cependant, son rappel est relativement bas à 0.54, suggérant qu'il manque certaines fraudes.

L'AUC est de 0.77, considérée comme acceptable mais avec un potentiel d'amélioration.

### Matrice de Confusion

La matrice de confusion révèle un grand nombre de vrais négatifs (transactions non frauduleuses) correctement classées, mais quelques faux négatifs (fraudes manquées).

### Rapport de Classification

Le rapport de classification détaille davantage la performance du modèle, mettant en évidence une précision élevée mais un rappel relativement bas.

### Implications Pratiques

- Le modèle est efficace pour identifier les transactions non frauduleuses.
- Des améliorations peuvent être explorées pour capturer davantage de fraudes.
- Le choix entre précision et rappel dépend des coûts associés aux erreurs de classification.
- L'ajustement du seuil de classification peut optimiser la balance entre précision et rappel en fonction des besoins spécifiques.

![Matrice de Confusion.](https://github.com/SebastienCherki/G2_P5-ML/blob/main/Mod%C3%A8le/k-NN/Matrice%20de%20Confusion.png)
![Courbe ROC](https://github.com/SebastienCherki/G2_P5-ML/blob/main/Mod%C3%A8le/k-NN/ROC.png)
