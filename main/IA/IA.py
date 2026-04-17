#   Ceci est un code pour créer une ia qui propose des recommandation basé sur les bonnes ou mauvaise réponse d'un questionnaire
#   Pour le cours de philo 2 Cchic
#   Questions basées sur les notes de cours personnelles de météo 1 du CQFA
#
#   Olivier Moreau
#
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

donné = pd.read_csv("basedonne.csv")
x = donné[["taux_humidité", "taux_réchauffement", "taux_refroidissement"]]
y = donné["résultat"]

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.1)

model = RandomForestClassifier(random_state = 42)
model.fit(X_train, y_train)
prédiction = model.predict(X_test)
accuracy = accuracy_score(y_test, prédiction)
print(accuracy)

nom_fichier = "base_de_donnee_IA.joblib"
joblib.dump(model, nom_fichier)

chargement_model = joblib.load("base_de_donnee_IA.joblib")
taux = pd.DataFrame([[0.98, 0.98, 0.60]], columns = ["taux_humidité", "taux_réchauffement", "taux_refroidissement"])
résultat = chargement_model.predict(taux)
print(résultat)

#Bravo, tu es excellent, tu as eu 100% partout. As-tu triché?                        7
#Excellent résultat, tu connais très bien ta matière.                                6
#Tu y es presque. Tu n'as fait que quelque erreurs                                   5
#Tu comprends bien ces catégories. Il ne te reste qu'a réviser cette catégorie       4
#En général, tu comprends bien, mais tu fais des erreurs dans ces catégories         3
#Tu fais beacoup d'erreur dans ces catégories, je te conseil de réviser              2
#Prends-tu le test au serieux!!!                                                     1