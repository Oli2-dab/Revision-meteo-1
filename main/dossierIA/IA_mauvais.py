#   Ceci est un code pour créer une ia qui propose des recommandation basé sur les bonnes ou mauvaise réponse d'un questionnaire
#   Pour le cours de philo 2 Cchic
#   Questions basées sur les notes de cours personnelles de météo 1 du CQFA
#
#   Olivier Moreau
#

import streamlit as st
import joblib
import pandas as pd

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

def prédiction_mauvais() :

    scorecat = st.session_state.scorecat
    totalcat = st.session_state.totalcat
    taux_theme = {}

    for t in totalcat :

        if totalcat[t] == 0 :
            taux_theme[t] = 0

        else :
            taux_theme[t] = round(scorecat.get(t, 0) / totalcat[t], 2)

    taux_hum = taux_theme.get("humidite", 2)

    taux_réch = taux_theme.get("rechauffement", 2)

    taux_refr = taux_theme.get("refroidissement", 2)

    taux_stab = taux_theme.get("stabilite", 2)

    taux_pres = taux_theme.get("pression", 2)

    taux_mass = taux_theme.get("masse", 2)

    taux_fron = taux_theme.get("front", 2)

    taux_nuag = taux_theme.get("nuage", 2)

    chargement_model = joblib.load("base_de_donnee_IA_mauvais.joblib")
    taux = pd.DataFrame([[taux_hum,taux_réch,taux_refr,taux_stab,taux_pres,taux_mass,taux_fron,taux_nuag]], columns = ["taux_humidité", "taux_réchauffement", "taux_refroidissement", "taux_stabilite", "taux_pression", "taux_masse", "taux_front", "taux_nuage"])
    résultat_taux = chargement_model.predict(taux)[0]

    dict_taux = {
        "l'humidité" : taux_hum,
        "le réchauffement" : taux_réch,
        "le refroidissement" : taux_refr,
        "la stabilité de l'air" : taux_stab,
        "la pression atmosphérique" : taux_pres,
        "les masses d'air" : taux_mass,
        "les fronts" : taux_fron,
        "les nuages et les précipitations" : taux_nuag,
    }

    dict_taux_filtré = {theme: nom_taux for theme, nom_taux in dict_taux.items() if nom_taux != 2}

    catégorie_affiché = min(dict_taux_filtré, key=dict_taux_filtré.get)

    if résultat_taux == 1 :
        résultat = f"Prends-tu le test au serieux!!!"

    elif résultat_taux == 2 :
        résultat = f"Tu fais beaucoup d'erreur dans plusieurs catégories. Je te conseil de réviser le chapitre sur {catégorie_affiché} car c'est dans cette catégorie que tu fais le plus d'erreurs."

    elif résultat_taux == 3 :
        résultat = f"En général, tu comprends bien, mais tu fais plusieurs erreurs. Je te conseil de réviser le chapitre sur {catégorie_affiché} car c'est dans cette catégorie que tu fais le plus d'erreurs."

    elif résultat_taux == 4 :
        résultat = f"Tu comprends bien la matière dans presque toutes les catégories. Il ne te reste qu'a réviser le chapitre sur {catégorie_affiché}."

    elif résultat_taux == 5 :
        résultat = f"Tu y es presque. Tu n'as fait que quelque erreurs"

    elif résultat_taux == 6 :
        résultat = f"Excellent résultat, tu connais très bien ta matière."

    elif résultat_taux == 7 :
        résultat = f"Bravo, tu es excellent, tu as presque eu 100% partout. As-tu triché?"

    return(résultat)

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

    résultat_IA = prédiction_mauvais()
    st.success(résultat_IA)