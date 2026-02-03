#   Ceci est un code pour créer une ia qui propose des recommandation basé sur les bonnes ou mauvaise réponse d'un questionnaire
#   Pour le cours de philo 2 Cchic
#   Questions basées sur les notes de cours personnelles de météo 1 du CQFA
#
#   Olivier Moreau
#

import streamlit as st
from IA import prédiction

st.session_state.sjavanthumidité = st.text_input("sjavanthumidité")
st.session_state.tavanthumidité = st.text_input("tavanthumidité")
st.session_state.sjavantréchauffement = st.text_input("sjavantréchauffement")
st.session_state.tavantréchauffement = st.text_input("tavantréchauffement")
st.session_state.sjavantrefroidissement = st.text_input("sjavantrefroidissement")
st.session_state.tavantrefroidissement = st.text_input("tavantrefroidissement")



if st.button("IA") :
    st.session_state.sjhumidité = int(st.session_state.sjavanthumidité)
    st.session_state.thumidité = int(st.session_state.tavanthumidité)
    st.session_state.sjréchauffement = int(st.session_state.sjavantréchauffement)
    st.session_state.tréchauffement = int(st.session_state.tavantréchauffement)
    st.session_state.sjrefroidissement = int(st.session_state.sjavantrefroidissement)
    st.session_state.trefroidissement = int(st.session_state.tavantrefroidissement)
    
    résultat_IA = prédiction()
    st.success(résultat_IA)