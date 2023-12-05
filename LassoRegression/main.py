# Importation des modules nécessaires
from sklearn.linear_model import Lasso
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score, roc_curve, auc
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.preprocessing import LabelEncoder

# Fonction pour plotter la matrice de confusion
def plot_confusion_matrix(y_true, y_pred, threshold=0.5):
    y_pred_binary = (y_pred > threshold).astype(int)
    cm = confusion_matrix(y_true, y_pred_binary)
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

# Régression Lasso
lasso_regression = Lasso(alpha=0.01)  # Vous pouvez ajuster le paramètre alpha si nécessaire
lasso_regression.fit(X_train, y_train)

# Prédiction sur l'ensemble de test
predictions = lasso_regression.predict(X_test)

# Binarisation des prédictions (utilisation d'un seuil, par exemple 0.5)
predictions_binary = (predictions > 0.5).astype(int)

# Évaluation du modèle
print("Matrice de Confusion:")
print(confusion_matrix(y_test, predictions_binary))
print("\nRapport de Classification :\n", classification_report(y_test, predictions_binary))

# Calcul de l'AUC-ROC
roc_auc = roc_auc_score(y_test, predictions)
print("Aire sous la courbe ROC (AUC): {:.2f}".format(roc_auc))

# Afficher la matrice de confusion sous forme de diagramme avec seaborn
plot_confusion_matrix(y_test, predictions, threshold=0.5)

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
