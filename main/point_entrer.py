#   Ceci est un code pour créer une ia qui propose des recommandation basé sur les bonnes ou mauvaise réponse d'un questionnaire
#   Pour le cours de philo 2 Cchic
#   Questions basées sur les notes de cours personnelles de météo 1 du CQFA
#
#   Olivier Moreau
#


#Plan
#Banque des questions avec plusieurs questions pour chauqe sujet (dans q1, il y a 4 questions formulées différemment)
#La prochaine fois, l'utilisateur peut choisir de faire les questions peut importe les catégories ou plus accé sur leurs difficulté.
#Ajouté un mode pour des cartes aide mémoire
#Chaque question a un % pour le score 0, 1, 2 personalisé
#Mode pour avoir des questions d'un seul chapitre
#Mode pour les questions de math
#Faire quelque chose si le joueur fait les questions par catégorie, car certains taux seront 0/0. Division par 0 = impossible et mauvaise interprétation. Mettre taux à None?
#Faire une page pour décoder les métars
#Faire une page pour les abréviations
#Faire un autre score : 0, 1, 2, 3 ou lieu de 0, 1, 2
#Faire une page pour les questions à choix multiple
#Entrainé l'IA pour que si le score est de 0, elle ne le prennent pas en compte : changer fichier d'entrainement



import streamlit as st

st.set_page_config(page_title="Révision météo 1")

navigation = st.navigation([
    st.Page("pages/accueil.py", title = "Page d'accueil"),
    st.Page("pages/jeu_questionnaire.py", title = "Questionnaire complet"),
    st.Page("pages/température.py", title = "Questionnaire température"),
    st.Page("dossierIA/IA_bon.py", title = "Bonne IA"),
    st.Page("dossierIA/IA_mauvais.py", title = "Mauvaise IA")
])

navigation.run()