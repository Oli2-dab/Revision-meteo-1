#   Ceci est un code pour créer une ia qui propose des recommandation basé sur les bonnes ou mauvaise réponse d'un questionnaire
#   Pour le cours de philo 2 Cchic
#   Questions basées sur les notes de cours personnelles de météo 1 du CQFA
#
#   Olivier Moreau
#


#Plan
#Banque des questions avec plusieurs questions pour chauqe sujet (dans q1, il y a 4 questions formulées différemment)
#Le score de chaque thème est initiallement de 0/0
#Si il donne une bonne réponse, +2, si il donne une réponse partielle, +1, si il donne une mauvaise réponse, +0. Mais le total pour la catégorie fait toujours +2
#À la fin, le code compare le résultat de chaque catégorie et émmet des recommendations
#La prochaine fois, l'utilisateur peut choisir de faire les questions peut importe les catégories ou plus accé sur leurs difficulté.
#Les questions sont choisis aléatoirement, et pour éviter la répétitions, le variable, q1, q2, etc est stoké dans une liste et cette liste est vérifier si la varible choisit n'est pas dans la liste
#Mettre une valeur qui donne une bonne réponse ou une réponse partielle, sans besoin de tapé toute la réponse
# #Pensez à une utilisation mauvaise (ex : Pour faire un devoir, mais sur un autre onglet, protégé par un mot de passe)
#Ajouté un mode pour des cartes aide mémoire
#Chaque question a un % pour le score 0, 1, 2 personalisé
#Mode pour avoir des questions d'un seul chapitre
#Mode pour les questions de math


import streamlit as st

st.set_page_config(page_title="Révision météo 1")

st.title("Platforme de révision pour le cours de météo 1")

if st.button("Jeu questionnaire"):
    st.experimental_set_query_params(page="jeu_questionnaire.py")