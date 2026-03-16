#   Ceci est un code pour créer une ia qui propose des recommandation basé sur les bonnes ou mauvaise réponse d'un questionnaire
#   Pour le cours de philo 2 Cchic
#   Questions basées sur les notes de cours personnelles de météo 1 du CQFA
#
#   Olivier Moreau
#

from extension.chargement_spacy import charger_spacy

val = charger_spacy()

def valrép(rj, rjeu, indice=""):
    # Nettoyage initial
    if not rj or rj.strip() == "":
        return 0

    # Supprimer l'indice de la réponse de l'utilisateur
    réponse_joueur = rj.replace(indice, "").strip().lower()
    réponse_jeu = rjeu.replace(indice, "").strip().lower() if indice else rjeu.strip().lower()

    # Si l'utilisateur n'a rien ajouté après l'indice → score 0
    if not réponse_joueur:
        return 0

    # Si la réponse est très courte (1 mot) ou identique à l'indice seul, comparer exactement
    if len(réponse_joueur.split()) <= 1:
        if réponse_joueur == réponse_jeu:
            return 2
        else:
            return 0

    # Comparaison spaCy seulement pour les phrases plus longues
    doc_joueur = val(réponse_joueur)
    doc_jeu = val(réponse_jeu)
    validité = doc_joueur.similarity(doc_jeu)

    # Score basé sur similarité
    if validité >= 0.80:
        scoreq = 2
    elif validité >= 0.40:
        scoreq = 1
    else:
        scoreq = 0

    # Codes spéciaux
    if réponse_joueur == "c2":
        scoreq = 2
    elif réponse_joueur == "c1":
        scoreq = 1
    elif réponse_joueur == "c0":
        scoreq = 0

    return scoreq