import os
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from imblearn.over_sampling import SMOTE

# Charger le dataset
script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, '..', 'data', 'bank.csv')
df = pd.read_csv(file_path)

# Supprimer les lignes avec des données manquantes
df.dropna(inplace=True)

# Encodage des variables catégorielles (utilisation de LabelEncoder)
label_encoder = LabelEncoder()
categorical_columns = ['type', 'nameOrig', 'nameDest']
df[categorical_columns] = df[categorical_columns].apply(label_encoder.fit_transform)

# Suppression des doublons
df = df.drop_duplicates()

# Normalisation des caractéristiques numériques
scaler = StandardScaler()
numeric_columns = ['amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest']
df[numeric_columns] = scaler.fit_transform(df[numeric_columns])

# Gestion des classes déséquilibrées (exemple de suréchantillonnage avec SMOTE)
X_resampled, y_resampled = SMOTE().fit_resample(df.drop(['isFraud', 'isFlaggedFraud'], axis=1), df['isFraud'])
df_resampled = pd.concat([X_resampled, y_resampled], axis=1)

# Sauvegarder le nouveau dataset nettoyé
cleaned_file_path = os.path.join(script_directory, '..', 'data', 'bank1.csv')
df_resampled.to_csv(cleaned_file_path, index=False)
