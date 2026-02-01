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
from extension.chargement_spacy import charger_spacy
from dossierIA.IA import prédiction

def principale(reset = False) : 

    if reset :

        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.qactuel = 0

        st.session_state.bqjeuhumidité = bqhumidité.copy()
        st.session_state.bqjeuréchauffement = bqréchauffement.copy()
        st.session_state.bqjeurefroidissement = bqrefroidissement.copy()

        st.session_state.répval = False


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

    if "bqjeuhumidité" not in st.session_state :
        st.session_state.bqjeuhumidité = bqhumidité.copy()

    if "bqjeuréchauffement" not in st.session_state :
        st.session_state.bqjeuréchauffement = bqréchauffement.copy()

    if "bqjeurefroidissement" not in st.session_state :
        st.session_state.bqjeurefroidissement = bqrefroidissement.copy()

    if "répval" not in st.session_state :
        st.session_state.répval = False

    if "tdispo" not in st.session_state :
        st.session_state.tdispo = []

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

        tdispo = []

        if len(st.session_state.bqjeuhumidité) > 0 :
            tdispo.append("humidité")

        if len(st.session_state.bqjeuréchauffement) > 0 :
            tdispo.append("réchauffement")

        if len(st.session_state.bqjeurefroidissement) > 0 :
            tdispo.append("refroidissement")

        theme = random.choice(tdispo)

        if theme == "humidité"  :

            choixq = random.randint(0, len(st.session_state.bqjeuhumidité) - 1)

            question = st.session_state.bqjeuhumidité[choixq]["question"]

            rjeu = st.session_state.bqjeuhumidité[choixq]["réponse"]

            st.session_state.bqjeuhumidité.pop(choixq)

        elif theme == "réchauffement" :

            choixq = random.randint(0, len(st.session_state.bqjeuréchauffement) - 1)

            question = st.session_state.bqjeuréchauffement[choixq]["question"]

            rjeu = st.session_state.bqjeuréchauffement[choixq]["réponse"]

            st.session_state.bqjeuréchauffement.pop(choixq)

        elif theme == "refroidissement" :

            choixq = random.randint(0, len(st.session_state.bqjeurefroidissement) - 1)

            question = st.session_state.bqjeurefroidissement[choixq]["question"]

            rjeu = st.session_state.bqjeurefroidissement[choixq]["réponse"]

            st.session_state.bqjeurefroidissement.pop(choixq)

        return(question, rjeu, theme)

    print("Bonjour et bienvenu à ce jeu questionnaire.")
    qrépondu = 0

    nbquestion = len(bqhumidité) + len(bqréchauffement) + len(bqrefroidissement)

    if st.session_state.index < nbquestion:
        st.subheader(f"Question {st.session_state.index + 1} sur {nbquestion}")

        if st.session_state.qactuel is None :
            st.session_state.qactuel = choix_question()
        question, rjeu, theme = st.session_state.qactuel

        st.write(question)
        rj = st.text_input("Votre réponse", key= f"réponse_{st.session_state.index}", disabled = st.session_state.répval)

        if not st.session_state.répval :

            if st.button("Valider la réponse") :
                st.session_state.scoreq = valrép(rj, rjeu)
                score = st.session_state.scoreq
                st.session_state.score += score

                if theme == "humidité" :
                    if question in st.session_state.qdscore :
                        sàenlevé = int(st.session_state.qdscore.get(question))
                        st.session_state.sjhumidité -= sàenlevé
                        st.session_state.sjhumidité += st.session_state.scoreq
                        st.session_state.qdscore.update({question : st.session_state.scoreq})
                        
                    
                    elif question not in st.session_state.qdscore :
                        st.session_state.qdscore.update({question : st.session_state.scoreq})
                        st.session_state.thumidité += 2
                        st.session_state.sjhumidité += st.session_state.scoreq


                elif theme == "réchauffement" :
                    if question in st.session_state.qdscore :
                        sàenlevé = int(st.session_state.qdscore.get(question))
                        st.session_state.sjréchauffement -= sàenlevé
                        st.session_state.sjréchauffement += st.session_state.scoreq
                        st.session_state.qdscore.update({question : st.session_state.scoreq})
                        
                    
                    elif question not in st.session_state.qdscore :
                        st.session_state.qdscore.update({question : st.session_state.scoreq})
                        st.session_state.tréchauffement += 2
                        st.session_state.sjréchauffement += st.session_state.scoreq


                elif theme == "refroidissement" :
                    if question in st.session_state.qdscore :
                        sàenlevé = int(st.session_state.qdscore.get(question))
                        st.session_state.sjrefroidissement -= sàenlevé
                        st.session_state.sjrefroidissement += st.session_state.scoreq
                        st.session_state.qdscore.update({question : st.session_state.scoreq})
                        
                    
                    elif question not in st.session_state.qdscore :
                        st.session_state.qdscore.update({question : st.session_state.scoreq})
                        st.session_state.trefroidissement += 2
                        st.session_state.sjrefroidissement += st.session_state.scoreq

                st.session_state.répval = True
                st.rerun()

        if st.session_state.répval :

            if st.session_state.scoreq == 2 :

                st.success("Bonne réponse! ✅")

            elif st.session_state.scoreq == 1 :

                st.warning(f"Réponse incomplète. La bonne réponse était {rjeu}")

            elif st.session_state.scoreq == 0 :

                st.error(f"Mauvaise réponse. La bonne réponse était {rjeu}")

            if st.button("Question suivante") :

                st.session_state.qactuel = None
                st.session_state.index += 1
                st.session_state.répval = False
                st.rerun()
                    

    else :
        résultat_IA = prédiction()

        st.success("Bravo! Vous avez terminer ce quiz.")
        st.success(résultat_IA)