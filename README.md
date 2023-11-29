# Projet-5-ML

## Synthèse des Modèles

### k-NN (KNeighborsClassifier)
- **Précision:** 0.88
- **Rappel:** 0.54
- **Aire sous la courbe ROC (AUC):** 0.77

*Interprétation :* Le modèle k-NN a une précision relativement élevée, mais le rappel est un peu faible, ce qui signifie qu'il peut manquer certaines fraudes. L'Aire sous la courbe ROC (AUC) indique une performance moyenne en termes de discrimination entre les classes.

### RandomForestClassifier
- **Précision:** 0.98
- **Rappel:** 0.79
- **Aire sous la courbe ROC (AUC):** 0.89

*Interprétation :* Le modèle RandomForestClassifier a une excellente précision et un rappel décent. L'AUC est élevée, indiquant une bonne capacité de discrimination entre les classes. Cela suggère que le modèle est robuste et performant.

### MLPClassifier
- **Précision:** 1.00
- **Rappel:** 0.01
- **Aire sous la courbe ROC (AUC):** 0.51

*Interprétation :* Le modèle MLPClassifier a une précision parfaite, mais un rappel très faible, ce qui signifie qu'il identifie bien les non-fraudes, mais manque beaucoup de fraudes. L'AUC est également faible, indiquant une performance médiocre en termes de discrimination.

### LogisticRegression
- **Précision:** 0.78
- **Rappel:** 0.44
- **Aire sous la courbe ROC (AUC):** 0.72

*Interprétation :* La régression logistique a une précision décente, mais un rappel assez bas. L'AUC est également moyen. Bien que ce modèle soit équilibré, il pourrait ne pas être aussi performant que le RandomForestClassifier.

### Conclusion
Le RandomForestClassifier semble être le meilleur choix, car il présente une combinaison élevée de précision, rappel et AUC. Il offre une bonne balance entre la capacité à détecter les fraudes et à éviter les faux positifs. En fonction de ces résultats, il serait recommandé de retenir le modèle RandomForestClassifier pour la détection de la fraude dans ce contexte.

## Synthèse du Projet

### Apprentissages

1. **Manipulation de Données :** J'ai perfectionné mes compétences en manipulation de données avec pandas. Nettoyer et préparer les données pour les modèles de machine learning a été une étape cruciale.

2. **Modélisation :** J'ai exploré divers algorithmes de machine learning tels que k-NN, RandomForest, MLP, et Logistic Regression. Comprendre le fonctionnement de chaque modèle et leurs implications a été enrichissant.

3. **Évaluation de Modèles :** L'évaluation des modèles au-delà des métriques standard (précision, rappel, AUC) m'a permis de mieux comprendre leurs forces et faiblesses.

### Réalisations

1. **Implémentation de Modèles :** J'ai réussi à mettre en œuvre plusieurs modèles de machine learning pour la détection de fraudes, chacun avec ses avantages et inconvénients.

2. **Optimisation de Performances :** J'ai travaillé sur l'optimisation des performances des modèles, en ajustant les hyperparamètres et en explorant différentes approches pour améliorer la détection.

3. **Visualisation des Résultats :** La création de visualisations telles que les courbes ROC et les matrices de confusion a été cruciale pour interpréter les résultats et les présenter de manière claire.

### Défis Rencontrés

1. **Déséquilibre des Classes :** Le déséquilibre entre les classes frauduleuses et non frauduleuses a posé un défi, nécessitant des techniques telles que le sous-échantillonnage et le suréchantillonnage.

2. **Choix du Modèle :** Sélectionner le modèle optimal a été difficile en raison des compromis entre précision et rappel. Choisir celui qui convient le mieux au contexte a demandé une analyse approfondie.

3. **Interprétation des Résultats :** Comprendre comment interpréter les résultats de manière contextuelle a été une étape importante, impliquant une réflexion approfondie sur les implications pratiques des prédictions.

En conclusion, ce projet m'a offert une expérience approfondie dans le domaine de la détection de fraudes, en mettant en lumière les nuances liées à la modélisation, à l'évaluation et à l'application pratique des résultats. Les défis rencontrés ont renforcé ma capacité à résoudre des problèmes complexes et à prendre des décisions éclairées dans le domaine de l'apprentissage automatique appliqué.
