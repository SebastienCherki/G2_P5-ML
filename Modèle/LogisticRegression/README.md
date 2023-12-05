```
Précision: 0.78
Rappel: 0.44
Aire sous la courbe ROC (AUC): 0.72
Matrice de Confusion:
[[1270700     201]
 [    911     712]]
Rapport de Classification :
               precision    recall  f1-score   support

           0       1.00      1.00      1.00   1270901
           1       0.78      0.44      0.56      1623

    accuracy                           1.00   1272524
   macro avg       0.89      0.72      0.78   1272524
weighted avg       1.00      1.00      1.00   1272524
```
![Matrice de Confusion.](https://github.com/SebastienCherki/G2_P5-ML/blob/main/LogisticRegression/Matrice%20de%20Confusion.png)
![Courbe ROC](https://github.com/SebastienCherki/G2_P5-ML/blob/main/LogisticRegression/ROC.png)

# Évaluation des Performances du Modèle LogisticRegression

Le modèle LogisticRegression a été évalué pour sa capacité à **détecter la fraude** dans les transactions. Les résultats obtenus sont les suivants :

### Précision:
Le modèle présente une **précision de 0.78**, indiquant une fiabilité d'environ 78% lorsqu'il prédit une fraude.

### Rappel:
Avec un **rappel de 0.44**, le modèle réussit à **capturer environ 44%** de toutes les transactions frauduleuses.

### Aire sous la courbe ROC (AUC):
L'**AUC atteint 0.72**, indiquant une capacité modérée du modèle à discriminer entre les classes.

### Matrice de Confusion:
La matrice révèle un grand nombre de **vrais négatifs (transactions non frauduleuses)** correctement classées, mais avec des **faux négatifs (fraudes manquées)** et des **faux positifs (fraudes incorrectement identifiées)**.

### Rapport de Classification:
Le rapport détaille davantage la performance du modèle, mettant en évidence une **précision acceptable** mais un **rappel relativement bas**.

## Interprétation:

Le modèle LogisticRegression présente une **précision acceptable**, indiquant une fiabilité acceptable lorsqu'il prédit une fraude. Cependant, son **rappel relativement bas** suggère que le modèle manque une partie significative des fraudes. L'**AUC modéré** indique une capacité moyenne du modèle à discriminer entre les classes.

## Implications Pratiques:

- Le modèle est **raisonnablement fiable pour identifier les transactions non frauduleuses**.
- Des **améliorations peuvent être envisagées** pour renforcer la détection des fraudes.
- L'ajustement du **seuil de classification** peut être exploré pour optimiser la balance entre précision et rappel.
