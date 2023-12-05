# Importation des modules nécessaires
import os
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder  # Ajout de l'importation de LabelEncoder
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

# KMeans
kmeans = KMeans(n_clusters=2, random_state=125)
kmeans.fit(X_train)

# Prédiction des clusters sur l'ensemble de test
test_clusters = kmeans.predict(X_test)

# Visualisation des clusters avec PCA
plt.scatter(X_test[:, 0], X_test[:, 1], c=test_clusters, cmap='viridis', s=50, alpha=0.5)
plt.title('Clusters avec KMeans')
plt.xlabel('Composante Principale 1')
plt.ylabel('Composante Principale 2')
plt.show()

# Évaluation de la détection de fraude basée sur les clusters
# Notez que cette évaluation est une approche simplifiée et pourrait nécessiter des ajustements en fonction de votre dataset et du contexte spécifique de la fraude.

# Déterminer le cluster majoritaire
majority_cluster = np.argmax(np.bincount(test_clusters))

# Affecter une classe prédite en fonction du cluster majoritaire
predicted_labels = np.where(test_clusters == majority_cluster, 0, 1)

# Matrice de confusion
cm = confusion_matrix(y_test, predicted_labels)

# Affichage de la matrice de confusion sous forme de diagramme avec seaborn
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False,
            xticklabels=["Pas de Fraude", "Fraude"],
            yticklabels=["Pas de Fraude", "Fraude"])
plt.xlabel('Prédit')
plt.ylabel('Réel')
plt.title('Matrice de Confusion')
plt.show()

# Affichage du rapport de classification
print("Rapport de Classification :\n", classification_report(y_test, predicted_labels))
