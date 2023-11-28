# Importation de la bibliothèque Pandas sous le raccourci 'pd'
import pandas as pd

# Importation de la bibliothèque NumPy sous le raccourci 'np'
import numpy as np

# Importation de la bibliothèque Seaborn sous le raccourci 'sns'
import seaborn as sns

# Importation de la bibliothèque pyplot de Matplotlib sous le raccourci 'plt'
from matplotlib import pyplot as plt

# Importation de la fonction 'train_test_split' de scikit-learn pour diviser les données
from sklearn.model_selection import train_test_split

# Importation de certaines métriques de performance (classification_report, confusion_matrix, precision_score, recall_score, roc_curve, auc)
from sklearn.metrics import classification_report, confusion_matrix, precision_score, recall_score, roc_curve, auc

# Importation du modèle RandomForestClassifier de scikit-learn
from sklearn.ensemble import RandomForestClassifier

# Configuration des paramètres de visualisation pour Seaborn
sns.set()

# Définition d'une fonction pour tracer la courbe ROC
def plot_roc_curve(y_true, y_scores):
    # Calcul des taux de faux positifs, vrais positifs et seuils pour la courbe ROC
    fpr, tpr, thresholds = roc_curve(y_true, y_scores)
    # Calcul de l'aire sous la courbe ROC (AUC)
    roc_auc = auc(fpr, tpr)
    # Création d'une figure avec Seaborn
    plt.figure(figsize=(8, 6))
    # Tracé de la courbe ROC avec des étiquettes et des paramètres esthétiques
    plt.plot(fpr, tpr, color='darkorange', lw=2, label='Courbe ROC (AUC = {:.2f})'.format(roc_auc))
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')  # Ligne en pointillés
    plt.xlabel('Taux de Faux Positifs')
    plt.ylabel('Taux de Vrais Positifs')
    plt.title('Courbe ROC')
    plt.legend(loc='lower right')  # Légende en bas à droite
    plt.show()  # Affichage de la figure

# Définition d'une fonction pour tracer la matrice de confusion
def plot_confusion_matrix(y_true, y_scores, threshold=0.5):
    # Convertir les scores de probabilité en classes binaires en fonction du seuil
    y_pred = (y_scores > threshold).astype(int)
    # Calcul de la matrice de confusion
    cm = confusion_matrix(y_true, y_pred)
    # Création d'une figure avec Seaborn
    plt.figure(figsize=(8, 6))
    # Tracé de la matrice de confusion avec des annotations et des paramètres esthétiques
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False,
                xticklabels=["Pas de Fraude", "Fraude"],
                yticklabels=["Pas de Fraude", "Fraude"])
    plt.xlabel('Prédit')
    plt.ylabel('Réel')
    plt.title('Matrice de Confusion')
    plt.show()  # Affichage de la figure

# Définition de l'ordre des colonnes pour la visualisation
ordre_des_colonnes = ['step', 'type', 'amount', 'nameOrig', 'oldbalanceOrg', 'newbalanceOrig',
                      'nameDest', 'oldbalanceDest', 'newbalanceDest', 'isFraud', 'isFlaggedFraud']

# Chargement du fichier CSV nettoyé dans un DataFrame avec Pandas
df = pd.read_csv('../data/bank_clean.csv')

# Sélection des colonnes numériques dans le DataFrame
X = df.select_dtypes(include=['float64', 'int64'])

# Division des données en ensembles d'entraînement et de test avec train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, df['isFraud'], test_size=0.2, random_state=42)

# Initialisation du modèle RandomForestClassifier avec 100 arbres et une graine aléatoire
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Entraînement du modèle sur l'ensemble d'entraînement
model.fit(X_train, y_train)

# Faire des prédictions sur l'ensemble de test
predictions = model.predict(X_test)

# Obtenir les probabilités des prédictions pour la courbe ROC
y_scores = model.predict_proba(X_test)[:, 1]

# Évaluation des performances du modèle en utilisant les fonctions définies précédemment
plot_confusion_matrix(y_test, y_scores)
plot_roc_curve(y_test, y_scores)

# Affichage du rapport de classification
print("Rapport de Classification :\n", classification_report(y_test, predictions))
