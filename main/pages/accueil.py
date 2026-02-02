#   Ceci est un code pour créer une ia qui propose des recommandation basé sur les bonnes ou mauvaise réponse d'un questionnaire
#   Pour le cours de philo 2 Cchic
#   Questions basées sur les notes de cours personnelles de météo 1 du CQFA
#
#   Olivier Moreau
#

import streamlit as st

st.title("Platforme de révision pour le cours de météo 1")
st.write("Choisiez le mode de jeu auquel vous voulez jouer.")

if st.button("Questionnaire complet") :
    st.switch_page("pages/jeu_questionnaire.py")

if st.button("Questionnaire température") :
    st.switch_page("pages/température.py")