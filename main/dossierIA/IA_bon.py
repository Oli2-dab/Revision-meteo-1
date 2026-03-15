#   Ceci est un code pour créer une ia qui propose des recommandation basé sur les bonnes ou mauvaise réponse d'un questionnaire
#   Pour le cours de philo 2 Cchic
#   Questions basées sur les notes de cours personnelles de météo 1 du CQFA
#
#   Olivier Moreau
#

import streamlit as st
from dossierIA.IA import prédiction

st.session_state.sjavanthumidité = st.text_input("sjavanthumidité")
st.session_state.tavanthumidité = st.text_input("tavanthumidité")
st.session_state.sjavantréchauffement = st.text_input("sjavantréchauffement")
st.session_state.tavantréchauffement = st.text_input("tavantréchauffement")
st.session_state.sjavantrefroidissement = st.text_input("sjavantrefroidissement")
st.session_state.tavantrefroidissement = st.text_input("tavantrefroidissement")
st.session_state.sjavantstabilite_air = st.text_input("sjstabilite_air")
st.session_state.tavantstabilite_air = st.text_input("tstabilite_air")
st.session_state.sjavantpression_atmo = st.text_input("sjpression_atmo")
st.session_state.tavantpression_atmo = st.text_input("tpression_atmo")
st.session_state.sjavantmasse_air = st.text_input("sjmasse_air")
st.session_state.tavantmasse_air = st.text_input("tmasse_air")
st.session_state.sjavantfronts = st.text_input("sjfronts")
st.session_state.tavantfronts = st.text_input("tfronts")
st.session_state.sjavantnuage_precipitation = st.text_input("sjnuage_precipitation")
st.session_state.tavantnuage_precipitation = st.text_input("tnuage_precipitation")



if st.button("IA") :
    
    scorecat = {
        "humidite": int(st.session_state.sjavanthumidité),
        "rechauffement": int(st.session_state.sjavantréchauffement),
        "refroidissement": int(st.session_state.sjavantrefroidissement),
        "stabilite": int(st.session_state.sjavantstabilite_air),
        "pression": int(st.session_state.sjavantpression_atmo),
        "masse": int(st.session_state.sjavantmasse_air),
        "front": int(st.session_state.sjavantfronts),
        "nuage": int(st.session_state.sjavantnuage_precipitation),
    }

    totalcat = {
        "humidite": int(st.session_state.tavanthumidité),
        "rechauffement": int(st.session_state.tavantréchauffement),
        "refroidissement": int(st.session_state.tavantrefroidissement),
        "stabilite": int(st.session_state.tavantstabilite_air),
        "pression": int(st.session_state.tavantpression_atmo),
        "masse": int(st.session_state.tavantmasse_air),
        "front": int(st.session_state.tavantfronts),
        "nuage": int(st.session_state.tavantnuage_precipitation),
    }

    st.session_state.scorecat = scorecat
    st.session_state.totalcat = totalcat

    résultat_IA = prédiction()
    st.success(résultat_IA)