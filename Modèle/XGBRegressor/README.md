# Analyse des Performances du Modèle XGBRegressor

## Résultats du Modèle XGBRegressor

**Précision:** 0.94 | **Rappel:** 0.68 | **AUC:** 0.99

## Matrice de Confusion

|               | Prédit Pas de Fraude | Prédit Fraude |
| ------------- | -------------------- | ------------- |
| **Réel Pas de Fraude** | 1270830 | 71 |
| **Réel Fraude** | 513 | 1110 |

## Rapport de Classification

|                | Précision | Recall | F1-Score | Support |
| -------------- | --------- | ------ | -------- | ------- |
| **Pas de Fraude**   | 1.00      | 1.00   | 1.00     | 1270901 |
| **Fraude**         | 0.94      | 0.68   | 0.79     | 1623    |

### Interprétation

Le modèle XGBRegressor présente une précision de 0.94, indiquant une fiabilité d'environ 94% lorsqu'il prédit une fraude. Son rappel est de 0.68, montrant une capacité à capturer environ 68% de toutes les transactions frauduleuses.

L'AUC est exceptionnellement élevée à 0.99, indiquant une excellente capacité de discrimination du modèle.

### Matrice de Confusion

La matrice de confusion montre un nombre élevé de vrais négatifs (transactions non frauduleuses) correctement classées, et relativement peu de faux négatifs (fraudes manquées).

### Rapport de Classification

Le rapport de classification met en évidence une précision élevée et un rappel raisonnable, indiquant une performance globale solide.

### Implications Pratiques

- Le modèle XGBRegressor est très fiable pour identifier les transactions non frauduleuses.
- Il capture une proportion significative de transactions frauduleuses.
- Les performances élevées suggèrent une robustesse du modèle pour cette tâche spécifique.

![Matrice de Confusion.](https://github.com/SebastienCherki/G2_P5-ML/blob/main/Mod%C3%A8le/XGBRegressor/Matrice%20de%20Confusion.png)
![Courbe ROC](https://github.com/SebastienCherki/G2_P5-ML/blob/main/Mod%C3%A8le/XGBRegressor/ROC.png)
