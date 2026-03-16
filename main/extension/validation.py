#   Ceci est un code pour créer une ia qui propose des recommandation basé sur les bonnes ou mauvaise réponse d'un questionnaire
#   Pour le cours de philo 2 Cchic
#   Questions basées sur les notes de cours personnelles de météo 1 du CQFA
#
#   Olivier Moreau
#

from extension.chargement_spacy import charger_spacy

val = charger_spacy()

def valrép(rj, rjeu, indice):
    if not rj or rj.strip() == "":
        return 0

    réponse_joueur = rj.replace(indice, "").strip().lower()
    réponse_jeu = rjeu.replace(indice, "").strip().lower()

    if not réponse_joueur:
        return 0

    pourvalrj = val(réponse_joueur)
    pourvalrjeu = val(réponse_jeu)
    validité = pourvalrj.similarity(pourvalrjeu)

    if validité >= 0.80:
        scoreq = 2
    elif validité >= 0.40:
        scoreq = 1
    else:
        scoreq = 0

    if réponse_joueur == "c2":
        scoreq = 2
    elif réponse_joueur == "c1":
        scoreq = 1
    elif réponse_joueur == "c0":
        scoreq = 0

    return scoreq