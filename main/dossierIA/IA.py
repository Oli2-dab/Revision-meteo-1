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
    résultat = chargement_model.predict(taux)

    return(résultat)