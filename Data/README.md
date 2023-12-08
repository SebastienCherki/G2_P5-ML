
## Synthèse du dataset

- **step**: Un indicateur de temps ou d'étape pour la transaction.
- **type**: Le type de transaction (PAYMENT, TRANSFER, CASH_OUT, DEBIT).
- **amount**: Le montant de la transaction.
- **nameOrig**: Le nom du client ou de l'entité d'origine.
- **oldbalanceOrg**: Le solde initial de l'entité d'origine avant la transaction.
- **newbalanceOrig**: Le nouveau solde de l'entité d'origine après la transaction.
- **nameDest**: Le nom du destinataire de la transaction.
- **oldbalanceDest**: Le solde initial du destinataire avant la transaction.
- **newbalanceDest**: Le nouveau solde du destinataire après la transaction.
- **isFraud**: Un indicateur binaire indiquant si la transaction est frauduleuse (1 pour vrai, 0 pour faux).
- **isFlaggedFraud**: Un indicateur binaire signalant si la transaction a été signalée comme frauduleuse.

![Dataset Brut](https://github.com/SebastienCherki/G2_P5-ML/blob/main/Data/dataset_no_clean.PNG)

## Nettoyage de Données et Modifications Introduites dans le Modèle de Détection de Fraude

Dans le cadre du projet de détection de fraude, une étape cruciale a été consacrée au nettoyage des données afin d'améliorer la qualité des informations fournies au modèle d'apprentissage automatique. Le jeu de données initial présentait divers défis, notamment des valeurs manquantes, des caractéristiques catégorielles non numériques et des incohérences.

### Gestion des Valeurs Manquantes

Pour remédier aux valeurs manquantes, la méthode d'imputation a été utilisée. Cependant, au lieu de remplacer les valeurs manquantes par la moyenne, une approche plus approfondie a été adoptée. Les lignes comportant des données manquantes ont été supprimées afin de préserver l'intégrité des informations existantes, évitant ainsi d'introduire une distorsion par des imputations artificielles.

### Encodage des Variables Catégorielles

Les variables catégorielles, telles que le type de transaction, les noms d'origine et de destination, ont été encodées numériquement à l'aide de la méthode LabelEncoder. Cette transformation permet au modèle de traiter ces informations de manière numérique tout en préservant la signification des catégories.

### Suppression des Doublons

La présence de doublons dans le jeu de données initial a été identifiée et ces entrées redondantes ont été supprimées. Cela vise à garantir une représentation unique de chaque observation, éliminant ainsi tout impact négatif pouvant résulter de la duplication des données.

### Normalisation des Caractéristiques Numériques

Les caractéristiques numériques ont été normalisées à l'aide d'une transformation standard, ce qui a pour effet de mettre toutes les variables numériques à la même échelle. Cela est particulièrement important pour les algorithmes qui sont sensibles aux écarts d'échelle entre les caractéristiques.

### Suréchantillonnage des Classes Déséquilibrées

En raison de la nature déséquilibrée du jeu de données, une technique de suréchantillonnage, en utilisant la méthode SMOTE, a été appliquée. Cela vise à créer une distribution plus équilibrée entre les classes "fraude" et "non-fraude", améliorant ainsi la capacité du modèle à détecter les fraudes.

Ces ajustements ont été apportés dans l'objectif d'améliorer la qualité des données et, par conséquent, d'optimiser les performances du modèle de détection de fraude. Cependant, il est essentiel de noter que l'évolution des performances du modèle peut nécessiter une itération continue de ces processus afin d'atteindre un équilibre optimal entre nettoyage des données et puissance prédictive. Les résultats obtenus devraient être interprétés et ajustés en fonction des exigences spécifiques du projet.

![Dataset Nettoyé](https://github.com/SebastienCherki/G2_P5-ML/blob/main/Data/dataset_clean.PNG)


