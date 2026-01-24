#   Ceci est un code pour créer une ia qui propose des recommandation basé sur les bonnes ou mauvaise réponse d'un questionnaire
#   Pour le cours de philo 2 Cchic
#   Questions basées sur les notes de cours personnelles de météo 1 du CQFA
#
#   Olivier Moreau
#

import streamlit as st
import random
from question import bqhumidité
from question import bqréchauffement
from question import bqrefroidissement
from main.extension.chargement_spacy import charger_spacy

if "index" not in st.session_state:
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.theme = "rien"
    st.session_state.question = "rien"
    st.session_state.sàenlevé = 0
    st.session_state.rj = "rien"
    st.session_state.rjeu = "rien"
    st.session_state.validité = 0  
    st.session_state.scoreq = 0

if "sjhumidité" not in st.session_state:
    st.session_state.sjhumidité = 0

if "sjréchauffement" not in st.session_state:
    st.session_state.sjréchauffement = 0 

if "sjrefroidissement" not in st.session_state:
    st.session_state.sjrefroidissement = 0

if "qdscore" not in st.session_state:
    st.session_state.qdscore = {}

if "thumidité" not in st.session_state:
    st.session_state.thumidité = 0

if "tréchauffement" not in st.session_state:
    st.session_state.tréchauffement = 0

if "trefroidissement" not in st.session_state:
    st.session_state.trefroidissement = 0

if "qactuel" not in st.session_state :
    st.session_state.qactuel = None

val = charger_spacy()

def valrép(rj, rjeu) :
    réponse_joueur = rj.strip().lower()
    réponse_jeu = rjeu.strip().lower()

    pourvalrj = val(réponse_jeu)
    pourvalrjeu = val(réponse_joueur)
    validité = pourvalrj.similarity(pourvalrjeu)

    if validité >= 0.80 :
        scoreq = 2

    elif validité >= 0.40 :
        scoreq = 1
    
    else :
        scoreq = 0.0

    if réponse_joueur == "c2" :
        scoreq = 2

    if réponse_joueur == "c1" :
        scoreq = 1

    if réponse_joueur == "c0" :
        scoreq = 0

    return(scoreq)

def choix_question() :
    choix_thème = random.randint(1,3)


    if choix_thème == 1 :

        theme = "humidité"

        choixq = random.randint(0, len(bqjeuhumidité) - 1)

        question = bqjeuhumidité[choixq]["question"]

        rjeu = bqjeuhumidité[choixq]["réponse"]

        bqjeuhumidité.pop(choixq)

    elif choix_thème == 2 :

        theme = "réchauffement"

        choixq = random.randint(0, len(bqjeuréchauffement) - 1)

        question = bqjeuréchauffement[choixq]["question"]

        rjeu = bqjeuréchauffement[choixq]["réponse"]

        bqjeuréchauffement.pop(choixq)

    elif choix_thème == 3 :

        theme = "refroidissement"

        choixq = random.randint(0, len(bqjeurefroidissement) - 1)

        question = bqjeurefroidissement[choixq]["question"]

        rjeu = bqjeurefroidissement[choixq]["réponse"]

        bqjeurefroidissement.pop(choixq)

    return(question, rjeu, theme)

print("Bonjour et bienvenu à ce jeu questionnaire.")
qrépondu = 0

bqjeuhumidité = []
bqjeuréchauffement = []
bqjeurefroidissement = []

bqjeuhumidité.extend(bqhumidité)
bqjeuréchauffement.extend(bqréchauffement)
bqjeurefroidissement.extend(bqrefroidissement)

nbquestion = len(bqhumidité) + len(bqréchauffement) + len(bqrefroidissement)

if st.session_state.index < nbquestion:
    st.subheader(f"Question {st.session_state.index + 1} sur {nbquestion}")

    if st.session_state.qactuel == None :
        st.session_state.qactuel = choix_question()
    question, rjeu, theme = st.session_state.qactuel

    st.write(question)
    rj = st.text_input("Votre réponse")

    if st.button("Valider la réponse") :
        scoreq = valrép(rj, rjeu)
        score = scoreq
        st.session_state.score += score

        if scoreq == 2 :

            st.success("Bonne réponse! ✅")

        elif scoreq == 1 :

            st.warning(f"Réponse incomplète. La bonne réponse était {rjeu}")

        elif scoreq == 0 :

            st.error(f"Mauvaise réponse. La bonne réponse était {rjeu}")

        if theme == "humidité" :
            if question in st.session_state.qdscore :
                sàenlevé = int(st.session_state.qdscore.get(question))
                st.session_state.sjhumidité -= sàenlevé
                st.session_state.sjhumidité += scoreq
                st.session_state.qdscore.update({question : scoreq})
                
            
            elif question not in st.session_state.qdscore :
                st.session_state.qdscore.update({question : scoreq})
                st.session_state.thumidité += 2
                st.session_state.sjhumidité += scoreq


        elif theme == "réchauffement" :
            if question in st.session_state.qdscore :
                sàenlevé = int(st.session_state.qdscore.get(question))
                st.session_state.sjréchauffement -= sàenlevé
                st.session_state.sjréchauffement += scoreq
                st.session_state.qdscore.update({question : scoreq})
                
            
            elif question not in st.session_state.qdscore :
                st.session_state.qdscore.update({question : scoreq})
                st.session_state.tréchauffement += 2
                st.session_state.sjréchauffement += scoreq


        elif theme == "refroidissement" :
            if question in st.session_state.qdscore :
                sàenlevé = int(st.session_state.qdscore.get(question))
                st.session_state.sjrefroidissement -= sàenlevé
                st.session_state.sjrefroidissement += scoreq
                st.session_state.qdscore.update({question : scoreq})
                
            
            elif question not in st.session_state.qdscore :
                st.session_state.qdscore.update({question : scoreq})
                st.session_state.trefroidissement += 2
                st.session_state.sjrefroidissement += scoreq

        st.session_state.qactuel = None

        st.session_state.index += 1

else :
    st.success("Bravo! Vous avez terminer ce quiz.")