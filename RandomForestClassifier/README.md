```
Précision: 0.98
Rappel: 0.79
Aire sous la courbe ROC (AUC): 0.89
Matrice de Confusion:
[[1270881      20]
 [    348    1275]]
Rapport de Classification :
               precision    recall  f1-score   support

           0       1.00      1.00      1.00   1270901
           1       0.98      0.79      0.87      1623

    accuracy                           1.00   1272524
   macro avg       0.99      0.89      0.94   1272524
weighted avg       1.00      1.00      1.00   1272524
```
![Matrice de Confusion.](https://github.com/SebastienCherki/G2_P5-ML/blob/main/RandomForestClassifier/Matrice%20de%20Confusion.png)
![Courbe ROC](https://github.com/SebastienCherki/G2_P5-ML/blob/main/RandomForestClassifier/ROC.png)

# Évaluation des Performances du Modèle RandomForestClassifier

Le modèle RandomForestClassifier a été évalué pour sa capacité à **détecter la fraude** dans les transactions. Les résultats obtenus sont les suivants :

### Précision:
Le modèle présente une **précision de 0.92**, indiquant une fiabilité d'environ 92% lorsqu'il prédit une fraude.

### Rappel:
Avec un **rappel de 0.68**, le modèle réussit à **capturer environ 68%** de toutes les transactions frauduleuses.

### Aire sous la courbe ROC (AUC):
L'**AUC atteint 0.85**, démontrant une capacité de discrimination élevée.

### Interprétation:

Le modèle RandomForestClassifier démontre une **excellente précision** et une capacité **solide à capturer les fraudes**. Son **rappel équilibré** et son **AUC élevé** soulignent son efficacité dans la détection de la fraude.

## Implications Pratiques:

- Le modèle est **très efficace pour identifier les transactions non frauduleuses**.
- Sa capacité à **capturer davantage de fraudes** en fait un choix potentiellement favorable dans certaines situations.
- Le choix entre **précision et rappel** reste important en fonction des coûts associés aux erreurs de classification.
- L'ajustement du **seuil de classification** peut toujours être exploré pour optimiser la balance entre précision et rappel.
