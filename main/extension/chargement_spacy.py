#   Ceci est un code pour créer une ia qui propose des recommandation basé sur les bonnes ou mauvaise réponse d'un questionnaire
#   Pour le cours de philo 2 Cchic
#   Questions basées sur les notes de cours personnelles de météo 1 du CQFA
#
#   Olivier Moreau
#

import streamlit as st
import spacy

@st.cache_resource
def charger_spacy() :
    try :
        val = spacy.load("fr_core_news_sm")
    except OSError :
        spacy.cli.download("fr_core_news_sm")
        val = spacy.load("fr_core_news_sm")
    return(val)