#   Ceci est un code pour créer une ia qui propose des recommandation basé sur les bonnes ou mauvaise réponse d'un questionnaire
#   Pour le cours de philo 2 Cchic
#   Questions basées sur les notes de cours personnelles de météo 1 du CQFA
#
#   Olivier Moreau
#

import streamlit as st
import random
from question import categorie
from extension.validation import valrép
from dossierIA.IA import prédiction

def principale() : 

    if "nbquestion" not in st.session_state :
        st.session_state.nbquestion = 0

    if "rénitialization_jeu" not in st.session_state or st.session_state.rénitialization_jeu == False :
        st.session_state.rénitialization_jeu = True

        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.qactuel = None
        st.session_state.répval = False

        st.session_state.bqjeu = []

        for q in categorie.values() :
            st.session_state.bqjeu += q.copy()

        st.session_state.nbquestion = len(st.session_state.bqjeu)

    if "scoreq" not in st.session_state :
        st.session_state.scoreq = 0

    if "qdscore" not in st.session_state:
        st.session_state.qdscore = {}

    if "qactuel" not in st.session_state :
        st.session_state.qactuel = None

    if "répval" not in st.session_state :
        st.session_state.répval = False

    if "scorecat" not in st.session_state :
        st.session_state.scorecat = {}

    if "totalcat" not in st.session_state :
        st.session_state.totalcat = {}

    def choix_question() :

        choixq = random.choice(st.session_state.bqjeu)

        question = choixq["question"]

        rjeu = choixq["réponse"]

        theme = choixq["theme"]

        indice = choixq["indice"]

        st.session_state.bqjeu.remove(choixq)

        return(question, rjeu, theme, indice)

    if st.session_state.index < st.session_state.nbquestion:
        st.subheader(f"Question {st.session_state.index + 1} sur {st.session_state.nbquestion}")

        if st.session_state.qactuel is None :
            st.session_state.qactuel = choix_question()
        question, rjeu, theme, indice = st.session_state.qactuel

        st.write(question)
        rj = st.text_input("Votre réponse", value = indice, key= f"réponse_{st.session_state.index}", disabled = st.session_state.répval)

        if not st.session_state.répval :

            if st.button("Valider la réponse") :
                st.session_state.scoreq = valrép(rj, rjeu, indice)
                st.session_state.score += st.session_state.scoreq

                if theme not in st.session_state.scorecat :
                    st.session_state.scorecat[theme] = 0

                if theme not in st.session_state.totalcat :
                    st.session_state.totalcat[theme] = 0

                if question in st.session_state.qdscore :
                    qancienne = st.session_state.qdscore[question]
                    st.session_state.scorecat[theme] -= qancienne

                else :
                    st.session_state.totalcat[theme] += 2

                st.session_state.scorecat[theme] += st.session_state.scoreq
                st.session_state.qdscore[question] = st.session_state.scoreq

                st.session_state.répval = True
                st.rerun()

        if st.session_state.répval :

            if st.session_state.scoreq == 2 :

                st.success(f"Bonne réponse! ✅ Si tu veux comparer avec la réponse du corrigé, la voici : {rjeu}")

            elif st.session_state.scoreq == 1 :

                st.warning(f"Réponse incomplète. La bonne réponse était : {rjeu}")

            elif st.session_state.scoreq == 0 :

                st.error(f"Mauvaise réponse. La bonne réponse était : {rjeu}")

            if st.button("Question suivante") :

                st.session_state.qactuel = None
                st.session_state.index += 1
                st.session_state.répval = False
                st.rerun()
                    

    else :
        résultat_IA = prédiction()

        total_score = st.session_state.index * 2

        st.subheader("Score par thème")
        for theme, score in st.session_state.scorecat.items():
            st.write(f"{theme}: {score}/{st.session_state.totalcat[theme]}")

        st.success(f"Bravo! Vous avez terminer ce quiz. Votre score est de {st.session_state.score} sur {total_score}.")
        st.success(résultat_IA)
        
        if st.button("Recommenser le questionnaire complet") :
            st.session_state.rénitialization_jeu = False
            st.rerun()

        if st.button("Page d'accueil") :
            st.session_state.rénitialization_jeu = False
            st.switch_page("pages/accueil.py")

principale()