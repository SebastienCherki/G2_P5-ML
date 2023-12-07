# Analyse des Performances du Modèle LGBMClassifier

## Résultats du Modèle LGBMClassifier

**Précision:** 0.09 | **Rappel:** 0.18 | **AUC:** 0.42

### Matrice de Confusion

|               | Prédit Pas de Fraude | Prédit Fraude |
| ------------- | -------------------- | ------------- |
| **Réel Pas de Fraude** | 1267966 | 2935 |
| **Réel Fraude** | 1330 | 293 |

### Rapport de Classification

|                | Précision | Recall | F1-Score | Support |
| -------------- | --------- | ------ | -------- | ------- |
| **Pas de Fraude**   | 1.00      | 1.00   | 1.00     | 1270901 |
| **Fraude**         | 0.09      | 0.18   | 0.12     | 1623    |

### Interprétation

Le modèle LGBMClassifier présente des performances relativement faibles, avec une précision de 0.09, indiquant une fiabilité limitée lorsqu'il prédit une fraude. Le rappel est de 0.18, montrant une capacité à capturer seulement 18% de toutes les transactions frauduleuses.

L'AUC est de 0.42, indiquant une capacité de discrimination limitée du modèle.

### Implications Pratiques

- Le modèle LGBMClassifier présente des performances limitées pour détecter les transactions frauduleuses.
- La précision est très basse, indiquant un grand nombre de faux positifs.
- Des ajustements significatifs, y compris l'optimisation des paramètres, peuvent être nécessaires pour améliorer les performances du modèle.

![Matrice de Confusion.](https://github.com/SebastienCherki/G2_P5-ML/blob/main/Mod%C3%A8le/LGBMClassifier/Matrice%20de%20Confusion.png)
![Courbe ROC](https://github.com/SebastienCherki/G2_P5-ML/blob/main/Mod%C3%A8le/LGBMClassifier/ROC.png)
