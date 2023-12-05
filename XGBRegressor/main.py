# Importation des modules nécessaires
from xgboost import XGBRegressor
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, precision_score, recall_score, roc_auc_score, confusion_matrix, roc_curve, auc, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.preprocessing import LabelEncoder

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

# Utilisation de LabelEncoder pour les variables catégorielles
label_encoder = LabelEncoder()
categorical_columns = ['type', 'nameOrig', 'nameDest']

for col in categorical_columns:
    df[col] = label_encoder.fit_transform(df[col])

# Définition de la donnée cible
X = df.drop('isFraud', axis=1)
y = df['isFraud']

# Division du Dataset en un ensemble d'entraînement et un ensemble de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=125)

# XGBoost Regressor
xgb_regressor = XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=125)
xgb_regressor.fit(X_train, y_train)

# Prédiction sur l'ensemble de test
predictions = xgb_regressor.predict(X_test)

# Mesures d'évaluation pour la régression
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Mean Squared Error (MSE): {:.2f}".format(mse))
print("R-squared (R2): {:.2f}".format(r2))

# Afficher la prédiction par rapport à la vérité terrain
plt.scatter(y_test, predictions)
plt.xlabel("Vérité Terrain")
plt.ylabel("Prédiction")
plt.title("Prédiction par rapport à la Vérité Terrain")
plt.show()

# Mesures d'évaluation spécifiques à la classification
# (Gardez cette partie si vous souhaitez évaluer la classification)
# Binarisation de la variable cible
y_binary = (y > 0).astype(int)

# Prédiction sur l'ensemble de test
predictions_binary = (predictions > 0.5).astype(int)

# Calcul de la précision, du rappel et de l'AUC
precision = precision_score(y_test, predictions_binary)
recall = recall_score(y_test, predictions_binary)
roc_auc = roc_auc_score(y_test, predictions)

# Affichage des résultats d'évaluation
print("Précision: {:.2f}".format(precision))
print("Rappel: {:.2f}".format(recall))
print("Aire sous la courbe ROC (AUC): {:.2f}".format(roc_auc))

# Évaluer les performances du modèle avec confusion_matrix
cm = confusion_matrix(y_test, predictions_binary)
print("Matrice de Confusion:")
print(cm)

# Afficher la matrice de confusion sous forme de diagramme avec seaborn
plot_confusion_matrix(y_test, predictions)

# Afficher la courbe ROC
fpr, tpr, thresholds = roc_curve(y_test, predictions)
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
