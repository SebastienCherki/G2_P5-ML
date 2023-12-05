# Importation des modules nécessaires
import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

# Chargement du fichier CSV nettoyé depuis le chemin spécifique
script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, '..', 'data', 'bank.csv')
df = pd.read_csv(file_path)

# Utilisation de LabelEncoder pour les variables catégorielles
label_encoder = LabelEncoder()
categorical_columns = ['type', 'nameOrig', 'nameDest']

for col in categorical_columns:
    df[col] = label_encoder.fit_transform(df[col])

# Sélection d'un sous-ensemble des données pour réduire la taille
df_sample = df.sample(frac=0.1, random_state=125)

# Conversion des données catégorielles en données numériques
df_encoded = pd.get_dummies(df_sample, columns=categorical_columns)

# Appliquer l'algorithme Apriori
frequent_itemsets = apriori(df_encoded, min_support=0.1, use_colnames=True)

# Génération des règles d'association
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

# Affichage des règles d'association
print("Règles d'Association :\n", rules)
