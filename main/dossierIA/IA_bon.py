#   Ceci est un code pour créer une ia qui propose des recommandation basé sur les bonnes ou mauvaise réponse d'un questionnaire
#   Pour le cours de philo 2 Cchic
#   Questions basées sur les notes de cours personnelles de météo 1 du CQFA
#
#   Olivier Moreau
#

import streamlit as st
from dossierIA.IA import prédiction

st.session_state.sjavanthumidité = int(st.text_input("sjavanthumidité"))
st.session_state.tavanthumidité = st.text_input("tavanthumidité")
st.session_state.sjavantréchauffement = st.text_input("sjavantréchauffement")
st.session_state.tavantréchauffement = st.text_input("tavantréchauffement")
st.session_state.sjavantrefroidissement = st.text_input("sjavantrefroidissement")
st.session_state.tavantrefroidissement = st.text_input("tavantrefroidissement")
st.session_state.sjstabilite_air = st.text_input("sjstabilite_air")
st.session_state.tstabilite_air = st.text_input("tstabilite_air")
st.session_state.sjpression_atmo = st.text_input("sjpression_atmo")
st.session_state.tpression_atmo = st.text_input("tpression_atmo")
st.session_state.sjmasse_air = st.text_input("sjmasse_air")
st.session_state.tmasse_air = st.text_input("tmasse_air")
st.session_state.sjfronts = st.text_input("sjfronts")
st.session_state.tfronts = st.text_input("tfronts")
st.session_state.sjnuage_precipitation = st.text_input("sjnuage_precipitation")
st.session_state.tnuage_precipitation = st.text_input("tnuage_precipitation")



if st.button("IA") :
    st.session_state.sjhumidité = int(st.session_state.sjavanthumidité)
    st.session_state.thumidité = int(st.session_state.tavanthumidité)
    st.session_state.sjréchauffement = int(st.session_state.sjavantréchauffement)
    st.session_state.tréchauffement = int(st.session_state.tavantréchauffement)
    st.session_state.sjrefroidissement = int(st.session_state.sjavantrefroidissement)
    st.session_state.trefroidissement = int(st.session_state.tavantrefroidissement)
    
    résultat_IA = prédiction()
    st.success(résultat_IA)