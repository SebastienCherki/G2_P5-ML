# Analyse des Performances du Modèle KMeans

## Résultats du Modèle KMeans

### Rapport de Classification

|                | Précision | Recall | F1-Score | Support |
| -------------- | --------- | ------ | -------- | ------- |
| **Pas de Fraude**   | 1.00      | 0.93   | 0.96     | 1270901 |
| **Fraude**         | 0.00      | 0.01   | 0.00     | 1623    |

### Interprétation

Le modèle KMeans présente des performances limitées, avec une précision de 1.00 pour les transactions non frauduleuses, indiquant une fiabilité élevée lorsqu'il prédit qu'une transaction n'est pas une fraude. Cependant, le rappel est extrêmement bas à 0.01, montrant une capacité très limitée à capturer les transactions frauduleuses.

### Implications Pratiques

- Le modèle KMeans semble avoir du mal à détecter les transactions frauduleuses, comme indiqué par le rappel très bas.
- Ces résultats suggèrent que le modèle KMeans n'est probablement pas approprié pour cette tâche de détection de fraude.

![Matrice de Confusion.](https://github.com/SebastienCherki/G2_P5-ML/blob/main/Mod%C3%A8le/KMeans/Matrice%20de%20Confusion.png)
![Cluster](https://github.com/SebastienCherki/G2_P5-ML/blob/main/Mod%C3%A8le/KMeans/Cluster.png)
