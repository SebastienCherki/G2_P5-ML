# Analyse des Performances du Modèle GradientBoostingRegressor

## Résultats du Modèle GradientBoostingRegressor

### Rapport de Classification

|                | Précision | Recall | F1-Score | Support |
| -------------- | --------- | ------ | -------- | ------- |
| **Pas de Fraude**   | 1.00      | 0.15   | 0.26     | 1270901 |
| **Fraude**         | 0.00      | 0.81   | 0.00     | 1623    |

### Interprétation

Le modèle GradientBoostingRegressor présente des performances limitées, avec une précision de 1.00 pour les transactions non frauduleuses, indiquant une fiabilité élevée lorsqu'il prédit qu'une transaction n'est pas une fraude. Cependant, le rappel est extrêmement bas à 0.15, montrant une capacité très limitée à capturer les transactions frauduleuses.

### Implications Pratiques

- Le modèle GradientBoostingRegressor semble avoir du mal à détecter les transactions frauduleuses, comme indiqué par le rappel très bas.
- Ces résultats suggèrent que le modèle GradientBoostingRegressor n'est probablement pas approprié pour cette tâche de détection de fraude.

