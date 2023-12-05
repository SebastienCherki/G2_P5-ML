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
Le modèle présente une **précision de 0.98**, indiquant une fiabilité exceptionnelle d'environ 98% lorsqu'il prédit une fraude.

### Rappel:
Avec un **rappel de 0.79**, le modèle réussit à **capturer environ 79%** de toutes les transactions frauduleuses.

### Aire sous la courbe ROC (AUC):
L'**AUC atteint 0.89**, démontrant une capacité solide du modèle à discriminer entre les classes.

### Matrice de Confusion:
La matrice révèle un grand nombre de **vrais négatifs (transactions non frauduleuses)** correctement classées, avec seulement quelques **faux négatifs (fraudes manquées)**.

### Rapport de Classification:
Le rapport détaille davantage la performance du modèle, mettant en évidence une **précision exceptionnellement élevée** et un **rappel solide**.

## Interprétation:

Le modèle RandomForestClassifier démontre une **excellente précision**, assurant une fiabilité exceptionnelle lorsqu'il prédit une fraude. Son **rappel solide** indique une capacité notable à capturer la majorité des fraudes. L'**AUC élevé** confirme la capacité du modèle à discriminer entre les classes.

## Implications Pratiques:

- Le modèle est **extrêmement fiable pour identifier les transactions non frauduleuses**.
- Son **rappel élevé** suggère une capacité robuste à **capturer la plupart des fraudes**.
- Ces résultats peuvent indiquer une meilleure performance par rapport au modèle k-NN.
- L'ajustement du **seuil de classification** peut toujours être exploré pour optimiser la balance entre précision et rappel.

