#   Ceci est un code pour créer une ia qui propose des recommandation basé sur les bonnes ou mauvaise réponse d'un questionnaire
#   Pour le cours de philo 2 Cchic
#   Questions basées sur les notes de cours personnelles de météo 1 du CQFA
#
#   Olivier Moreau
#

import streamlit as st

bqhumidité = [
    {"question" : "Quel est l'élément le plus important en météo?", "réponse" : "la vapeur d'eau"},
    {"question" : "Le point de rosée augmente si l'air est...", "réponse" : "chaud"},
    {"question" : "Qu'est ce que le point de rosée?", "réponse" : "La température à pression constante à laquelle si l'air doit être refroidit pour qu'il y ait saturation"},
    {"question" : "Que fait l'eau lorsqu'elle est dans l'air et devient liquide?", "réponse" : "elle donne son énergie à l'air, ce qui augmente la température de l'air"},
]

bqréchauffement = [
    {"question" : "Quel est la température qui définit la tropopause?", "réponse" : "-56"},
    {"question" : "Quels sont les quatres couches de l'atmosphère?", "réponse" : "la troposphère, la mésosphère, la stratosphère et la thermoshère"},
    {"question" : "Quel type d'onde nous envoit le Soleil (2 lettres) et quel est sa longeur d'onde?", "réponse" : "uv et petite ou courte"},
    {"question" : "Qu'est ce que la réflexion Albédo?", "réponse" : "Lorsque les rayons touchent la terre perpendiculairement, ils sont plus puissant que ceux tengent"},
]

bqrefroidissement = [
    {"question" : "Comment ce nomme le concept qui définit que la température diminue de 1,98°C par 1000 pi?", "réponse" : "le gradient thermique verticale"},
    {"question" : "Comment ce nomme le concept qui définit que la température diminue de 3°C par 1000 pi?", "réponse" : "le gradient adiabatique sec"},
]