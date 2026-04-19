#   Ceci est un code pour créer une ia qui propose des recommandation basé sur les bonnes ou mauvaise réponse d'un questionnaire
#   Pour le cours de philo 2 Cchic
#   Questions basées sur les notes de cours personnelles de météo 1 du CQFA
#
#   Olivier Moreau
#

import streamlit as st

bqhumidité = [
    {"theme" : "humidite", "question" : "Exam 1 Quel est l'élément le plus important en météo?", "réponse" : "la vapeur d'eau", "indice" : ""},
    {"theme" : "humidite", "question" : "Exam 1 Le point de rosée augmente si l'air est...", "réponse" : "chaud", "indice" : ""},
    {"theme" : "humidite", "question" : "Exam 1 Qu'est-ce que le point de rosée?", "réponse" : "La température à pression constante à laquelle si l'air doit être refroidi pour qu'il y ait saturation", "indice" : ""},
    {"theme" : "humidite", "question" : "Exam 1 Que fait l'eau lorsqu'elle est dans l'air et devient liquide?", "réponse" : "elle donne son énergie à l'air, ce qui augmente la température de l'air", "indice" : ""},
]

bqréchauffement = [
    {"theme" : "rechauffement", "question" : "Exam 1 Quel est la température qui définit la tropopause?", "réponse" : "-56", "indice" : ""},
    {"theme" : "rechauffement", "question" : "Exam 1 Quels sont les quatre couches de l'atmosphère?", "réponse" : "la troposphère, la mésosphère, la stratosphère et la thermosphère", "indice" : ""},
    {"theme" : "rechauffement", "question" : "Exam 1 Quel type d'onde nous envoie le Soleil (2 lettres) et quel est sa longueur d'onde?", "réponse" : "uv et petite ou courte", "indice" : ""},
    {"theme" : "rechauffement", "question" : "Exam 1 Qu'est-ce que la réflexion Albédo?", "réponse" : "Lorsque les rayons touchent la Terre perpendiculairement, ils sont plus puissants que ceux tangents", "indice" : ""},
]

bqrefroidissement = [
    {"theme" : "refroidissement", "question" : "Exam 1 Comment ce nomme le concept qui définit que la température diminue de 1,98°C par 1000 pi?", "réponse" : "le gradient thermique vertical", "indice" : ""},
    {"theme" : "refroidissement", "question" : "Exam 1 Comment ce nomme le concept qui définit que la température diminue de 3°C par 1000 pi?", "réponse" : "le gradient adiabatique sec", "indice" : ""},
]

stabilite_air = [
    {"theme" : "stabilite", "question" : "Que va faire l'air stable après qu'il ait été forcée de monter?", "réponse" : "L'air va redescendre", "indice" : "L'air va "},
    {"theme" : "stabilite", "question" : "Que va faire l'air instable après qu'il ait été forcée de monter?", "réponse" : "L'air va continuer de monter", "indice" : "L'air va "},
    {"theme" : "stabilite", "question" : "Que va faire l'air neutre après qu'elle ait été forcée de monter?", "réponse" : "L'air va rester à l'altitude où il est", "indice" : "L'air va "},
    {"theme" : "stabilite", "question" : "Si une particule est au dessus du GTVM, va-t-elle monter, descendre ou rester au même niveau?", "réponse" : "Elle va monter", "indice" : "Elle va "},
    {"theme" : "stabilite", "question" : "Si une particule est en dessous du GTVM, va-t-elle monter, descendre ou rester au même niveau?", "réponse" : "Elle va descendre", "indice" : "Elle va "},
    {"theme" : "stabilite", "question" : "Comment se nomme le type de stabilité lorsqu'une particule revient à son point de départ?", "réponse" : "stabilité absolue", "indice" : "stabilité "},
    {"theme" : "stabilite", "question" : "Si le GTVM change pour qu'il fasse plus froid à haut niveau et plus chaud à bas niveau, l'air devient-il plus stable ou plus instable?", "réponse" : "Plus instable", "indice" : "Plus "},
    {"theme" : "stabilite", "question" : "Si le GTVM change pour qu'il fasse plus chaud à haut niveau et plus froid à bas niveau, l'air devient-il plus stable ou plus instable?", "réponse" : "Plus stable", "indice" : "Plus "},
    {"theme" : "stabilite", "question" : "Quels sont les cinq éléments qui caractérisent l'air stable?", "réponse" : "Visibilité mauvaise, nuages stagnants, précipitation faible ou modérée, vent constant et faible ou modéré et continue et turbulence nulle à léger", "indice" : ""},
    {"theme" : "stabilite", "question" : "Quels sont les cinq éléments qui caractérisent l'air instable?", "réponse" : "Visibilité va s'améliorer, nuages vont bouger et nuage cumuliforme, précipitation en averse et avec des changements d'intensités, vents qui vont varier, jusqu'à fort, avec rafales et beaucoup de turbulence au niveau horizontal", "indice" : ""},
]

pression_atmo = [
    {"theme" : "pression", "question" : "La pression est responsable de 3 éléments. Quels sont-ils?", "réponse" : "Altitude de vol, déplacement des systèmes météorologiques et performance de vol", "indice" : ""},
    {"theme" : "pression", "question" : "Quel élément influence le poids de la colonne d'air", "réponse" : "Température", "indice" : ""},
    {"theme" : "pression", "question" : "Quel est l'intervalle de temps retenu pour calculer la pression théorique en dessous de la station, jusqu'au niveau de la mer?", "réponse" : "12 heures", "indice" : " heures"},
    {"theme" : "pression", "question" : "Quel est l'intervalle entre les lignes des isobares", "réponse" : "4 hPa", "indice" : " hPa"},
    {"theme" : "pression", "question" : "Quel est la ligne d'isobare qui est toujours indiquée?", "réponse" : "1000 hPa", "indice" : " hPa"},
    {"theme" : "pression", "question" : "Quels sont les autres noms de la basse pression", "réponse" : "Dépression et cyclone", "indice" : ""},
    {"theme" : "pression", "question" : "Comment définit-on une zone de basse pression?", "réponse" : "Une zone entourée de tous les côtés par une pression supérieure", "indice" : ""},
    {"theme" : "pression", "question" : "Si de l'air humide est dans une basse pression, que va-t-il se passer", "réponse" : "L'air va se condenser et former des nuages", "indice" : ""},
    {"theme" : "pression", "question" : "Quels sont les autres noms de la haute pression", "réponse" : "Anticyclone", "indice" : ""},
    {"theme" : "pression", "question" : "Comment définit-on une zone de haute pression?", "réponse" : "Une zone entourée de tous les côtés par une pression inférieure", "indice" : ""},
    {"theme" : "pression", "question" : "Quel temps fera-t-il dans une zone de haute pression et pourquoi?", "réponse" : "Du beau temps, car l'air va descendre et se réchauffer par compression, donc l'air va s'éloigner du point de rosée", "indice" : ""},
    {"theme" : "pression", "question" : "Qu'est-ce qu'un creux barométrique?", "réponse" : "Une zone allongée de basse pression où la pression la plus basse se trouve", "indice" : ""},
    {"theme" : "pression", "question" : "Comment sera la météo dans un creux barométrique et pourquoi?", "réponse" : "Mauvaise, car c'est un zone de convergence", "indice" : ""},
    {"theme" : "pression", "question" : "Comment est identifié un creux barométrique?", "réponse" : "Par une ligne pointillée", "indice" : "Par une "},
    {"theme" : "pression", "question" : "Qu'est-ce qu'une crête?", "réponse" : "Une zone allongée de haute pression où la pression la plus forte se retrouve", "indice" : ""},
    {"theme" : "pression", "question" : "Comment sera la météo dans une crête et pourquoi?", "réponse" : "Bonne, car c'est une haute pression", "indice" : ""},
    {"theme" : "pression", "question" : "Est-ce qu'une crête sera identifié?", "réponse" : "Non", "indice" : ""},
    {"theme" : "pression", "question" : "Qu'est-ce qu'un col?", "réponse" : "Une zone neutre entre deux zones de hautes pression et deux zones de basses pression", "indice" : ""},
    {"theme" : "pression", "question" : "Qu'est-ce que la tendance barométrique?", "réponse" : "La variation de la pression à un point donné en fonction du temps", "indice" : ""},
    {"theme" : "pression", "question" : "Plus les isobares sont collées, plus le vent sera ____.", "réponse" : "Fort", "indice" : ""},
    {"theme" : "pression", "question" : "Où la force de coriolis sera-t-elle la plus forte?", "réponse" : "Aux pôles", "indice" : ""},
    {"theme" : "pression", "question" : "Dans quel sens la force de coriolis influence-t-elle le vent?", "réponse" : "Vers la droite", "indice" : "Vers la "},
    {"theme" : "pression", "question" : "Qu'est-ce que le vent géostrophique et décris son mouvement?", "réponse" : "Du vent où la force de coriolis et la force du gradient de pression est égale. Il va parallèlement aux isobares", "indice" : ""},
    {"theme" : "pression", "question" : "L'effet coriolis influence-t-il plus le vent plus en altitude ou plus au sol?", "réponse" : "Plus en altitude", "indice" : "Plus "},
    {"theme" : "pression", "question" : "Qu'est-ce que la règle de Buys-Ballot?", "réponse" : "Avec le vent dans le dos, la basse pression est à gauche", "indice" : "Avec "},
    {"theme" : "pression", "question" : "Dans quel sens le vent tourne-t-il dans une zone de haute pression?", "réponse" : "Dans le sens horaire", "indice" : "Dans le sens "},
    {"theme" : "pression", "question" : "Dans quel sens le vent tourne-t-il dans une zone de basse pression?", "réponse" : "Dans le sens antihoraire", "indice" : "Dans le sens "},
    {"theme" : "pression", "question" : "Le vent est-il plus fort dans la haute ou dans la basse pression à pression égale et pourquoi?", "réponse" : "Il est plus fort dans la haute pression, car il est aidé par la force centrifuge", "indice" : "Il est plus fort dans la "},
    {"theme" : "pression", "question" : "De combien de degrés le vent est-il dévié sur un terrain lisse? (Écrire uniquement les chiffres)", "réponse" : "10", "indice" : ""},
    {"theme" : "pression", "question" : "De combien de degrés le vent est-il dévié sur un terrain accidenté? Écrire uniquement les chiffres)", "réponse" : "40", "indice" : ""},
    {"theme" : "pression", "question" : "Dans quel sens le vent est-il dévié à cause du sol? (Par rapport à la direction qu'il est sensé aller avec le gradient de pression et la force de coriolis.)", "réponse" : "Il est dévié à gauche", "indice" : "Il est dévié à "},
    {"theme" : "pression", "question" : "Comment se nomme les vents qui augmente d'intensité qui tendent vers la droite en montant en altitude?", "réponse" : "Dextrogyre", "indice" : ""},
    {"theme" : "pression", "question" : "Comment se nomme les vents qui diminuent d'intensité qui tendent vers la gauche en descendant en altitude?", "réponse" : "Lévogyre", "indice" : ""},
    {"theme" : "pression", "question" : "Comment va se comporter les vents si le système s'intensifie?", "réponse" : "Ils vont traverser les isobares", "indice" : ""},
    {"theme" : "pression", "question" : "Qu'est-ce que l'altitude indiquée?", "réponse" : "L'altitude lue sur l'altimètre lorsqu'il est au calage de l'aéroport", "indice" : ""},
    {"theme" : "pression", "question" : "Qu'est-ce que l'altitude pression?", "réponse" : "L'altitude lue sur l'altimètre lorsqu'il est au calage standard", "indice" : ""},
    {"theme" : "pression", "question" : "Qu'est-ce que l'altitude densité?", "réponse" : "L'altitude pression corrigée pour les erreurs de température", "indice" : ""},
    {"theme" : "pression", "question" : "Qu'est-ce que l'altitude vraie?", "réponse" : "L'altitude réelle par rapport au niveau de la mer", "indice" : ""},
    {"theme" : "pression", "question" : "Qu'est-ce que la hauteur?", "réponse" : "L'élévation réelle au dessus du sol", "indice" : ""},
    {"theme" : "pression", "question" : "Qu'est-ce que le niveau de vol?", "réponse" : "L'altitude en centaines de pieds lorsqu'on utilise le calage standard", "indice" : ""},
]

masse_air = [
    {"theme" : "masse", "question" : "Quelles sont les caractéristiques de l'atmosphère?", "réponse" : "Humidité, température, stabilité, altitude de la tropopause", "indice" : ""},
    {"theme" : "masse", "question" : "Quel est la définition d'une masse d'air?", "réponse" : "Un grand volume d'air ayant acquis les mêmes caractéristiques", "indice" : ""},
    {"theme" : "masse", "question" : "Quel est la limite verticale d'une masse d'air?", "réponse" : "La tropopause", "indice" : ""},
    {"theme" : "masse", "question" : "Qu'est-ce qu'une masse d'air mA?", "réponse" : "Maritime arctique", "indice" : ""},
    {"theme" : "masse", "question" : "Qu'est-ce qu'une masse d'air cA?", "réponse" : "Continentale arctique", "indice" : ""},
    {"theme" : "masse", "question" : "Qu'est-ce qu'une masse d'air mP?", "réponse" : "Maritime polaire", "indice" : ""},
    {"theme" : "masse", "question" : "Qu'est-ce qu'une masse d'air cP?", "réponse" : "Continentale polaire", "indice" : ""},
    {"theme" : "masse", "question" : "Qu'est-ce qu'une masse d'air mT?", "réponse" : "Maritime tropicale", "indice" : ""},
    {"theme" : "masse", "question" : "Qu'est-ce qu'une masse d'air cT?", "réponse" : "Continentale tropicale", "indice" : ""},
    {"theme" : "masse", "question" : "Quels sont les masses d'air qui touchent le Canada (abréviation)?", "réponse" : "cA, mA, mP, mT", "indice" : ""},
    {"theme" : "masse", "question" : "Si l'air est froid, la tropopause est-elle haute ou basse?", "réponse" : "Elle est basse", "indice" : "Elle est "},
    {"theme" : "masse", "question" : "Si la tropopause est chaud, est-elle haute ou basse?", "réponse" : "Elle est basse", "indice" : "Elle est "},
    {"theme" : "masse", "question" : "Quels sont les trois caractéristiques qui influence le déplacement et le degré de changement d'une masse d'air?", "réponse" : "La vitesse de déplacement, l'humidité et la différence de température", "indice" : ""},
    {"theme" : "masse", "question" : "Quel phénomène sera créé par un réchauffement par le dessous? (Sans déterminant)", "réponse" : "Convection", "indice" : ""},
    {"theme" : "masse", "question" : "Quel phénomène sera créé par un refroidissement par le dessous? (Sans déterminant)", "réponse" : "Inversion", "indice" : ""},
    {"theme" : "masse", "question" : "Comment se nomme la zone de transition entre deux masses d'air qui ont des caractéristiques très différentes?", "réponse" : "Un front", "indice" : "Un "},
    {"theme" : "masse", "question" : "Comment se nomme le front lorsque l'air froid s'en va?", "réponse" : "Un front chaud", "indice" : "Un "},
    {"theme" : "masse", "question" : "Comment se nomme le front lorsque l'air froid arrive?", "réponse" : "Un front froid", "indice" : "Un "},
]

fronts = [
    {"theme" : "front", "question" : "Quel est la largeur de la zone de mélange d'un front?", "réponse" : "50 à 100 NM", "indice" : " NM"},
    {"theme" : "front", "question" : "Dans quel système se retrouve presque tous les fronts?", "réponse" : "La basse pression", "indice" : "La "},
    {"theme" : "front", "question" : "De quel masse d'air provient le nom du front?", "réponse" : "L'air froid", "indice" : "L'air "},
    {"theme" : "front", "question" : "Quels sont les quatre éléments requis pour qu'un front soit indiqué sur une carte?", "réponse" : "Changement de vent, de température, d'humidité et de pression", "indice" : ""},
    {"theme" : "front", "question" : "Si un front est perpendiculaire aux isobares, ira-t-il plus vite qu'un front qui parallèle aux isobares?", "réponse" : "Oui", "indice" : ""},
    {"theme" : "front", "question" : "Quel front va le plus vite?", "réponse" : "Le front froid", "indice" : "Le front "},
    {"theme" : "front", "question" : "Comment se nomme le phénomène lorsque l'air chaud glisse sur l'air froid et monte en altitude?", "réponse" : "Glissement ascendant frontal", "indice" : ""},
    {"theme" : "front", "question" : "Quels sont les rapports de pente du front chaud?", "réponse" : "1 pour 150 à 1 pour 200", "indice" : ""},
    {"theme" : "front", "question" : "Quel est le rapport de pente du front froid?", "réponse" : "1 pour 50", "indice" : ""},
    {"theme" : "front", "question" : "Pour qu'une ligne de grain se forme, faut-il que le front froid soit rapide ou lent?", "réponse" : "Le front froid doit être rapide", "indice" : "Le front froid doit être "},
    {"theme" : "front", "question" : "Qu'est-ce qui crée des fronts en altitude?", "réponse" : "Des montagnes, un changement trop faible pour être qualifié de front au sol ou une réchauffement du sol par le soleil", "indice" : ""},
    {"theme" : "front", "question" : "La différence entre les masses d'air est-elle plus importante au sol ou en altitude et quelle est l'altitude qui définit la partie basse de la partie haute (pour cette question uniquement)?", "réponse" : "Au sol, en dessous de 4000 pi", "indice" : ""},
    {"theme" : "front", "question" : "Quels sont les cinq caractéristiques qui vont changer lors du passage d'un front?", "réponse" : "La température, le point de rosée, la pression, le vent et la visibilité", "indice" : ""},
    {"theme" : "front", "question" : "Lors du passage d'un front, la température va-t-elle changer brusquement ou graduellement?", "réponse" : "Elle va changer brusquement", "indice" : "Elle va changer "},
    {"theme" : "front", "question" : "Lors du passage d'un front chaud, est-ce que le point de rosée va augmenter?", "réponse" : "Oui", "indice" : ""},
    {"theme" : "front", "question" : "Lors du passage d'un front chaud, comment varie la pression?", "réponse" : "Elle diminue", "indice" : "Elle "},
    {"theme" : "front", "question" : "Lors du passage d'un front froid, comment varie la pression?", "réponse" : "Elle augmente", "indice" : "Elle "},
    {"theme" : "front", "question" : "Où se trouve les fronts dans une basse pression?", "réponse" : "Dans les creux", "indice" : ""},
    {"theme" : "front", "question" : "Le vent va-t-il plus vite dans l'air froid ou dans l'air chaud?", "réponse" : "Dans l'air froid", "indice" : "Dans l'air "},
    {"theme" : "front", "question" : "Dans quel direction faut-il corriger notre cap lorsqu'on passe un front?", "réponse" : "À droite", "indice" : "À"},
    {"theme" : "front", "question" : "Lors du passage d'un front froid, comment varie la visibilité?", "réponse" : "Elle augmente", "indice" : "Elle "},
    {"theme" : "front", "question" : "Lors du passage d'un front chaud, comment varie la visibilité?", "réponse" : "Elle diminue", "indice" : "Elle "},
    {"theme" : "front", "question" : "Qu'est-ce qu'une occlusion et comment sera le temps?", "réponse" : "Un front froid qui rattrappe un front chaud et qui se combinent ensemble. Le temps dépendra de l'addition des deux fronts et sera plus intense à l'endroit où les deux fronts se rencontrent", "indice" : ""},
    {"theme" : "front", "question" : "Quel est la vitesse qui définit un front stationnaire?", "réponse" : "Moins de 5 kt", "indice" : " kt"},
]

nuage_precipitation = [
    {"theme" : "nuage", "question" : "Quels sont les éléments requis pour qu'il y ait des nuages?", "réponse" : "Humidité, noyau de condensation et processus de refroidissement", "indice" : ""},
    {"theme" : "nuage", "question" : "Quels sont le(s) altitude(s) qui définissent les nuages élevés?", "réponse" : "20 000 à 40 000 pi", "indice" : " pi"},
    {"theme" : "nuage", "question" : "Quels sont le(s) altitude(s) qui définissent les nuages moyens?", "réponse" : "6500 à 20 000 pi", "indice" : " pi"},
    {"theme" : "nuage", "question" : "Quels sont le(s) altitude(s) qui définissent les nuages bas?", "réponse" : "6500 pi et moins", "indice" : " pi "},
    {"theme" : "nuage", "question" : "Quels sont le(s) altitude(s) qui définissent les nuages à développement vertical?", "réponse" : "Base à partir de 1600 pi", "indice" : " pi "},
    {"theme" : "nuage", "question" : "Quel est le nom, la hauteur et les caractéristiques du nuage ST?", "réponse" : "Stratus, bas, ressemble au brouillard, air stable, ne repose pas au sol, bruine ou faible neige", "indice" : ""},
    {"theme" : "nuage", "question" : "Quel est le nom, la hauteur et les caractéristiques du nuage NS?", "réponse" : "Nimbostratus, bas, précipitation continue faible ou modérée, très épais, air stable", "indice" : ""},
    {"theme" : "nuage", "question" : "Quel est l'épaisseur du NS?", "réponse" : "5000 à 15 000 pi d'épaisseur", "indice" : " pi d'épaisseur"},
    {"theme" : "nuage", "question" : "Quel est le nom, la hauteur et les caractéristiques du nuage SC?", "réponse" : "Stratocumulus, bas, base bien définie, ondulé ou roulé, peu de précipitation", "indice" : ""},
    {"theme" : "nuage", "question" : "Que se passe-t-il avec l'air lorsque le nuage est ondulé ou roulé?", "réponse" : "L'air est instable en dessous, stable au dessus et il y a de la turbulence mécanique", "indice" : ""},
    {"theme" : "nuage", "question" : "Quel est le nom, la hauteur et les caractéristiques du nuage AS?", "réponse" : "Altostratus, moyen, on peut voir la lune ou le soleil au travers, donc il n'est pas très épais", "indice" : ""},
    {"theme" : "nuage", "question" : "Quel est le nom, la hauteur et les caractéristiques du nuage AC?", "réponse" : "Altocumulus, moyen, instabilité au niveau du nuage", "indice" : ""},
    {"theme" : "nuage", "question" : "Quel est le nom, la hauteur et les caractéristiques du nuage ACC?", "réponse" : "Altocumulus castellanus, moyen, ressemble à ac, tourelle bien défini, très instable", "indice" : ""},
    {"theme" : "nuage", "question" : "Quel est le nom, la hauteur et les caractéristiques du nuage CI?", "réponse" : "Cirrus, élevé, cheveux d'ange", "indice" : ""},
    {"theme" : "nuage", "question" : "Quel est le nom, la hauteur et les caractéristiques du nuage CS?", "réponse" : "Cirrostratus, élevé, halo autour des astres, humidité visible, givrage possible, dangereux", "indice" : ""},
    {"theme" : "nuage", "question" : "Quel est le nom, la hauteur et les caractéristiques du nuage CC?", "réponse" : "Cirrocumulus, élevé, présence d'instabilité", "indice" : ""},
    {"theme" : "nuage", "question" : "Quel est le nom, la hauteur et les caractéristiques du nuage CU?", "réponse" : "Cumulus, développement verticale, turbulence convective et instabilité, beau temps, base bien définie, cumulus fractus quand ils se séparent", "indice" : ""},
    {"theme" : "nuage", "question" : "Quel est le nom, la hauteur et les caractéristiques du nuage TCU?", "réponse" : "Cumulus bourgeonnant ou cumulus congestus, développement verticale, aspect de chou-fleur, givrage fort, vent ascendant et descendent, averses", "indice" : ""},
    {"theme" : "nuage", "question" : "Quel est le nom, la hauteur et les caractéristiques du nuage CB?", "réponse" : "Cumulonimbus, développement verticale, orages, cisaillement du vent à bas niveau, forme d'enclume", "indice" : ""},
    {"theme" : "nuage", "question" : "Pourquoi le CB a-t-il une forme d'enclume?", "réponse" : "Il y a une inversion à la tropopause", "indice" : ""},
    {"theme" : "nuage", "question" : "La partie la plus longue de l'enclume indique quoi et où est-elle par rapport au CB?", "réponse" : "La direction dans laquelle le cb va et elle est en avant du cb.", "indice" : ""},
    {"theme" : "nuage", "question" : "Comment se nomme le principe lorsque de l'air froid arrive au dessus d'une étendue chaude et humide et que l'air se charge d'humidité et se condense, car il monte?", "réponse" : "Convection due à l'advection", "indice" : ""},
    {"theme" : "nuage", "question" : "Que se passe-t-il à la base des nuages lorsqu'il y a de la convection?", "réponse" : "La base du nuage va monter, car le bas du nuage va s'évaporer", "indice" : ""},
    {"theme" : "nuage", "question" : "Où va se situer la turbulence mécanique par rapport au nuage?", "réponse" : "En dessous ou dans le nuage", "indice" : ""},
    {"theme" : "nuage", "question" : "Dans quel ordre, avec les abréviations, allons nous voir apparaître les nuages pour un front chaud, humide et stable?", "réponse" : "ci, cs, as, ns et st", "indice" : ""},
    {"theme" : "nuage", "question" : "Dans quel ordre, avec les abréviations, allons nous voir apparaître les nuages pour un front chaud, humide et instable?", "réponse" : "ci, cs, ac et as, cb et ns et st", "indice" : ""},
    {"theme" : "nuage", "question" : "Dans quel ordre, avec les abréviations, allons nous voir apparaître les nuages pour un front chaud, sec et stable?", "réponse" : "ci, cs, as", "indice" : ""},
    {"theme" : "nuage", "question" : "Dans quel ordre, avec les abréviations, allons nous voir apparaître les nuages pour un front froid, instable, humide et chaud?", "réponse" : "st, cb, cu", "indice" : ""},
    {"theme" : "nuage", "question" : "Dans quel ordre, avec les abréviations, allons nous voir apparaître les nuages pour un front froid, peut-être instable, humide et chaud?", "réponse" : "tcu, ac et as, cu, cs et ci", "indice" : ""},
    {"theme" : "nuage", "question" : "Quels sont les nuages associées au lignes de grain et comment sont-ils?", "réponse" : "cb et tcu organisés", "indice" : ""},
    {"theme" : "nuage", "question" : "Quels sont les éléments qui influencent les changements lors d'un soulèvement orographique?", "réponse" : "Vitesse du déplacement, élévation du terrain, humidité", "indice" : ""},
    {"theme" : "nuage", "question" : "De quel élément dépend le type de nuage lors d'un soulèvement orographique?", "réponse" : "La stabilité de l'air", "indice" : ""},
    {"theme" : "nuage", "question" : "Qu'est-ce qu'une cuvette d'air froid?", "réponse" : "Lorsque l'air stagne, car elle n'a pas assez d'énergie pour passer au dessus d'une montagne, mais se refroidit", "indice" : ""},
    {"theme" : "nuage", "question" : "Est-ce que la convergence va amener un soulèvement rapide ou lent?", "réponse" : "Lent", "indice" : ""},
    {"theme" : "nuage", "question" : "L'advection est-elle plus importante lors du réchauffement ou du refroidissement pour la formation des nuages?", "réponse" : "Refroidissement", "indice" : ""},
    {"theme" : "nuage", "question" : "Comment les précipitations vont influencer les nuages?", "réponse" : "Une partie des gouttelettes va s'évaporer, ce qui va créer des stratus en altitude ou du brouillard ou de la brume au sol", "indice" : ""},
    {"theme" : "nuage", "question" : "Quel est l'élément responsable de la pluie?", "réponse" : "Les courants verticaux", "indice" : ""},
    {"theme" : "nuage", "question" : "Pourquoi les courants verticaux sont-ils responsables des précipitations?", "réponse" : "Les gouttelettes vont bouger, donc se cogner et grossir", "indice" : ""},
    {"theme" : "nuage", "question" : "Qu'est-ce que l'effet Bergeron?", "réponse" : "La saturation autour d'un cristal de glace se fait à un taux d'humidité plus bas qu'une gouttelette. donc, il refroidit se qui est autour de lui, grossit, devient plus lourd, descend et ainsi de suite. il ne devient jamais très gros et deviennent de la pluie s'il passe dans une zone d'air chaud", "indice" : ""},
    {"theme" : "nuage", "question" : "Que fait l'effet de coalescence ou de captation?", "réponse" : "Il provoque un accroissement rapide de la dimension donc de leur masse et de leur vitesse de chute.", "indice" : ""},
    {"theme" : "nuage", "question" : "Que se passe-t-il lorsque deux cristaux entrent en collisions (lors de la formation des précipitations)?", "réponse" : "Plusieurs fins cristaux se séparent et créent des nouveaux noyaux de condensation", "indice" : ""},
    {"theme" : "nuage", "question" : "Quelle sera le type de précipitation s'il y a de l'air chaud au dessus d'air froid?", "réponse" : "Précipitations verglaçantes ou verglas", "indice" : "Précipitations "},
    {"theme" : "nuage", "question" : "Quels éléments influencent les précipitations?", "réponse" : "Force du courant ascendant, humidité et température de l'air", "indice" : ""},
    {"theme" : "nuage", "question" : "Que signifie averse?", "réponse" : "Précipitation de courte durée, avec possibilité d'éclaircissement entre les précipitations et nuage cumuliforme", "indice" : ""},
    {"theme" : "nuage", "question" : "Que signifie précipitation intermittente?", "réponse" : "Pas une averse, mais précipitations s'arrêtent et reprennent au moins une fois dans l'heure, nuage stratiforme, précipitations proviennent du même nuage", "indice" : ""},
    {"theme" : "nuage", "question" : "Que signifie précipitation continue?", "réponse" : "Précipitation qui tombe sans intérruptions pendant au moins une heure, nuage stratiforme", "indice" : ""},
    {"theme" : "nuage", "question" : "Quels sont les effets sur le vol des précipitations?", "réponse" : "Possibilité de givrage, visibilité réduite, modifie l'écoulement de l'air sur l'aile, modifie la vitesse de décrochage, diminue le contact avec la piste", "indice" : ""},
]

###
fb_fd = [
    {"theme" : "FBFD", "question" : "Quels sont les niveaux pour lesquelles le centre météorologique canadien émet des prévisions de vents et/ou de température, dans les bas niveaux? (Ne pas mettre pi)", "réponse" : "3000, 6000, 9000, 12000 et 18000", "indice" : ""},
    {"theme" : "FBFD", "question" : "Que donnent les FB et les FD?", "réponse" : "Ils donnent des prévisions de vents et de température en altitude", "indice" : "Ils donnent des"},
    {"theme" : "FBFD", "question" : "Est-ce que l'altitude des FB et des FD est en ASL ou en AGL?", "réponse" : "En ASL", "indice" : "En"},
    {"theme" : "FBFD", "question" : "Complète la phrase suivante en écrivant uniquement les nombres séparés d'un virgule : On omet le FD/FB pour l'altitude ____ pi lorsque l'altitude du terrain est supérieur à ____ pi.", "réponse" : "3000, 1500", "indice" : ""},
    {"theme" : "FBFD", "question" : "Quel élément est omis dans le FB/FD de 3000 pi (vent ou température)?", "réponse" : "température", "indice" : ""},
    {"theme" : "FBFD", "question" : "Par qui sont données les vents et les tempéatures à haut niveau et quels sont les altitudes? (Ne pas mettre pi)", "réponse" : "Par les Américains pour les altitudes 24000, 30000, 34000, 39000, 45000 et 53000", "indice" : "Par les  pour les altitudes "},
    {"theme" : "FBFD", "question" : "Pour les FD, est-ce que la direction du vent est donnée en centaine, dizaine ou à l'unité, en degrés?", "réponse" : "dizaine", "indice" : ""},
    {"theme" : "FBFD", "question" : "Pour les FB/FD, est-ce que la direction du vent est donnée par rapport au nord vrai ou au nord magétique?", "réponse" : "Nord vrai", "indice" : "Nord "},
    {"theme" : "FBFD", "question" : "Quel est l'unité de mesure de la vitesse des vents pour les FB/FD?", "réponse" : "Le noeud", "indice" : "Le "},
    {"theme" : "FBFD", "question" : "Quel est l'unité de mesure de la température pour les FB/FD, le °C, le °K ou le °F?", "réponse" : "Le °C", "indice" : "Le "},
    {"theme" : "FBFD", "question" : "Pour le FD, que représente les deux premiers chiffres?", "réponse" : "La direction des vents", "indice" : "La "},
    {"theme" : "FBFD", "question" : "Pour le FD, que représente les chiffres du milieu?", "réponse" : "La vitesse des vents", "indice" : "La "},
    {"theme" : "FBFD", "question" : "Pour le FD, que représente les deux derniers chiffres? (Après le +/- pour les bas niveaux)", "réponse" : "La température", "indice" : "La "},
    {"theme" : "FBFD", "question" : "Pour les FB/FD, les bas niveaux sont ___ à 24 000 pi : inférieur , inférieur ou égale, supérieur, supérieur ou égale .", "réponse" : "inférieur ou égale", "indice" : ""},
    {"theme" : "FBFD", "question" : "Pour les FB/FD, les hauts niveaux sont ___ à 24 000 pi : inférieur , inférieur ou égale, supérieur, supérieur ou égale .", "réponse" : "supérieur", "indice" : ""},
    {"theme" : "FBFD", "question" : "La température est automatiquement négative pour les FB/FD ____ à _____ pi? (Sépare le(s) mot(s) et le nombre par une virgule)", "réponse" : "supérieur, 24000", "indice" : ""},
    {"theme" : "FBFD", "question" : "Les FD sont émis combien de fois par jour? (en chiffre)", "réponse" : "2 fois", "indice" : " fois"},
    {"theme" : "FBFD", "question" : "Les FD, un fois émis, sont valide pour combien de temps? (Sépare le(s) nombre(s) par une(des) virgule(s) et ne mets pas h)", "réponse" : "6, 12, 24", "indice" : ""},
    {"theme" : "FBFD", "question" : "Les FB sont émis combien de fois par jour? (en chiffre)", "réponse" : "4", "indice" : ""},
    {"theme" : "FBFD", "question" : "Dans le FD, quel code indique que les vents sont léger et variable?", "réponse" : "9900", "indice" : ""},
    {"theme" : "FBFD", "question" : "Dans le FD, si les deux premiers chiffres dépasses 36, que faut-il faire?", "réponse" : "Enlevé 50 à la direction des vents et ajouté 100 à la vitesse des vents", "indice" : ""},
    {"theme" : "FBFD", "question" : "Est-ce que les deux premiers chiffres d'un FD peuvent être supérieur à 36?", "réponse" : "Non", "indice" : ""},
    {"theme" : "FBFD", "question" : "Pourquoi les FB sont-ils plus précis que les FD?", "réponse" : "Car, ils sortent plus souvent", "indice" : "Car, "},
]

airmet_sigmet = [
    {"theme" : "___met", "question" : "Qu'est-ce qu'un Airmet?", "réponse" : "Un avis météo à court terme qui indique des conditions potentiellement dangereuses", "indice" : "Un "},
    {"theme" : "___met", "question" : "Pourquoi les Airmet sont-ils utilisés?", "réponse" : "Pour indiquer les changements importants et pour modifier un GFA", "indice" : "Pour "},
    {"theme" : "___met", "question" : "Les Airmet décrivent des conditions jusqu'à quel altitude inclusivement? (Ne pas mettre pi)", "réponse" : "24000", "indice" : ""},
    {"theme" : "___met", "question" : "Quels sont, en générale, les critères d'émissions d'un Airmet?", "réponse" : "Un développement inatendu, la dissipation ou la non-manifestation des phénomènes", "indice" : ""},
    {"theme" : "___met", "question" : "Quels sont spécifiquement les critères d'émissions d'un Airmet?", "réponse" : "Une vitesse moyenne des vents dépassant 30 kt, une visibilité réduite à moins de 3 SM, une couverture nuageuse fragmenté ou de ciel couvert dont la base est à moins de 1000 pi AGL, des orages isolés ou occasionnels, des orages isolés ou occasionnels accompagnés de grêle, des cumulus bourgeonnants isolés, occasionnels ou fréquents, des cumulus bourgeonnants occasionnels et orages isolés accompagné ou non de grêle, des cumulus bourgeonnants fréquents et orages isolés accompagné ou non de grêle, de la turbulence modérée, du givrage modéré ou une onde orographique modérée", "indice" : ""},
    {"theme" : "___met", "question" : "Quel est la période de validité d'un Airmet?", "réponse" : "Elle est de 4 h ou jusqu'à sa mise-à-jour ou son annulation", "indice" : "Elle est de  h ou "},
    {"theme" : "___met", "question" : "Comment les Airmet sont-ils classifiers?", "réponse" : "À l'aide d'une classification alphanumérique", "indice" : "À l'aide d'une "},
    {"theme" : "___met", "question" : "Dans la phrase suivante, dans un Airmet : <<WTN 15 NM of LN>>, est ce que la largeur de la ligne est de 15 ou 30 NM?", "réponse" : "30 NM", "indice" : " NM"},
    {"theme" : "___met", "question" : "Jusqu'à combien de temps avant le début du phénomène est-ce qu'un Airmet pourrais-être émis?", "réponse" : "4 h", "indice" : " h"},
    {"theme" : "___met", "question" : "Est-ce que les Airmet sont mise-à-jour automatiquement?", "réponse" : "Non, sauf si une nouvelle GFA est émis", "indice" : " ,sauf si "},
    {"theme" : "___met", "question" : "Quels sont les critères d'annulation d'un Airmet?", "réponse" : "L'émission d'une nouvelle GFA, la condition ne se matérialise pas ou se termine avant l'émission de la prochaine GFA ou les conditions deviennent assez dangereuse pour l'émission d'un Sigmet", "indice" : ""},
    {"theme" : "___met", "question" : "Que doit-on inclure quand un Airmet est annulé?", "réponse" : "Un énoncé justifiant l'annulation", "indice" : ""},
    {"theme" : "___met", "question" : "Pourquoi utilise-t-on des Airmet?", "réponse" : "Pour communiquer des changements météorologiques importants aux pilotes après leurs exposés et leurs départs", "indice" : ""},
    {"theme" : "___met", "question" : "Où sont disponible les Airmet et les Sigmet?", "réponse" : "Sur le site de Nav Canada et sur 121.7", "indice" : "Sur  et sur "},
    {"theme" : "___met", "question" : "Est-ce que ce sont les Airmet ou les Sigmet qui sont un moyen internationnal de communique de l'information?", "réponse" : "Sigmet", "indice" : ""},
    {"theme" : "___met", "question" : "Quel est le rôle d'un sigmet?", "réponse" : "Il est de donner des alertes à court terme sur certains phénomènes dangereux", "indice" : "Il est de "},
    {"theme" : "___met", "question" : "Quels sont les phénomènes indiqués par les Sigmet? (Pas précisément, on cherche une définition)", "réponse" : "Les phénomènes dangereux er d'importance vitale pour tous les types d'aéronefs", "indice" : "Les phénomènes "},
    {"theme" : "___met", "question" : "Quel est la zone, au niveau verticale, dans laquel des Sigmet peuvent être émis?", "réponse" : "De la surface à 60000 pi inclusivement", "indice" : ""},
    {"theme" : "___met", "question" : "Pourquoi utilise-t-on des Sigmet?", "réponse" : "Pour communiquer des changements météorologiques importants aux pilotes après leurs exposés et leurs départs et pour modifier automatiquement un GFA", "indice" : ""},
    {"theme" : "___met", "question" : "Quels sont les critères d'émissions d'un Sigmet?", "réponse" : "Des orages fréquents accompagnés ou non de grêle, avec possibilité de tornade/trombe marine et/ou en ligne de grains, de la turbulence forte, du givrage fort dû ou non à de la pluie vergalçante, des ondes orographique importante, du cisaillement de vent à basse altitude, des fortes tempêtes de poussière ou de sable, des nuages radioactifs, des cendres volcaniques ou un cyclone tropical", "indice" : ""},
    {"theme" : "___met", "question" : "Un Sigmet couvre une période de combien d'heures et quel est l'exception?", "réponse" : "4 h, sauf pour les Sigmet de cendres volcaniques et de cyclones tropicaux qui couvre 6 h", "indice" : " h, sauf pour les Sigmet  qui couvre  h"},
    {"theme" : "___met", "question" : "Un Sigmet peut être émis combien de temps d'avance et quel est l'exception?", "réponse" : "4 h, sauf pour les Sigmet de cendres volcaniques et de cyclones tropicaux qui peuvent être émis 12 h d'avance", "indice" : " h, sauf pour les Sigmet  qui peuvent être émis  h d'avance"},
    {"theme" : "___met", "question" : "Que signifie WVCN dans un Sigmet?", "réponse" : "Sigmet de cendre volcanique", "indice" : "Sigmet "},
    {"theme" : "___met", "question" : "Que signifie WCCN dans un Sigmet?", "réponse" : "Sigmet de cyclone tropical", "indice" : "Sigmet "},
    {"theme" : "___met", "question" : "Que signifie WSCN dans un Sigmet?", "réponse" : "Tous les autres Sigmet", "indice" : " Sigmet "},
    {"theme" : "___met", "question" : "Lorsque l'on parle de la direction des vents, que signife le WD après le point cardinal? (en français)", "réponse" : "va vers", "indice" : ""},
    {"theme" : "___met", "question" : "Lorsque l'on parle de la direction des vents, que signife le LY après le point cardinal? (en français)", "réponse" : "vient de", "indice" : ""},
]

atmo_type = [
    {"theme" : "atmo", "question" : "Selon l'OACI, quel sont les caractérisrtiques de base de l'atmosphère?", "réponse" : "Un air qui est parfaitmement sec, qui est à 15°C au niveau de la mer, qui a un GTV de 1.98°C/1000 pi et une pression au niveau de la mer de 29.92 poHg", "indice" : "Un air qui est , qui  °C , qui °C/1000 pi et  poHg"},
    {"theme" : "atmo", "question" : "Quels sont les critères pour que les conditions soit VMC?", "réponse" : "Plafond de plus de 3000 pi AGL ET visibilité de plus de 5 SM", "indice" : "Plafond de  pi  ET visibilité de  SM"},
    {"theme" : "atmo", "question" : "Quels sont les critères pour que les conditions soit MVFR?", "réponse" : "Plafond de 1000 à 3000 pi AGL OU visibilité de 3 à 5 SM", "indice" : "Plafond de  pi  OU visibilité de  SM"},
    {"theme" : "atmo", "question" : "Quels sont les critères pour que les conditions soit IMC?", "réponse" : "Plafond de moins de 1000 pi AGL OU visibilité de moins de 3 SM", "indice" : "Plafond de  pi  OU visibilité de  SM"},
    {"theme" : "atmo", "question" : "Quel sont le minimum VFR selon le RAC, dans un espace aérien contrôlé?", "réponse" : "Visibilité d'au moins 3 SM, distance latérale de 1 SM des nuages et distance verticale de 500 pi des nuages", "indice" : "Visibilité d'au moins  SM, distance latérale de  SM des nuages et distance verticale de  pi des nuages"},
    {"theme" : "atmo", "question" : "Quel sont le minimum VFR selon le RAC, dans un espace aérien non contrôlé, à 1000 pi et +?", "réponse" : "Visibilité d'au moins 1 SM, distance latérale de 2000 pi des nuages et distance verticale de 500 pi des nuages", "indice" : "Visibilité d'au moins  SM, distance latérale de  pi des nuages et distance verticale de  pi des nuages"},
    {"theme" : "atmo", "question" : "Quel sont le minimum VFR selon le RAC, dans un espace aérien non contrôlé, en dessous de 1000 pi?", "réponse" : "Visibilité d'au moins 2 SM et hors des nuages", "indice" : "Visibilité d'au moins  SM et  des nuages"},
    {"theme" : "atmo", "question" : "Quel sont le minimum VFR selon le RAC, dans un espace aérien contrôlé, avec un SVRF?", "réponse" : "Visibilité d'au moins 1 SM et hors des nuages", "indice" : "Visibilité d'au moins  SM et  des nuages"},
    {"theme" : "atmo", "question" : "Quel est le minumum de température en Solo sur le C-23?", "réponse" : "- 18°C", "indice" : "- °C"},
    {"theme" : "atmo", "question" : "Quel est le minumum de température en DC sur le C-23?", "réponse" : "- 24°C", "indice" : "- °C"},
    {"theme" : "atmo", "question" : "Quel est le minumum de vents traversiers en Solo sur le C-23?", "réponse" : "17 KTS à 90°", "indice" : " KTS à 90°"},
    {"theme" : "atmo", "question" : "Quel est le minumum de vents traversiers en DC sur le C-23?", "réponse" : "25 KTS à 90°", "indice" : " KTS à 90°"},
    {"theme" : "atmo", "question" : "Quel est le minumum de vents en Solo sur le C-23, pour un étudiant ayant fait 0 à 29.9 heures en solo?", "réponse" : "22 KTS avec rafales n'excédant pas 10 KTS", "indice" : " KTS avec rafales n'excédant pas  KTS"},
    {"theme" : "atmo", "question" : "Quel est le minumum de vents en Solo sur le C-23, pour un étudiant ayant fait 30 heures et plus en solo?", "réponse" : "28 KTS avec rafales n'excédant pas 15 KTS", "indice" : " KTS avec rafales n'excédant pas  KTS"},
    {"theme" : "atmo", "question" : "Quel sont les minumums, selon le MANOP, pour un vol de circuit à CYRC en solo?", "réponse" : "Plafond de 1500 pi AGL et visibilité de 5 SM", "indice" : "Plafond de  pi AGL et visibilité de  SM"},
    {"theme" : "atmo", "question" : "Quel sont les minumums, selon le MANOP, pour les zones d'entrainement ou le tour du lac, en solo?", "réponse" : "Plafond de 2500 pi AGL et visibilité de 9 SM", "indice" : "Plafond de  pi AGL et visibilité de  SM"},
    {"theme" : "atmo", "question" : "Quel sont les minumums, selon le MANOP, pour un vol-voyage en solo?", "réponse" : "Plafond de 3000 pi AGL et visibilité de 9 SM", "indice" : "Plafond de  pi AGL et visibilité de  SM"},
    {"theme" : "atmo", "question" : "Quel est la condition pour qu'il y ait des vols dans les zones d'entrainement/tour du lac?", "réponse" : "Il doit y avoir un instructeur de présent dans les zones d'entrainement ou tour du lac en tout temps", "indice" : ""},
    {"theme" : "atmo", "question" : "Est-ce qu'un vol peut être approuvé, et quel sont le conditions pour le faire, lorsque le TAF de Bagotville ou de Roberval indique un Tempo inférieur au minimum prévu pour les zones et le tour du lac, mais qu'un instructeur est présent voit que les conditions dans les zones/tour du lac sont supérieur à 2500 pi AGL et 9 SM?", "réponse" : "oui, mais il doit y avoir un instructeur de présent en tout temps et les contions prévues ne peuvent pas être inférieur à 1500 pi AGL et 5 SM", "indice" : ""},
    {"theme" : "atmo", "question" : "Pour qu'un vol-voyage soit approuvé, il faut que les conditions soit dans les limites __ heure(s), selon les TAF de CYRJ ET CYBG après le retour à CYRC? (nombre)", "réponse" : "1 h", "indice" : " h"},
    {"theme" : "atmo", "question" : "Si les contions sont bonne partout, quel(s) type(s) de vol peut être approuvé?(Circuit = 1, Zones = 2, Vol-voyage = 3)", "réponse" : "1, 2, et 3", "indice" : ""},
    {"theme" : "atmo", "question" : "Si les contions sont bonne à CYRC et CYBG, mais mauvaise à CYRJ, quel(s) type(s) de vol peut être approuvé?(Circuit = 1, Zones = 2, Vol-voyage = 3)", "réponse" : "1 et 2", "indice" : ""},
    {"theme" : "atmo", "question" : "Si les contions sont bonne à CYRC et CYRJ, mais mauvaise à CYBG, quel(s) type(s) de vol peut être approuvé?(Circuit = 1, Zones = 2, Vol-voyage = 3)", "réponse" : "1 et 2", "indice" : ""},
    {"theme" : "atmo", "question" : "Si les contions sont bonne à CYRC, mais mauvaise à CYBG et CYRJ, quel(s) type(s) de vol peut être approuvé?(Circuit = 1, Zones = 2, Vol-voyage = 3)", "réponse" : "1", "indice" : ""},
    {"theme" : "atmo", "question" : "Si les contions sont bonne à CYBG, mais mauvaise à CYBG et CYRJ, quel(s) type(s) de vol peut être approuvé?(Circuit = 1, Zones = 2, Vol-voyage = 3)", "réponse" : "Aucun", "indice" : ""},
    {"theme" : "atmo", "question" : "Si les contions mauvaise partout, quel(s) type(s) de vol peut être approuvé?(Circuit = 1, Zones = 2, Vol-voyage = 3)", "réponse" : "Aucun", "indice" : ""},
    {"theme" : "atmo", "question" : "Pour les limites des vents traversiers en Solo, quel est la restriction sur le nombre d'heure (0 à 29.9 et 30 et +)?", "réponse" : "Les heures doivent avoir été faites au CQFA", "indice" : "Les heures doivent "},
]




Questions météo 

chapitre restant : PIREP, Visibilité et GFA

Supprime les —- et écrit dans ces sections. Pas besoin de remplir theme/indice

Chapitre PIREP
1
{"theme" : "", "question" : "Que signifie UACN01?", "réponse" : "PIREP non-urgent", "indice" : ""},
2
{"theme" : "", "question" : "Es-ce que un wind shear d’environ 15 kts en approche est un PIREP URGENT?", "réponse" : "Oui", "indice" : ""},
3
{"theme" : "", "question" : "Que signifie TR?", "réponse" : "Trace = La glace devient perceptible", "indice" : ""},
4
{"theme" : "", "question" : "qu’est-ce qu’un PIREP?", "réponse" : "rapport publié par un pilote", "indice" : ""},
5
{"theme" : "", "question" : "décode et définit la raison principale de publication de ce PIREP: UACN10 CZNB 101457 EG
UA /OV YSM 330005 /TM 1453 /FLDURC /TP JS31 /SK 004 OVC 022 /IC TR LGT ICGIC /RM VERT VIS 008
?", "réponse" : "Un British aerospace Jetstream en montée à 5 NM au 330° de YSM rapporte à 14:53Z un plafond à 400 ft avec une couche overcast à 2200 ft, un givrage trace à léger, icing in-cloud et une visibilité verticale de 800 ft. Raison de publication: givrage + plafond très bas + visibilité verticale réduite", "indice" : ""},
6
{"theme" : "", "question" : "décode et définit la raison principale de publication de ce PIREP : UACN10 CYTH 101728 WG
UA /OV CYTH /TM 1707 /FLDURD /TP PC12 /WV 200022 /RM WND AT 500AGL ON APCH RWY 06 CORR COPY?", "réponse" : "Un PC12 (Pilates single-engin turboprop) en descente à CYTH à 17:07Z signale un vent du 200° à 22 kt et un vent particulier à 500 ft AGL sur l’approche de la piste 06. Raison de publication: vent de dos en descente", "indice" : ""},
7
{"theme" : "", "question" : "décode et définit la raison principale de publication de ce PIREP : UACN10 CYQQ 101823 VR
UA /OV CYQQ /TM 1813 /FL3400 /TP F18 /RM ENTERED CLD AT 3400FT. TOPS 15000FT.?", "réponse" : "Un F18 près de CYQQ à 18:13Z indique être entré dans les nuages à 3400 ft avec des sommets atteignant 15 000 ft. Raison de publication: info essentielle", "indice" : ""},
8
{"theme" : "", "question" : "décode et définit la raison principale de publication de ce PIREP : UACN01 CYHZ 111755 QM
UUA /OV CYHZ /TM 1753 /FLDURD /TP B190 /TB MDT BLO 030 /IC LGT RIME BLO 030 /RM WIND SHEAR +/- 15 KTS ON APCH?", "réponse" : "Un Beechcraft 1900 en descente à CYHZ à 17:53Z rapporte une turbulence modérée et un givrage léger blanc sous 3000 ft ainsi qu’un wind shear de ±15 kt en approche, ce qui en fait un PIREP urgent. Raison de publication: wind shear +15 kts", "indice" : ""},
9
{"theme" : "", "question" : "décode et définit la raison principale de publication de ce PIREP : UACN10 CYQR 111557 WG
UA /OV CYQR 310001 /TM 1555 /FLDURD /TP CRJ2 /SK 021OVC /RM APCH RWY 13 PILOT BROKE OUT AT MIN. FLT VIS 1/4SM. VIA TWR?", "réponse" : "Un Bombardier CRJ200 en descente à 1 NM au 310° de CYQR à 15:55Z signale un plafond overcast à 2100 ft et indique avoir percé les nuages au minimum IFR avec une visibilité de 1/4 SM en approche piste 13. Raison de publication: conditions IFR sévères", "indice" : ""},
10
{"theme" : "", "question" : "décode et définit la raison principale de publication de ce PIREP : UACN10 CYQB 141533 UL
UA /OV CYUL /TM 1531 /FL210 /TP CL25 /SK OVC170 /TB SFC-170 SMOOTH 170-210 SMALL RIDDLE ONLY /RM FREEZING PCPNS FM SFC-040, LIQUID PCPN ABV
?", "réponse" : "Un CL-215 au FL210 près de CYUL à 15:31Z rapporte une couche overcast à 17 000 ft, des conditions lisses du sol à 21 000 ft et des précipitations givrantes du sol à 4000 ft puis liquides au-dessus. Raison de publication: précipitations givrantes", "indice" : ""},
11
{"theme" : "", "question" : "décode et définit la raison principale de publication de ce PIREP : UACN10 CYQB 012034 UL
UA /OV CYFE 225005 /TM 2030 /FL013 /TP BE23 /SK 012 OVC 045 /RM LOW CIG, PCPN IN FRST 5NM N OF ST LAUR. FRM 5NM SW OF CYFE TO NE?", "réponse" : "Un Beech-craft 23 à 13 000 ft près de CYFE à 20:30Z signale un plafond bas avec overcast à 1200 ft et 4500 ft ainsi que des précipitations dans les 5 premiers NM au nord du St-Laurent et de 5 NM au sud-ouest de CYFE jusqu’au nord-est. Raison de publication: plafond bas + précipitations", "indice" : ""},
12
{"theme" : "", "question" : "décode et définit la raison principale de publication de ce PIREP : UACN10 CYXU 120022 YZ
UA /OV CYYZ /TM 0020 /FL055 /TP UNKN /TB MOD 055-090 /RM REPD BY ALL TYPE?", "réponse" : "Un appareil non identifié près de CYYZ à 00:20Z rapporte une turbulence modérée entre 5500 et 9000 ft, confirmée par tous les types d’aéronefs. Raison de publication: turbulence modérée", "indice" : ""},

13

{"theme" : "", "question" : "décode et définit la raison principale de publication de ce PIREP : UACN10 CYXU 112200 YZ
UA /OV CYGD /TM 2155 /FL330 /TP UNKN /TB LGT-MOD 330-350 /RM REPD AS LGT - OCNL MOD CHOP, REPD BY ALL TYP", "réponse" : "Un appareil non identifié au FL330 près de CYGD à 21:55Z signale une turbulence légère à modérée entre FL330 et FL350, décrite comme légère avec parfois du chop modéré, rapportée par tous les types. Raison de publication: turbulence en altitude", "indice" : ""},

14

{"theme" : "", "question" : "décode et définit la raison principale de publication de ce PIREP : UACN10 CYEG 120027 EG
UA /OV 6122N13902W /TM 0005 /FL370 /TP B748 /RM MOUNTAIN WAVES +/- 10 KTS AND 100 FEET", "réponse" : "Un Boeing 747-8 au FL370 à 00:05Z au-dessus de 61°22N 139°02W rapporte des ondes orographiques causant des variations de ±10 kt et ±100 ft. Raison de publication: mountain waves", "indice" : ""},



Questions météo 

chapitre restant : PIREP, Visibilité et GFA

Supprime les —- et écrit dans ces sections. Pas besoin de remplir theme/indice

Chapitre visibilité 
1
{"theme" : "", "question" : "Quels sont les 6 facteurs qui peuvent influencer la visibilité?", "réponse" :" brume sèche, fumée, sable et poussière, précipitations, brouillard, conditions atmosphériques générales (stratosphère)", "indice" : ""},
2
{"theme" : "", "question" : "  pourquoi la visibilité est-elle relative?", "réponse" : "parce qu’elle dépend de qui la regarde et dans quel direction", "indice" : ""},
3
{"theme" : "", "question" : "comment évalue-t-on la visibilité au sol le jour?", "réponse" : "avec des points de repères", "indice" : ""},
4
{"theme" : "", "question" : "comment évalue-t-on la visibilité au sol le soir?", "réponse" : "avec une lumière non focalisée", "indice" : ""},
5
{"theme" : "", "question" : "quel est la définition de la visibilité dominante?", "réponse" : " visibilité maximale commune aux sections représentant au minimum inclusif de la moitié de l’horizon en SM", "indice" : ""},
6
{"theme" : "", "question" : "  quels sont trois facteurs nécessaires pour déterminer la RVR?", "réponse" : "  visibilité du capteur, luminosité ambiante et la brillance des feux de piste", "indice" : ""},
7
{"theme" : "", "question" : " Quel est la difference entre la brume sèche et le brouillard?", "réponse" : "brume sèche n’est pas saturé", "indice" : ""},
8
{"theme" : "", "question" : " quel est le phénomène qui réduit la visibilité même par ciel clair?", "réponse" : "le voile blanc", "indice" : ""},
9
{"theme" : "", "question" : " Quel est le brouillard le plus fréquent au Québec pendant chaque saison?", "réponse" : " printemps/ été = givrage d’advection automne = par rayonnement et hiver = givre glacée ", "indice" : ""},
10
{"theme" : "", "question" : " quel est le brouillard le plus dangereux pour l’aviation?", "réponse" : " le brouillard glacée puisqu’il produit du givrage sur l’aéronef", "indice" : ""},
11
{"theme" : "", "question" : "pourquoi une inversion en stratosphère trompe la visibilité air-air ?", "réponse" : "parce qu’il n’y a aucun repère entre l’avion et le nuage", "indice" : ""},
12
{"theme" : "", "question" : " les montagnes crée un effet de (…)?", "réponse" : "  loupe 🔍 ", "indice" : ""},
13
{"theme" : "", "question" : " quel est la cause du brouillard par rayonnement?", "réponse" : "  refroidissement nocturne du sol", "indice" : ""},
14
{"theme" : "", "question" : "    Quel est la cause du brouillard par advection?", "réponse" : "  air chaud et humide se déplaçant sur une surface froide", "indice" : ""},
15
{"theme" : "", "question" : "    Quel est la cause du brouillard de pente?", "réponse" : "  air forcé de monter une pente = refroidissement ", "indice" : ""},
16
{"theme" : "", "question" : "Quel est la cause du brouillard d’évaporation/ fumée de mer arctique?", "réponse" : " air froide passant au dessus d’eau plus chaude", "indice" : ""},
17
{"theme" : "", "question" : "Quel est la cause du brouillard glacé ?", "réponse" : " Brouillard contenant des gouttelettes surfondues", "indice" : ""},
18
{"theme" : "", "question" : "Quel est la cause du brouillard frontal?", "réponse" : "chaleur de l’air réchauffe les précipitations au début du front froid et ils s’évapore (stratus)", "indice" : ""},











{"theme" : "", "question" : "?", "réponse" : "", "indice" : ""},
###

categorie = {
    "humidite" : bqhumidité,
    "rechauffement" : bqréchauffement,
    "refroidissement" : bqrefroidissement,
    "stabilite" : stabilite_air,
    "pression" : pression_atmo,
    "masse" : masse_air,
    "front" : fronts,
    "nuage" : nuage_precipitation
}