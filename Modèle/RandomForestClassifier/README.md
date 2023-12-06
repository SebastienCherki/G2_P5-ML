# Analyse des Performances du Modèle RandomForestClassifier

## Résultats du Modèle RandomForestClassifier

**Précision:** 0.98 | **Rappel:** 0.79 | **AUC:** 0.89

## Matrice de Confusion

|               | Prédit Pas de Fraude | Prédit Fraude |
| ------------- | -------------------- | ------------- |
| **Réel Pas de Fraude** | 1270881 | 20 |
| **Réel Fraude** | 348 | 1275 |

## Rapport de Classification

|                | Précision | Recall | F1-Score | Support |
| -------------- | --------- | ------ | -------- | ------- |
| **Pas de Fraude**   | 1.00      | 1.00   | 1.00     | 1270901 |
| **Fraude**         | 0.98      | 0.79   | 0.87     | 1623    |

### Interprétation

Le modèle RandomForestClassifier présente une précision élevée de 0.98, indiquant une fiabilité d'environ 98% lorsqu'il prédit une fraude. Son rappel est de 0.79, montrant une capacité à capturer environ 79% de toutes les transactions frauduleuses.

L'AUC est de 0.89, indiquant une bonne capacité de discrimination du modèle.

### Matrice de Confusion

La matrice de confusion montre un nombre élevé de vrais négatifs (transactions non frauduleuses) correctement classées, et relativement peu de faux négatifs (fraudes manquées).

### Rapport de Classification

Le rapport de classification met en évidence une précision élevée et un rappel raisonnable, indiquant une performance globale solide.

### Implications Pratiques

- Le modèle RandomForestClassifier est très fiable pour identifier les transactions non frauduleuses.
- Il capture une proportion significative de transactions frauduleuses.
- Les performances élevées suggèrent une robustesse du modèle pour cette tâche spécifique.

![Matrice de Confusion.](https://github.com/SebastienCherki/G2_P5-ML/blob/main/Mod%C3%A8le/RandomForestClassifier/Matrice%20de%20Confusion.png)
![Courbe ROC](https://github.com/SebastienCherki/G2_P5-ML/blob/main/Mod%C3%A8le/RandomForestClassifier/ROC.png)
