# Importation des modules nécessaires
from xgboost import XGBClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import precision_score, recall_score, roc_auc_score, confusion_matrix, roc_curve, auc, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Fonction pour plotter la matrice de confusion
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

# Chargement du fichier CSV nettoyé depuis le chemin spécifique
script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, '..', 'data', 'bank.csv')
df = pd.read_csv(file_path)

# Initialisation de la fonction LabelEncoder()
label_encoder = LabelEncoder()

# Conversion des données catégorielles en données numériques utilisables par le modèle
df['type'] = label_encoder.fit_transform(df['type'])
df['nameOrig'] = label_encoder.fit_transform(df['nameOrig'])
df['nameDest'] = label_encoder.fit_transform(df['nameDest'])

# Définition de la donnée cible
X = df.drop('isFraud', axis=1)
y = df['isFraud']

# Division du Dataset en un ensemble d'entraînement et un ensemble de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=125)

# XGBoost
xgb_classifier = XGBClassifier(random_state=125)
xgb_classifier.fit(X_train, y_train)

# Probabilités continues prédites pour la classe positive (fraude)
probabilities = xgb_classifier.predict_proba(X_test)[:, 1]

# Binarisation des prédictions
predictions_binary = (probabilities > 0.5).astype(int)

# Calcul de la précision, du rappel et de l'AUC
precision = precision_score(y_test, predictions_binary)
recall = recall_score(y_test, predictions_binary)
roc_auc = roc_auc_score(y_test, probabilities)

# Affichage des résultats d'évaluation
print("Précision: {:.2f}".format(precision))
print("Rappel: {:.2f}".format(recall))
print("Aire sous la courbe ROC (AUC): {:.2f}".format(roc_auc))

# Évaluer les performances du modèle avec confusion_matrix
cm = confusion_matrix(y_test, predictions_binary)
print("Matrice de Confusion:")
print(cm)

# Afficher la matrice de confusion sous forme de diagramme avec seaborn
plot_confusion_matrix(y_test, probabilities)

# Afficher la courbe ROC
fpr, tpr, thresholds = roc_curve(y_test, probabilities)
area_under_curve = auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label='Courbe ROC (AUC = {:.2f})'.format(area_under_curve))
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('Taux de faux positifs')
plt.ylabel('Taux de vrais positifs')
plt.title('Courbe ROC')
plt.legend(loc="lower right")
plt.show()

# Afficher le rapport de classification
print("Rapport de Classification :\n", classification_report(y_test, predictions_binary))
