#   Ceci est un code pour créer une ia qui propose des recommandation basé sur les bonnes ou mauvaise réponse d'un questionnaire
#   Pour le cours de philo 2 Cchic
#   Questions basées sur les notes de cours personnelles de météo 1 du CQFA
#
#   Olivier Moreau
#

import streamlit as st
import joblib
import pandas as pd

def prédiction() :

    taux_hum_avant = st.session_state.sjhumidité / st.session_state.thumidité
    taux_hum = round(taux_hum_avant, 2)

    taux_réch_avant = st.session_state.sjréchauffement / st.session_state.tréchauffement
    taux_réch = round(taux_réch_avant, 2)

    taux_refr_avant = st.session_state.sjrefroidissement / st.session_state.trefroidissement
    taux_refr = round(taux_refr_avant, 2)

    chargement_model = joblib.load("base_de_donnee_IA.joblib")
    taux = pd.DataFrame([[taux_hum,taux_réch,taux_refr]], columns = ["taux_humidité", "taux_réchauffement", "taux_refroidissement"])
    résultat_taux = chargement_model.predict(taux)[0]

    dict_taux = {
        "l'humidité" : taux_hum,
        "le réchauffement" : taux_réch,
        "le refroidissement" : taux_refr
    }

    catégorie_affiché = min(dict_taux, key = dict_taux.get)

    if résultat_taux == 1 :
        résultat = f"Prends-tu le test au serieux!!!"

    elif résultat_taux == 2 :
        résultat = f"Tu fais beacoup d'erreur dans plusieurs catégories. Je te conseil de réviser le chapitre sur {catégorie_affiché} car c'est dans cette catégorie que tu fais le plus d'erreurs."

    elif résultat_taux == 3 :
        résultat = f"En général, tu comprends bien, mais tu fais plusieurs erreurs. Je te conseil de réviser le chapitre sur {catégorie_affiché} car c'est dans cette catégorie que tu fais le plus d'erreurs."

    elif résultat_taux == 4 :
        résultat = f"Tu comprends bien la matière dans presque toutes les catégories. Il ne te reste qu'a réviser le chapitre sur {catégorie_affiché}."

    elif résultat_taux == 5 :
        résultat = f"Tu y es presque. Tu n'as fait que quelque erreurs"

    elif résultat_taux == 6 :
        résultat = f"Excellent résultat, tu connais très bien ta matière."

    elif résultat_taux == 7 :
        résultat = f"Bravo, tu es excellent, tu as eu 100% partout. As-tu triché?"

    return(résultat)

#Bravo, tu es excellent, tu as eu 100% partout. As-tu triché?                        7
#Excellent résultat, tu connais très bien ta matière.                                6
#Tu y es presque. Tu n'as fait que quelque erreurs                                   5
#Tu comprends bien ces catégories. Il ne te reste qu'a réviser cette catégorie       4
#En général, tu comprends bien, mais tu fais des erreurs dans ces catégories         3
#Tu fais beacoup d'erreur dans ces catégories, je te conseil de réviser              2
#Prends-tu le test au serieux!!!                                                     1