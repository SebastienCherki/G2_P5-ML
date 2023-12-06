# Analyse des Performances du Modèle MLPClassifier

## Résultats du Modèle MLPClassifier

**Précision:** 1.00 | **Rappel:** 0.01 | **AUC:** 0.51

## Matrice de Confusion

|               | Prédit Pas de Fraude | Prédit Fraude |
| ------------- | -------------------- | ------------- |
| **Réel Pas de Fraude** | 1270901 | 0 |
| **Réel Fraude** | 1599 | 24 |

## Rapport de Classification

|                | Précision | Recall | F1-Score | Support |
| -------------- | --------- | ------ | -------- | ------- |
| **Pas de Fraude**   | 1.00      | 1.00   | 1.00     | 1270901 |
| **Fraude**         | 1.00      | 0.01   | 0.03     | 1623    |

### Interprétation

Le modèle MLPClassifier présente une précision parfaite de 1.00, indiquant une fiabilité totale lorsqu'il prédit une fraude. Cependant, son rappel est extrêmement bas à 0.01, suggérant qu'il manque la grande majorité des transactions frauduleuses.

L'AUC est de 0.51, indiquant une capacité de discrimination très faible du modèle.

### Matrice de Confusion

La matrice de confusion montre un nombre élevé de vrais négatifs (transactions non frauduleuses) correctement classées, mais un nombre très élevé de faux négatifs (fraudes manquées).

### Rapport de Classification

Le rapport de classification met en évidence une précision parfaite mais un rappel extrêmement bas, indiquant une performance limitée du modèle pour détecter les fraudes.

### Implications Pratiques

- Le modèle MLPClassifier est très fiable pour identifier les transactions non frauduleuses.
- Cependant, il manque la grande majorité des transactions frauduleuses en raison du rappel très bas.
- Les performances globales du modèle pour la détection de fraudes nécessitent des améliorations.

![Matrice de Confusion.](https://github.com/SebastienCherki/G2_P5-ML/blob/main/Mod%C3%A8le/MLPClassifier/Matrice%20de%20Confusion.png)
![Courbe ROC](https://github.com/SebastienCherki/G2_P5-ML/blob/main/Mod%C3%A8le/MLPClassifier/ROC.png)
