#   Ceci est un code pour créer une ia qui propose des recommandation basé sur les bonnes ou mauvaise réponse d'un questionnaire
#   Pour le cours de philo 2 Cchic
#   Questions basées sur les notes de cours personnelles de météo 1 du CQFA
#
#   Olivier Moreau
#

import streamlit as st
import random
from question import bqhumidité, bqréchauffement, bqrefroidissement, stabilite_air, pression_atmo, masse_air, fronts, nuage_precipitation
from extension.validation import valrép
from dossierIA.IA import prédiction

initialization = {
    "scoreq_ctq":0,
    "qdscore":{},
    "qactuel_ctq":None,
    "répval_ctq":False,
    "scorecat":{},
    "totalcat":{},
    "nbquestion_ctq":0,
    "rénitialization_ctq":False,
    "index_ctq":0,
    "score_ctq":0,
    "bqjeu_ctq":[]
}

for nom, valeur in initialization.items() :
    if nom not in st.session_state :
        st.session_state[nom] = valeur

def choix_question() :

        choixq_ctq = random.choice(st.session_state.bqjeu_ctq)

        question = choixq_ctq["question"]

        rjeu = choixq_ctq["réponse"]

        theme = choixq_ctq["theme"]

        indice = choix_ctq["indice"]

        st.session_state.bqjeu_ctq.remove(choixq_ctq)

        return(question, rjeu, theme, indice)

def choix_ctq() :

    st.session_state.index_ctq = 0
    st.session_state.score_ctq = 0
    st.session_state.qactuel_ctq = None
    st.session_state.répval_ctq = False

    st.session_state.bqjeu_ctq = []
    theme_dispo_ctq = {
        "humidite" : ("l'humidité", bqhumidité),
        "rechauffement" : ("le réchauffement", bqréchauffement),
        "refroidissement" : ("le refroidissement", bqrefroidissement),
        "stabilite" : ("la stabilité de l'air", stabilite_air),
        "pression" : ("la pression atmosphérique", pression_atmo),
        "masse" : ("les masses d'air", masse_air),
        "front" : ("les fronts", fronts),
        "nuage" : ("les nuages et les précipitations", nuage_precipitation),
    }

    for t_ctq, (label_ctq, _) in theme_dispo_ctq.items() :
        st.checkbox(label_ctq, key = f"theme_{t_ctq}")

    if st.button("Débuter le questionnaire") :
        for t_ctq in theme_dispo_ctq.keys():
            if st.session_state[f"theme_{t_ctq}"] :
                st.session_state.bqjeu_ctq += theme_dispo_ctq[t_ctq][1]

        if not st.session_state.bqjeu_ctq:
            st.warning("Veuillez sélectionner des thèmes")
            return
        
        st.session_state.nbquestion_ctq = len(st.session_state.bqjeu_ctq)
        st.session_state.rénitialization_ctq = True
        st.rerun()

def jeu_ctq() :

    st.subheader(f"Question {st.session_state.index_ctq + 1} sur {st.session_state.nbquestion_ctq}")

    if st.session_state.qactuel_ctq is None :
        st.session_state.qactuel_ctq = choix_question()
    question, rjeu, theme, indice = st.session_state.qactuel_ctq

    st.write(question)
    rj = st.text_input("Votre réponse", value = indice, key= f"réponse_{st.session_state.index_ctq}", disabled = st.session_state.répval_ctq)

    if not st.session_state.répval_ctq :

        if st.button("Valider la réponse") :
            st.session_state.scoreq_ctq = valrép(rj, rjeu)
            st.session_state.score_ctq += st.session_state.scoreq_ctq

            if theme not in st.session_state.scorecat :
                st.session_state.scorecat[theme] = 0

            if theme not in st.session_state.totalcat :
                st.session_state.totalcat[theme] = 0

            if question in st.session_state.qdscore :
                qancienne = st.session_state.qdscore[question]
                st.session_state.scorecat[theme] -= qancienne

            else :
                st.session_state.totalcat[theme] += 2

            st.session_state.scorecat[theme] += st.session_state.scoreq_ctq
            st.session_state.qdscore[question] = st.session_state.scoreq_ctq

            st.session_state.répval_ctq = True
            st.rerun()

    if st.session_state.répval_ctq :

        if st.session_state.scoreq_ctq == 2 :

            st.success("Bonne réponse! ✅")

        elif st.session_state.scoreq_ctq == 1 :

            st.warning(f"Réponse incomplète. La bonne réponse était {rjeu}")

        elif st.session_state.scoreq_ctq == 0 :

            st.error(f"Mauvaise réponse. La bonne réponse était {rjeu}")

        if st.button("Question suivante") :

            st.session_state.qactuel_ctq = None
            st.session_state.index_ctq += 1
            st.session_state.répval_ctq = False
            st.rerun()

def resultat_ctq() :

    résultat_IA = prédiction()

    total_score_ctq = st.session_state.index_ctq * 2

    st.subheader("Score par thème")
    for theme, score in st.session_state.scorecat.items():
        st.write(f"{theme}: {score}/{st.session_state.totalcat[theme]}")

    st.success(f"Bravo! Vous avez terminer ce quiz. Votre score est de {st.session_state.score_ctq} sur {total_score_ctq}.")
    st.success(résultat_IA)
    
    if st.button("Recommenser le questionnaire") :
        st.session_state.rénitialization_ctq = False
        st.rerun()

    if st.button("Page d'accueil") :
        st.session_state.rénitialization_ctq = False
        st.switch_page("pages/accueil.py")



if st.session_state.rénitialization_ctq == False :
    choix_ctq()

elif st.session_state.rénitialization_ctq == True and st.session_state.index_ctq < st.session_state.nbquestion_ctq :
    jeu_ctq()

else :
    resultat_ctq()