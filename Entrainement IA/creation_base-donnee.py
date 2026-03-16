import random
import pandas as pd

data = []

def rand(a, b):
    return round(random.uniform(a, b), 2)

def génération(nb_ligne, high_range, résultat, nb_donnée = 8, manquante = 0):
    
    for _ in range(nb_ligne):

        taux_avec_résultat = [rand(*high_range) for _ in range(nb_donnée - manquante)]
        valeures_manquantes = [2.00] * manquante

        values = taux_avec_résultat + valeures_manquantes
        random.shuffle(values)

        data.append(values + [résultat])

def génération_4(nb_ligne, manquante=0):

    for _ in range(nb_ligne):

        high = [rand(0.80,1.00) for _ in range(7-manquante)]
        low = rand(0.00,0.69)

        values = high + [low] + [2.00]*manquante
        random.shuffle(values)

        data.append(values + [4])

# Résultat 7
génération(200, (0.95,1.00), 7)

# Résultat 6
génération(300, (0.85,0.94), 6)

# Résultat 5
génération(300, (0.75,0.84), 5)

# Résultat 4 (1 erreur)
for _ in range(400):

    high = [rand(0.80,1.00) for _ in range(7)]
    low = rand(0.00,0.69)

    values = high + [low]
    random.shuffle(values)

    data.append(values + [4])

# Résultat 3
génération(300, (0.60,0.74), 3)

# Résultat 2
génération(300, (0.20,0.59), 2)

# Résultat 1
génération(200, (0.00,0.19), 1)



# Résultat 7 avec thèmes manquants
for nb_manquant in range(1,7):
    génération(200, (0.95,1.00), 7, manquante = nb_manquant)

# Résultat 6 avec thèmes manquants
for nb_manquant in range(1,7):
    génération(300, (0.85,0.94), 6, manquante = nb_manquant)

# Résultat 5 avec thèmes manquants
for nb_manquant in range(1,7):
    génération(300, (0.75,0.84), 5, manquante = nb_manquant)

# Résultat 4 avec thèmes manquants
for nb_manquant in range(1,7):
    génération_4(400, manquante = nb_manquant)

# Résultat 3 avec thèmes manquants
for nb_manquant in range(1,7):
    génération(300, (0.60,0.74), 3, manquante = nb_manquant)

# Résultat 2 avec thèmes manquants
for nb_manquant in range(1,7):
    génération(300, (0.20,0.59), 2, manquante = nb_manquant)

# Résultat 1 avec thèmes manquants
for nb_manquant in range(1,7):
    génération(200, (0.00,0.19), 1, manquante = nb_manquant)

base_de_donne = pd.DataFrame(
    data,
    columns=[
        "taux_humidité",
        "taux_réchauffement",
        "taux_refroidissement",
        "taux_stabilite",
        "taux_pression",
        "taux_masse",
        "taux_front",
        "taux_nuage",
        "résultat"
    ]
)

base_de_donne = base_de_donne.sample(frac=1).reset_index(drop=True)

base_de_donne.to_csv("base_donne_a_valider.csv", index=False)

print("Base de données créée : base_donne_a_valider.csv")
print("Nombre de lignes :", len(base_de_donne))