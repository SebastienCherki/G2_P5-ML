# Analyse des Performances du Modèle LGBMRegressor

## Résultats du Modèle LGBMRegressor

**Mean Squared Error (MSE):** 0.00 | **R-squared (R2):** 0.67 | **Précision:** 0.98 | **Rappel:** 0.69 | **AUC:** 0.99

### Matrice de Confusion

|               | Prédit Pas de Fraude | Prédit Fraude |
| ------------- | -------------------- | ------------- |
| **Réel Pas de Fraude** | 1270882 | 19 |
| **Réel Fraude** | 500 | 1123 |

### Rapport de Classification

|                | Précision | Recall | F1-Score | Support |
| -------------- | --------- | ------ | -------- | ------- |
| **Pas de Fraude**   | 1.00      | 1.00   | 1.00     | 1270901 |
| **Fraude**         | 0.98      | 0.69   | 0.81     | 1623    |

### Interprétation

Le modèle LGBMRegressor présente des performances globales solides, avec un MSE de 0.00 et un R2 de 0.67, indiquant une bonne capacité du modèle à expliquer la variance des données. La précision est élevée à 0.98, suggérant une fiabilité élevée lorsqu'il prédit une fraude.

Le rappel est de 0.69, montrant une capacité à capturer environ 69% de toutes les transactions frauduleuses.

L'AUC est de 0.99, indiquant une excellente capacité de discrimination du modèle.

### Implications Pratiques

- Le modèle LGBMRegressor présente une fiabilité élevée pour identifier les transactions non frauduleuses.
- Il capture une proportion significative de transactions frauduleuses avec une précision élevée.
- Les performances globales du modèle sont solides, mais des ajustements peuvent être explorés pour améliorer le rappel si nécessaire.

![Matrice de Confusion.](https://github.com/SebastienCherki/G2_P5-ML/blob/main/Mod%C3%A8le/LGBMRegressor/Matrice%20de%20Confusion.png)
![Courbe ROC](https://github.com/SebastienCherki/G2_P5-ML/blob/main/Mod%C3%A8le/LGBMRegressor/ROC.png)
