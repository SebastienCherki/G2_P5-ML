```
Précision: 1.00
Rappel: 0.01
Aire sous la courbe ROC (AUC): 0.51
Matrice de Confusion:
[[1270901       0]
 [   1599      24]]
Rapport de Classification :
               precision    recall  f1-score   support

           0       1.00      1.00      1.00   1270901
           1       1.00      0.01      0.03      1623

    accuracy                           1.00   1272524
   macro avg       1.00      0.51      0.51   1272524
weighted avg       1.00      1.00      1.00   1272524
```

![Matrice de Confusion.](https://github.com/SebastienCherki/G2_P5-ML/blob/main/Bonus/MLPClassifier/Matrice%20de%20Confusion.png)
![Courbe ROC](https://github.com/SebastienCherki/G2_P5-ML/blob/main/Bonus/MLPClassifier/ROC.png)

# Évaluation des Performances du Modèle MLPClassifier

Le modèle MLPClassifier a été évalué pour sa capacité à **détecter la fraude** dans les transactions. Les résultats obtenus sont les suivants :

### Précision:
Le modèle présente une **précision parfaite de 1.00**, indiquant une fiabilité totale lorsqu'il prédit une fraude.

### Rappel:
Avec un **rappel de 0.01**, le modèle réussit à **capturer seulement 1%** de toutes les transactions frauduleuses.

### Aire sous la courbe ROC (AUC):
L'**AUC atteint 0.51**, indiquant une capacité de discrimination minimale.

### Interprétation:

Le modèle MLPClassifier présente une **précision parfaite**, mais son **rappel extrêmement bas** et son **AUC faible** soulignent des défis majeurs dans la détection de la fraude.

## Implications Pratiques:

- Bien que le modèle soit **parfaitement précis dans la prédiction des fraudes**, il manque la grande majorité des transactions frauduleuses, comme indiqué par le **rappel très bas**.
- L'AUC de 0.51 suggère une **capacité de discrimination faible** par rapport aux autres modèles évalués.
- Des ajustements significatifs ou l'exploration d'autres approches peuvent être nécessaires pour améliorer la performance du modèle dans la détection de la fraude.

