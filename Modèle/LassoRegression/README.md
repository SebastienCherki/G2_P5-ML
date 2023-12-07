# Analyse des Performances du Modèle Lasso Regression

## Résultats du Modèle Lasso Regression

### Matrice de Confusion

|               | Prédit Pas de Fraude | Prédit Fraude |
| ------------- | -------------------- | ------------- |
| **Réel Pas de Fraude** | 1270901 | 0 |
| **Réel Fraude** | 1505 | 118 |

### Rapport de Classification

|                | Précision | Recall | F1-Score | Support |
| -------------- | --------- | ------ | -------- | ------- |
| **Pas de Fraude**   | 1.00      | 1.00   | 1.00     | 1270901 |
| **Fraude**         | 1.00      | 0.07   | 0.14     | 1623    |

### AUC

L'Aire sous la courbe ROC (AUC) est de 0.96, indiquant une capacité de discrimination solide du modèle.

### Interprétation

Le modèle Lasso Regression présente une précision parfaite de 1.00, indiquant une fiabilité totale lorsqu'il prédit une fraude. Cependant, son rappel est très bas à 0.07, suggérant qu'il manque la grande majorité des transactions frauduleuses.

### Implications Pratiques

- Les performances élevées en termes de précision suggèrent que le modèle est très fiable pour identifier les transactions non frauduleuses.
- Cependant, le rappel très bas indique que le modèle manque la grande majorité des transactions frauduleuses.
- Il peut être nécessaire d'explorer d'autres modèles ou d'ajuster les hyperparamètres pour améliorer la capacité du modèle à détecter les fraudes.

![Matrice de Confusion.](https://github.com/SebastienCherki/G2_P5-ML/blob/main/Mod%C3%A8le/LassoRegression/Matrice%20de%20Confusion.png)
![Courbe ROC](https://github.com/SebastienCherki/G2_P5-ML/blob/main/Mod%C3%A8le/LassoRegression/ROC.png)
