# Importation des modules nécessaires
import os
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import IsolationForest
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split

# Chargement du fichier CSV nettoyé depuis le chemin spécifique
script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, '..', 'data', 'bank.csv')
df = pd.read_csv(file_path)

# Utilisation de LabelEncoder pour les variables catégorielles
label_encoder = LabelEncoder()
categorical_columns = ['type', 'nameOrig', 'nameDest']

for col in categorical_columns:
    df[col] = label_encoder.fit_transform(df[col])

# Standardisation des données
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df.drop(['isFraud'], axis=1))

# Réduction de dimension avec PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Division du Dataset en un ensemble d'entraînement et un ensemble de test
X_train, X_test, y_train, y_test = train_test_split(X_pca, df['isFraud'], test_size=0.2, random_state=125)

# Isolation Forest
isolation_forest = IsolationForest(random_state=125)
isolation_forest.fit(X_train)

# Prédiction des anomalies
predictions = isolation_forest.predict(X_test)

# Transformer les prédictions (-1 pour les anomalies, 1 pour les normales) en 0 et 1
predictions_binary = [1 if x == 1 else 0 for x in predictions]

# Matrice de confusion
cm = confusion_matrix(y_test, predictions_binary)

# Affichage de la matrice de confusion sous forme de diagramme avec seaborn
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False,
            xticklabels=["Pas de Fraude", "Fraude"],
            yticklabels=["Pas de Fraude", "Fraude"])
plt.xlabel('Prédit')
plt.ylabel('Réel')
plt.title('Matrice de Confusion')
plt.show()

# Affichage du rapport de classification
print("Rapport de Classification :\n", classification_report(y_test, predictions_binary))
