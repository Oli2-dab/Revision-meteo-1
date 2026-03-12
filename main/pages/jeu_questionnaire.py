#   Ceci est un code pour créer une ia qui propose des recommandation basé sur les bonnes ou mauvaise réponse d'un questionnaire
#   Pour le cours de philo 2 Cchic
#   Questions basées sur les notes de cours personnelles de météo 1 du CQFA
#
#   Olivier Moreau
#

import streamlit as st
import random
from question import bqhumidité, bqréchauffement, bqrefroidissement, stabilite_air, pression_atmo, masse_air, fronts, nuage_precipitation
from extension.chargement_spacy import charger_spacy
from dossierIA.IA import prédiction

def principale() : 

    if "rénitialization_jeu" not in st.session_state :
        st.session_state.rénitialization_jeu = True

        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.qactuel = None
        st.session_state.répval = False

        st.session_state.bqjeuhumidité = bqhumidité.copy()
        st.session_state.bqjeuréchauffement = bqréchauffement.copy()
        st.session_state.bqjeurefroidissement = bqrefroidissement.copy()
        st.session_state.bqstabilite_air = stabilite_air.copy()
        st.session_state.bqpression_atmo = pression_atmo.copy()
        st.session_state.bqmasse_air = masse_air.copy()
        st.session_state.bqfronts = fronts.copy()
        st.session_state.bqnuage_precipitation = nuage_precipitation.copy()

    if "scoreq" not in st.session_state :
        st.session_state.scoreq = 0

    if "sjhumidité" not in st.session_state:
        st.session_state.sjhumidité = 0

    if "sjréchauffement" not in st.session_state:
        st.session_state.sjréchauffement = 0 

    if "sjrefroidissement" not in st.session_state:
        st.session_state.sjrefroidissement = 0
    
    if "sjstabilite_air" not in st.session_state:
        st.session_state.sjstabilite_air = 0

    if "sjpression_atmo" not in st.session_state:
        st.session_state.sjpression_atmo = 0

    if "sjmasse_air" not in st.session_state:
        st.session_state.sjmasse_air = 0

    if "sjfronts" not in st.session_state:
        st.session_state.sjfronts = 0

    if "sjnuage_precipitation" not in st.session_state:
        st.session_state.sjnuage_precipitation = 0

    if "qdscore" not in st.session_state:
        st.session_state.qdscore = {}

    if "thumidité" not in st.session_state:
        st.session_state.thumidité = 0

    if "tréchauffement" not in st.session_state:
        st.session_state.tréchauffement = 0

    if "trefroidissement" not in st.session_state:
        st.session_state.trefroidissement = 0

    if "tstabilite_air" not in st.session_state:
        st.session_state.tstabilite_air = 0

    if "tpression_atmo" not in st.session_state:
        st.session_state.tpression_atmo = 0

    if "tmasse_air" not in st.session_state:
        st.session_state.tmasse_air = 0

    if "tfronts" not in st.session_state:
        st.session_state.tfronts = 0

    if "tnuage_precipitation" not in st.session_state:
        st.session_state.tnuage_precipitation = 0

    if "qactuel" not in st.session_state :
        st.session_state.qactuel = None

    if "répval" not in st.session_state :
        st.session_state.répval = False

    val = charger_spacy()

    if st.session_state.rénitialization_jeu == False :
        st.session_state.rénitialization_jeu = True

        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.qactuel = None
        st.session_state.répval = False

        st.session_state.bqjeuhumidité = bqhumidité.copy()
        st.session_state.bqjeuréchauffement = bqréchauffement.copy()
        st.session_state.bqjeurefroidissement = bqrefroidissement.copy()
        st.session_state.bqstabilite_air = stabilite_air.copy()
        st.session_state.bqpression_atmo = pression_atmo.copy()
        st.session_state.bqmasse_air = masse_air.copy()
        st.session_state.bqfronts = fronts.copy()
        st.session_state.bqnuage_precipitation = nuage_precipitation.copy()

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

        if len(st.session_state.bqstabilite_air) > 0 :
            tdispo.append("stabilite_de_l_air")

        if len(st.session_state.bqpression_atmo) > 0 :
            tdispo.append("pression_atmospherique")

        if len(st.session_state.bqmasse_air) > 0 :
            tdispo.append("masse_d_air")

        if len(st.session_state.bqfronts) > 0 :
            tdispo.append("les_fronts")

        if len(st.session_state.bqnuage_precipitation) > 0 :
            tdispo.append("nuage_et_precipitation")

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

        elif theme == "stabilite_de_l_air" :

            choixq = random.randint(0, len(st.session_state.bqstabilite_air) - 1)

            question = st.session_state.bqstabilite_air[choixq]["question"]

            rjeu = st.session_state.bqstabilite_air[choixq]["réponse"]

            st.session_state.bqstabilite_air.pop(choixq)

        elif theme == "pression_atmospherique" :

            choixq = random.randint(0, len(st.session_state.bqpression_atmo) - 1)

            question = st.session_state.bqpression_atmo[choixq]["question"]

            rjeu = st.session_state.bqpression_atmo[choixq]["réponse"]

            st.session_state.bqpression_atmo.pop(choixq)
        
        elif theme == "masse_d_air" :

            choixq = random.randint(0, len(st.session_state.bqmasse_air) - 1)

            question = st.session_state.bqmasse_air[choixq]["question"]

            rjeu = st.session_state.bqmasse_air[choixq]["réponse"]

            st.session_state.bqmasse_air.pop(choixq)

        elif theme == "les_fronts" :

            choixq = random.randint(0, len(st.session_state.bqfronts) - 1)

            question = st.session_state.bqfronts[choixq]["question"]

            rjeu = st.session_state.bqfronts[choixq]["réponse"]

            st.session_state.bqfronts.pop(choixq)

        elif theme == "nuage_et_precipitation" :

            choixq = random.randint(0, len(st.session_state.bqnuage_precipitation) - 1)

            question = st.session_state.bqnuage_precipitation[choixq]["question"]

            rjeu = st.session_state.bqnuage_precipitation[choixq]["réponse"]

            st.session_state.bqnuage_precipitation.pop(choixq)

        return(question, rjeu, theme)

    nbquestion = len(bqhumidité) + len(bqréchauffement) + len(bqrefroidissement) + len(stabilite_air) + len(pression_atmo) + len(masse_air) + len(fronts) + len(nuage_precipitation)

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
                st.session_state.score = st.session_state.scoreq
                st.session_state.score += st.session_state.score

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


                elif theme == "stabilite_de_l_air" :
                    if question in st.session_state.qdscore :
                        sàenlevé = int(st.session_state.qdscore.get(question))
                        st.session_state.sjstabilite_air -= sàenlevé
                        st.session_state.sjstabilite_air += st.session_state.scoreq
                        st.session_state.qdscore.update({question : st.session_state.scoreq})
                        
                    
                    elif question not in st.session_state.qdscore :
                        st.session_state.qdscore.update({question : st.session_state.scoreq})
                        st.session_state.tstabilite_air += 2
                        st.session_state.sjstabilite_air += st.session_state.scoreq


                elif theme == "pression_atmospherique" :
                    if question in st.session_state.qdscore :
                        sàenlevé = int(st.session_state.qdscore.get(question))
                        st.session_state.sjpression_atmo -= sàenlevé
                        st.session_state.sjpression_atmo += st.session_state.scoreq
                        st.session_state.qdscore.update({question : st.session_state.scoreq})
                        
                    
                    elif question not in st.session_state.qdscore :
                        st.session_state.qdscore.update({question : st.session_state.scoreq})
                        st.session_state.tpression_atmo += 2
                        st.session_state.sjpression_atmo += st.session_state.scoreq


                elif theme == "masse_d_air" :
                    if question in st.session_state.qdscore :
                        sàenlevé = int(st.session_state.qdscore.get(question))
                        st.session_state.sjmasse_air -= sàenlevé
                        st.session_state.sjmasse_air += st.session_state.scoreq
                        st.session_state.qdscore.update({question : st.session_state.scoreq})
                        
                    
                    elif question not in st.session_state.qdscore :
                        st.session_state.qdscore.update({question : st.session_state.scoreq})
                        st.session_state.tmasse_air += 2
                        st.session_state.sjmasse_air += st.session_state.scoreq


                elif theme == "les_fronts" :
                    if question in st.session_state.qdscore :
                        sàenlevé = int(st.session_state.qdscore.get(question))
                        st.session_state.sjfronts -= sàenlevé
                        st.session_state.sjfronts += st.session_state.scoreq
                        st.session_state.qdscore.update({question : st.session_state.scoreq})
                        
                    
                    elif question not in st.session_state.qdscore :
                        st.session_state.qdscore.update({question : st.session_state.scoreq})
                        st.session_state.tfronts += 2
                        st.session_state.sjfronts += st.session_state.scoreq


                elif theme == "nuage_et_precipitation" :
                    if question in st.session_state.qdscore :
                        sàenlevé = int(st.session_state.qdscore.get(question))
                        st.session_state.sjnuage_precipitation -= sàenlevé
                        st.session_state.sjnuage_precipitation += st.session_state.scoreq
                        st.session_state.qdscore.update({question : st.session_state.scoreq})
                        
                    
                    elif question not in st.session_state.qdscore :
                        st.session_state.qdscore.update({question : st.session_state.scoreq})
                        st.session_state.tnuage_precipitationt += 2
                        st.session_state.sjnuage_precipitation += st.session_state.scoreq

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

        total_score = st.session_state.index * 2

        st.success(f"Bravo! Vous avez terminer ce quiz. Votre score est de {st.session_state.score} sur {total_score}.")
        st.success(résultat_IA)
        
        if st.button("Recommenser le questionnaire complet") :
            st.session_state.rénitialization_jeu = False
            st.rerun()

        if st.button("Page d'accueil") :
            st.session_state.rénitialization_jeu = False
            st.switch_page("pages/accueil.py")

principale()