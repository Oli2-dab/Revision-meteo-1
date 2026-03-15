#   Ceci est un code pour créer une ia qui propose des recommandation basé sur les bonnes ou mauvaise réponse d'un questionnaire
#   Pour le cours de philo 2 Cchic
#   Questions basées sur les notes de cours personnelles de météo 1 du CQFA
#
#   Olivier Moreau
#

import streamlit as st
import joblib
import pandas as pd

@st.cache_resource
def chargement_IA() :
    return joblib.load("base_de_donnee_IA.joblib")

def prédiction() :

    scorecat = st.session_state.scorecat
    totalcat = st.session_state.totalcat
    taux_theme = {}

    for t in totalcat :

        if totalcat[t] == 0 :
            taux_theme[t] = 0

        else :
            taux_theme[t] = round(scorecat.get(t, 0) / totalcat[t], 2)

    taux_hum = taux_theme.get("humidite", 0)

    taux_réch = taux_theme.get("rechauffement", 0)

    taux_refr = taux_theme.get("refroidissement", 0)

    taux_stab = taux_theme.get("stabilite", 0)

    taux_pres = taux_theme.get("pression", 0)

    taux_mass = taux_theme.get("masse", 0)

    taux_fron = taux_theme.get("front", 0)

    taux_nuag = taux_theme.get("nuage", 0)

    model = chargement_IA()
    taux = pd.DataFrame([[taux_hum,taux_réch,taux_refr,taux_stab,taux_pres,taux_mass,taux_fron,taux_nuag]], columns = ["taux_humidité", "taux_réchauffement", "taux_refroidissement", "taux_stabilite", "taux_pression", "taux_masse", "taux_front", "taux_nuage"])
    résultat_taux = model.predict(taux)[0]

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

    catégorie_affiché = min(dict_taux, key = dict_taux.get)

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

#Bravo, tu es excellent, tu as eu 100% partout. As-tu triché?                        7
#Excellent résultat, tu connais très bien ta matière.                                6
#Tu y es presque. Tu n'as fait que quelque erreurs                                   5
#Tu comprends bien ces catégories. Il ne te reste qu'a réviser cette catégorie       4
#En général, tu comprends bien, mais tu fais des erreurs dans ces catégories         3
#Tu fais beacoup d'erreur dans ces catégories, je te conseil de réviser              2
#Prends-tu le test au serieux!!!                                                     1