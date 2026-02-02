#   Ceci est un code pour créer une ia qui propose des recommandation basé sur les bonnes ou mauvaise réponse d'un questionnaire
#   Pour le cours de philo 2 Cchic
#   Questions basées sur les notes de cours personnelles de météo 1 du CQFA
#
#   Olivier Moreau
#

import streamlit as st
from dossierIA.IA import prédiction

st.session_state.sjhumidité = st.text_input("sjhumidité")
st.session_state.thumidité = st.text_input("thumidité")
st.session_state.sjréchauffement = st.text_input("sjréchauffement")
st.session_state.tréchauffement = st.text_input("tréchauffement")
st.session_state.sjrefroidissement = st.text_input("sjrefroidissement")
st.session_state.trefroidissement = st.text_input("trefroidissement")

st.session_state.sjhumidité = int(st.session_state.sjhumidité)
st.session_state.thumidité = int(st.session_state.thumidité)
st.session_state.sjréchauffement = int(st.session_state.sjréchauffement)
st.session_state.tréchauffement = int(st.session_state.tréchauffement)
st.session_state.sjrefroidissement = int(st.session_state.sjrefroidissement)
st.session_state.trefroidissement = int(st.session_state.trefroidissement)

if st.button("IA") :
    résultat_IA = prédiction()
    st.success(résultat_IA)