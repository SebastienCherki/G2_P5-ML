import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.ensemble import RandomForestClassifier

# Configuration de la visualisation
sns.set()

# Fonction pour tracer la matrice de confusion
def plot_confusion_matrix(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False,
                xticklabels=["Pas de Fraude", "Fraude"],
                yticklabels=["Pas de Fraude", "Fraude"])
    plt.xlabel('Prédit')
    plt.ylabel('Réel')
    plt.title('Matrice de Confusion')
    plt.show()

# Définir l'ordre des colonnes
ordre_des_colonnes = ['step', 'type', 'amount', 'nameOrig', 'oldbalanceOrg', 'newbalanceOrig',
                      'nameDest', 'oldbalanceDest', 'newbalanceDest', 'isFraud', 'isFlaggedFraud']

# Charger le fichier CSV nettoyé dans un DataFrame
df = pd.read_csv('bank_nettoye.csv')

# Sélectionner uniquement les colonnes numériques
X = df.select_dtypes(include=['float64', 'int64'])

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, df['isFraud'], test_size=0.2, random_state=42)

# Initialiser un modèle (Random Forest Classifier dans cet exemple)
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Entraîner le modèle sur l'ensemble d'entraînement
model.fit(X_train, y_train)

# Faire des prédictions sur l'ensemble de test
predictions = model.predict(X_test)

# Évaluer les performances du modèle
accuracy = accuracy_score(y_test, predictions)
report = classification_report(y_test, predictions)

# Afficher les résultats de la matrice de confusion
plot_confusion_matrix(y_test, predictions)

# Afficher les résultats
print(f"Précision : {accuracy}")
print("Rapport de Classification :\n", report)
