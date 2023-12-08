# Importation des modules nécessaires
from sklearn.ensemble import RandomForestClassifier  # Importation du modèle RandomForestClassifier
import pandas as pd  # Importation de la bibliothèque pandas pour la manipulation des données
from sklearn.model_selection import train_test_split  # Importation de la fonction pour diviser le jeu de données
from sklearn.preprocessing import LabelEncoder, binarize  # Importation des outils de prétraitement des données
from sklearn.metrics import precision_score, recall_score, roc_auc_score, confusion_matrix, roc_curve, auc, classification_report  # Importation des métriques d'évaluation
import matplotlib.pyplot as plt  # Importation de la bibliothèque de visualisation matplotlib
import seaborn as sns  # Importation de la bibliothèque de visualisation seaborn
import os  # Importation du module pour la gestion des chemins de fichiers

# Fonction pour afficher la matrice de confusion
def plot_confusion_matrix(y_true, y_scores, threshold=0.5):
    # Binarisation des prédictions avec un seuil spécifié
    y_pred = (y_scores > threshold).astype(int)
    
    # Calcul de la matrice de confusion
    cm = confusion_matrix(y_true, y_pred)
    
    # Affichage de la matrice de confusion avec seaborn
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
file_path = os.path.join(script_directory, '..', 'data', 'bank.csv')  # Obtention du chemin du fichier CSV
df = pd.read_csv(file_path)  # Chargement des données dans un DataFrame pandas

# Initialisation de la fonction LabelEncoder()
label_encoder = LabelEncoder()

# Conversion des données catégorielles en données numériques utilisables par le modèle
df['type'] = label_encoder.fit_transform(df['type'])
df['nameOrig'] = label_encoder.fit_transform(df['nameOrig'])
df['nameDest'] = label_encoder.fit_transform(df['nameDest'])

# Définition de la donnée cible
X = df.drop('isFraud', axis=1)
y = df['isFraud']

# Binarisation de la variable cible
y_binary = binarize(y.values.reshape(-1, 1)).ravel()

# Division du Dataset en un ensemble d'entraînement et un ensemble de test
X_train, X_test, y_train, y_test = train_test_split(X, y_binary, test_size=0.2, random_state=125)

# Initialisation du modèle RandomForestClassifier avec 100 estimateurs
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)  # Vous pouvez ajuster le nombre d'estimateurs (n_estimators) selon vos besoins
rf_classifier.fit(X_train, y_train)

# Test du modèle
predictions_rf = rf_classifier.predict(X_test)

# Binarisation des prédictions
predictions_binary_rf = binarize(predictions_rf.reshape(-1, 1)).ravel()

# Calcul de la précision, du rappel et de l'AUC pour RandomForestClassifier
precision_rf = precision_score(y_test, predictions_binary_rf)
recall_rf = recall_score(y_test, predictions_binary_rf)
roc_auc_rf = roc_auc_score(y_test, predictions_rf)

# Affichage des résultats d'évaluation pour RandomForestClassifier
print("Précision (RandomForest): {:.2f}".format(precision_rf))
print("Rappel (RandomForest): {:.2f}".format(recall_rf))
print("Aire sous la courbe ROC (AUC) (RandomForest): {:.2f}".format(roc_auc_rf))

# Évaluer les performances du modèle RandomForestClassifier avec confusion_matrix
cm_rf = confusion_matrix(y_test, predictions_binary_rf)
print("Matrice de Confusion (RandomForest):")
print(cm_rf)

# Afficher la matrice de confusion pour RandomForestClassifier
plot_confusion_matrix(y_test, predictions_binary_rf)

# Afficher la courbe ROC pour RandomForestClassifier
fpr_rf, tpr_rf, thresholds_rf = roc_curve(y_test, predictions_rf)
area_under_curve_rf = auc(fpr_rf, tpr_rf)

plt.figure()
plt.plot(fpr_rf, tpr_rf, color='darkorange', lw=2, label='Courbe ROC (AUC = {:.2f}) (RandomForest)'.format(area_under_curve_rf))
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('Taux de faux positifs')
plt.ylabel('Taux de vrais positifs')
plt.title('Courbe ROC (RandomForest)')
plt.legend(loc="lower right")
plt.show()

# Afficher le rapport de classification pour RandomForestClassifier
print("Rapport de Classification (RandomForest) :\n", classification_report(y_test, predictions_binary_rf))
