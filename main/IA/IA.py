#   Ceci est un code pour créer une ia qui propose des recommandation basé sur les bonnes ou mauvaise réponse d'un questionnaire
#   Pour le cours de philo 2 Cchic
#   Questions basées sur les notes de cours personnelles de météo 1 du CQFA
#
#   Olivier Moreau
#

import joblib
import pandas as pd

def IA(taux_hum, taux_réch, taux_refr) :

    chargement_model = joblib.load("base_de_donnee_IA.joblib")
    taux = pd.DataFrame([[taux_hum,taux_réch,taux_refr]], columns = ["taux_humidité", "taux_réchauffement", "taux_refroidissement"])
    résultat = chargement_model.predict(taux)

    return(résultat)