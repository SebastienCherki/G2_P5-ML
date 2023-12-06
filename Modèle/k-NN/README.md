```
Précision: 0.88
Rappel: 0.54
Aire sous la courbe ROC (AUC): 0.77
Matrice de Confusion:
[[1270786     115]
 [    739     884]]
Rapport de Classification :
               precision    recall  f1-score   support

           0       1.00      1.00      1.00   1270901
           1       0.88      0.54      0.67      1623

    accuracy                           1.00   1272524
   macro avg       0.94      0.77      0.84   1272524
weighted avg       1.00      1.00      1.00   1272524
```
![Matrice de Confusion.](https://github.com/SebastienCherki/G2_P5-ML/blob/main/Mod%C3%A8le/k-NN/Matrice%20de%20Confusion.png)
![Courbe ROC](https://github.com/SebastienCherki/G2_P5-ML/blob/main/Mod%C3%A8le/k-NN/ROC.png)

# Évaluation des Performances du Modèle k-NN

Le modèle k-NN a été évalué pour sa capacité à **détecter la fraude** dans les transactions. Les résultats obtenus sont les suivants :

### Précision:
Le modèle présente une **précision de 0.88**, indiquant une fiabilité d'environ 88% lorsqu'il prédit une fraude.

### Rappel:
Avec un **rappel de 0.54**, le modèle réussit à **capturer environ 54%** de toutes les transactions frauduleuses.

### Aire sous la courbe ROC (AUC):
L'**AUC atteint 0.77**, ce qui est considéré comme acceptable mais pourrait être amélioré.

### Matrice de Confusion:
La matrice révèle un grand nombre de **vrais négatifs (transactions non frauduleuses)** correctement classées, mais quelques **faux négatifs (fraudes manquées)**.

### Rapport de Classification:
Le rapport détaille davantage la performance du modèle, mettant en évidence une **précision élevée** mais un **rappel relativement bas**.

## Interprétation:

Le modèle k-NN démontre une **bonne précision**, assurant une fiabilité élevée lorsqu'il prédit une fraude. Cependant, son **rappel relativement bas** suggère qu'il manque certaines fraudes, nécessitant une amélioration pour une détection plus exhaustive. L'**AUC est acceptable** mais pourrait bénéficier d'ajustements pour renforcer la capacité de discrimination du modèle.

## Implications Pratiques:

- Le modèle est efficace pour **identifier les transactions non frauduleuses**.
- Des améliorations peuvent être explorées pour **capturer davantage de fraudes**.
- Le choix entre **précision et rappel** dépend des coûts associés aux erreurs de classification.
- L'ajustement du **seuil de classification** peut optimiser la balance entre précision et rappel en fonction des besoins spécifiques.
