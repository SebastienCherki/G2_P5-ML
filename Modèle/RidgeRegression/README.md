# Analyse des Performances du Modèle RidgeRegression

## Résultats du Modèle RidgeRegression

### Matrice de Confusion

|               | Prédit Pas de Fraude | Prédit Fraude |
| ------------- | -------------------- | ------------- |
| **Réel Pas de Fraude** | 1270901 | 0 |
| **Réel Fraude** | 1478 | 145 |

## Rapport de Classification

|                | Précision | Recall | F1-Score | Support |
| -------------- | --------- | ------ | -------- | ------- |
| **Pas de Fraude**   | 1.00      | 1.00   | 1.00     | 1270901 |
| **Fraude**         | 1.00      | 0.09   | 0.16     | 1623    |

### AUC

L'Aire sous la courbe ROC (AUC) est de 0.93, indiquant une capacité de discrimination solide du modèle.

### Interprétation

Le modèle RidgeRegression présente une précision élevée de 1.00, indiquant une fiabilité parfaite lorsqu'il prédit une fraude. Cependant, son rappel est très bas à 0.09, suggérant qu'il manque la plupart des transactions frauduleuses.

### Implications Pratiques

- Le modèle RidgeRegression est très fiable pour identifier les transactions non frauduleuses.
- Cependant, il manque la plupart des transactions frauduleuses en raison du rappel très bas.
- Les performances globales du modèle pour la détection de fraudes peuvent nécessiter des améliorations.

![Matrice de Confusion.](https://github.com/SebastienCherki/G2_P5-ML/blob/main/Mod%C3%A8le/RidgeRegression/Matrice%20de%20Confusion.png)
![Courbe ROC](https://github.com/SebastienCherki/G2_P5-ML/blob/main/Mod%C3%A8le/RidgeRegression/ROC.png)
