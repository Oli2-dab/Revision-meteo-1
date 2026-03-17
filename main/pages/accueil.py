#   Ceci est un code pour créer une ia qui propose des recommandation basé sur les bonnes ou mauvaise réponse d'un questionnaire
#   Pour le cours de philo 2 Cchic
#   Questions basées sur les notes de cours personnelles de météo 1 du CQFA
#
#   Olivier Moreau
#

import streamlit as st

st.title("Platforme de révision pour le cours de météo 1")
st.write("Choisiez le mode de jeu auquel vous voulez jouer.")

st.write("AVERTISSEMENT")
st.write("Cette platforme est utiliser pour différent projet. Pour la révision de météo, utiliser <<Questionnaire complet>> ou <<Questionnaire avec choix des thèmes>> seulement. Dans la banque de question, il y a 10 questions de l'examen 1. Elle sont présentes pour un autre projet. Vous pouvez toujours essayer d'y répondre.")
st.write("Si vous renconter des erreurs, svp m'écrire pour que je puisse les corrigées pour que les autres ne les rencontres pas.")

if st.button("Questionnaire complet") :
    st.switch_page("pages/jeu_questionnaire.py")

if st.button("Questionnaire avec choix des thèmes") :
    st.switch_page("pages/choix_t_questionnaire.py")

if st.button("Bonne IA") :
    st.switch_page("dossierIA/IA_bon.py")

if st.button("Mauvaise IA") :
    st.switch_page("dossierIA/IA_mauvais.py")

st.write("Version 1.0.39")

st.markdown("""
            -**1.0.39**  
            Mise à jour de l'IA avec le nouveau modèle d'entrainement.  
            -**1.0.38**  
            Correction d'erreurs dans les réponses.  
            -**1.0.37**  
            Correction de bugs avec le nouveau système de réponse.  
            Modification du modèle de langage.  
            -**1.0.23**  
            Modification de l'IA pour ne pas prendre en compte les thèmes s'ils n'ont pas été sélectionnés.  
            Correction d'erreurs dans les réponses.  
            Modification du système de réponse pour que l'utilisateurs ait moins de réponse incomplète s'il met le mauvais déterminant.  
            -**1.0.17**  
            Ajout d'un jeu questionnaire où l'on peut choisir les chapitres que l'on veut réviser.  
            Correction d'erreurs dans les réponses.  
            -**1.0.23**  
            Modification de l'IA pour ne pas prendre en compte les thèmes s'ils n'ont pas été sélectionnés.  
            Correction d'erreurs dans les réponses.  
            Modification du système de réponse pour que l'utilisateurs ait moins de réponse incomplète s'il met le mauvais déterminant.
            """)