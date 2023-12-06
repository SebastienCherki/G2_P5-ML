# Analyse des Performances du Modèle LinearRegression

## Résultats du Modèle LinearRegression

### Matrice de Confusion

|               | Prédit Pas de Fraude | Prédit Fraude |
| ------------- | -------------------- | ------------- |
| **Réel Pas de Fraude** | 1270901 | 0 |
| **Réel Fraude** | 1478 | 145 |

### Rapport de Classification

|                | Précision | Recall | F1-Score | Support |
| -------------- | --------- | ------ | -------- | ------- |
| **Pas de Fraude**   | 1.00      | 1.00   | 1.00     | 1270901 |
| **Fraude**         | 1.00      | 0.09   | 0.16     | 1623    |

### AUC

L'Aire sous la courbe ROC (AUC) est de 0.93, indiquant une capacité de discrimination solide du modèle.

### Interprétation

Le modèle LinearRegression présente une précision parfaite de 1.00, indiquant une fiabilité totale lorsqu'il prédit une fraude. Cependant, son rappel est extrêmement bas à 0.09, suggérant qu'il manque la grande majorité des transactions frauduleuses.

### Implications Pratiques

- Les performances élevées en termes de précision suggèrent que le modèle est très fiable pour identifier les transactions non frauduleuses.
- Cependant, le rappel très bas indique que le modèle manque la grande majorité des transactions frauduleuses.
- L'utilisation de la Linear Regression pour la classification peut ne pas être appropriée pour cette tâche spécifique.
  
![Matrice de Confusion.](https://github.com/SebastienCherki/G2_P5-ML/blob/main/Mod%C3%A8le/LinearRegression/Matrice%20de%20Confusion.png)
![Courbe ROC](https://github.com/SebastienCherki/G2_P5-ML/blob/main/Mod%C3%A8le/LinearRegression/ROC.png)
