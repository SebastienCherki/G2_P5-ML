# Analyse des Performances du Modèle TreeClassifier

## Résultats du Modèle TreeClassifier

### Matrice de Confusion

|               | Prédit Pas de Fraude | Prédit Fraude |
| ------------- | -------------------- | ------------- |
| **Réel Pas de Fraude** | 1270689 | 212 |
| **Réel Fraude** | 211 | 1412 |

## Rapport de Classification

|                | Précision | Recall | F1-Score | Support |
| -------------- | --------- | ------ | -------- | ------- |
| **Pas de Fraude**   | 1.00      | 1.00   | 1.00     | 1270901 |
| **Fraude**         | 0.87      | 0.87   | 0.87     | 1623    |

### AUC

L'Aire sous la courbe ROC (AUC) est de 0.93, indiquant une capacité de discrimination solide du modèle.

### Interprétation

Le modèle TreeClassifier présente une précision élevée de 0.87, indiquant une fiabilité d'environ 87% lorsqu'il prédit une fraude. Son rappel est également élevé à 0.87, montrant une capacité à capturer environ 87% de toutes les transactions frauduleuses.

### Implications Pratiques

- Le modèle TreeClassifier est très fiable pour identifier les transactions non frauduleuses.
- Il capture une proportion élevée de transactions frauduleuses.
- Les performances élevées suggèrent une robustesse du modèle pour cette tâche spécifique.

![Matrice de Confusion.](https://github.com/SebastienCherki/G2_P5-ML/blob/main/Mod%C3%A8le/TreeClassifier/Matrice%20de%20Confusion.png)
![Courbe ROC](https://github.com/SebastienCherki/G2_P5-ML/blob/main/Mod%C3%A8le/TreeClassifier/ROC.png)
