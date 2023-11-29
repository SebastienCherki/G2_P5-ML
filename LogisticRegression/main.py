# Importation des modules nécessaires
from sklearn.linear_model import LogisticRegression  # Importation du modèle de régression logistique
import pandas as pd  # Importation de la bibliothèque pandas pour la manipulation des données
from sklearn.model_selection import train_test_split  # Importation de la fonction pour diviser le jeu de données
from sklearn.preprocessing import LabelEncoder, binarize  # Importation des outils de prétraitement des données
from sklearn.metrics import precision_score, recall_score, roc_auc_score, confusion_matrix, roc_curve, auc, classification_report  # Importation des métriques d'évaluation
import matplotlib.pyplot as plt  # Importation de la bibliothèque pour la visualisation
import seaborn as sns  # Importation de la bibliothèque de visualisation avancée
import os  # Importation du module pour travailler avec les chemins de fichiers

# Fonction pour afficher la matrice de confusion
def plot_confusion_matrix(y_true, y_scores, threshold=0.5):
    # Binarisation des prédictions avec un seuil spécifié
    y_pred = (y_scores > threshold).astype(int)
    
    # Calcul de la matrice de confusion
    cm = confusion_matrix(y_true, y_pred)
    
    # Plot de la matrice de confusion avec seaborn
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False,
                xticklabels=["Pas de Fraude", "Fraude"],
                yticklabels=["Pas de Fraude", "Fraude"])
    plt.xlabel('Prédit')
    plt.ylabel('Réel')
    plt.title('Matrice de Confusion')
    plt.show()

# Chargement du fichier CSV nettoyé depuis le chemin spécifique
script_directory = os.path.dirname(os.path.abspath(__file__))  # Obtention du répertoire du script
file_path = os.path.join(script_directory, '..', 'data', 'bank.csv')  # Construction du chemin du fichier CSV
df = pd.read_csv(file_path)  # Chargement du fichier CSV dans un DataFrame

# Initialisation de la fonction LabelEncoder()
label_encoder = LabelEncoder()  # Initialisation de l'encodeur de libellé pour convertir les catégories en nombres

# Conversion des données catégorielles en données numériques utilisables par le modèle
df['type'] = label_encoder.fit_transform(df['type'])
df['nameOrig'] = label_encoder.fit_transform(df['nameOrig'])
df['nameDest'] = label_encoder.fit_transform(df['nameDest'])

# Définition de la donnée cible
X = df.drop('isFraud', axis=1)  # Les caractéristiques du modèle
y = df['isFraud']  # La variable cible à prédire

# Binarisation de la variable cible
y_binary = binarize(y.values.reshape(-1, 1)).ravel()  # Binarisation des valeurs pour les classes (0 ou 1)

# Division du Dataset en un ensemble d'entraînement et un ensemble de test
X_train, X_test, y_train, y_test = train_test_split(X, y_binary, test_size=0.2, random_state=125)  # Division du jeu de données

# Logistic Regression
logreg_classifier = LogisticRegression(random_state=125)  # Initialisation du modèle de régression logistique
logreg_classifier.fit(X_train, y_train)  # Entraînement du modèle sur l'ensemble d'entraînement

# Test du modèle
predictions = logreg_classifier.predict(X_test)  # Prédictions sur l'ensemble de test

# Binarisation des prédictions
predictions_binary = binarize(predictions.reshape(-1, 1)).ravel()  # Binarisation des valeurs prédites

# Calcul de la précision, du rappel et de l'AUC
precision = precision_score(y_test, predictions_binary)  # Calcul de la précision
recall = recall_score(y_test, predictions_binary)  # Calcul du rappel
roc_auc = roc_auc_score(y_test, predictions)  # Calcul de l'AUC

# Affichage des résultats d'évaluation
print("Précision: {:.2f}".format(precision))
print("Rappel: {:.2f}".format(recall))
print("Aire sous la courbe ROC (AUC): {:.2f}".format(roc_auc))

# Évaluer les performances du modèle avec confusion_matrix
cm = confusion_matrix(y_test, predictions_binary)  # Calcul de la matrice de confusion
print("Matrice de Confusion:")
print(cm)

# Afficher la matrice de confusion sous forme de diagramme avec seaborn
plot_confusion_matrix(y_test, predictions_binary)

# Afficher la courbe ROC
fpr, tpr, thresholds = roc_curve(y_test, predictions)  # Calcul des valeurs pour la courbe ROC
area_under_curve = auc(fpr, tpr)  # Calcul de l'aire sous la courbe ROC

plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label='Courbe ROC (AUC = {:.2f})'.format(area_under_curve))  # Plot de la courbe ROC
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('Taux de faux positifs')
plt.ylabel('Taux de vrais positifs')
plt.title('Courbe ROC')
plt.legend(loc="lower right")
plt.show()

# Afficher le rapport de classification
print("Rapport de Classification :\n", classification_report(y_test, predictions_binary))
