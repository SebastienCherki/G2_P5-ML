import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, precision_score, recall_score, roc_curve, auc
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import os

# Configuration de la visualisation
sns.set()

# Fonction pour tracer la courbe ROC
def plot_roc_curve(y_true, y_scores):
    fpr, tpr, thresholds = roc_curve(y_true, y_scores)
    roc_auc = auc(fpr, tpr)
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, color='darkorange', lw=2, label='Courbe ROC (AUC = {:.2f})'.format(roc_auc))
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlabel('Taux de Faux Positifs')
    plt.ylabel('Taux de Vrais Positifs')
    plt.title('Courbe ROC')
    plt.legend(loc='lower right')
    plt.show()

# Fonction pour tracer la matrice de confusion
def plot_confusion_matrix(y_true, y_scores, threshold=0.5):
    y_pred = (y_scores > threshold).astype(int)
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

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, '..', 'data', 'bank_clean.csv')

# Charger le fichier CSV nettoyé dans un DataFrame
df = pd.read_csv(file_path)

# Sélectionner uniquement les colonnes numériques
X = df.select_dtypes(include=['float64', 'int64'])

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, df['isFraud'], test_size=0.2, random_state=42)

# Initialiser un modèle de régression logistique
model = make_pipeline(StandardScaler(), LogisticRegression(random_state=42))

# Entraîner le modèle sur l'ensemble d'entraînement
model.fit(X_train, y_train)

# Faire des prédictions sur l'ensemble de test
predictions = model.predict(X_test)

# Obtenir les probabilités des prédictions pour la courbe ROC
y_scores = model.predict_proba(X_test)[:, 1]

# Évaluer les performances du modèle
plot_confusion_matrix(y_test, y_scores)
plot_roc_curve(y_test, y_scores)

# Afficher le rapport de classification
print("Rapport de Classification :\n", classification_report(y_test, predictions))
