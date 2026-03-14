import random
import pandas as pd

data = []

def rand(a, b):
    return round(random.uniform(a, b), 2)

# Classe 7
for _ in range(200):
    data.append([rand(0.95,1.00), rand(0.95,1.00), rand(0.95,1.00), rand(0.95,1.00), rand(0.95,1.00), rand(0.95,1.00), rand(0.95,1.00), rand(0.95,1.00), 7])

# Classe 6
for _ in range(300):
    data.append([rand(0.85,0.94), rand(0.85,0.94), rand(0.85,0.94), rand(0.85,0.94), rand(0.85,0.94), rand(0.85,0.94), rand(0.85,0.94), rand(0.85,0.94), 6])

# Classe 5
for _ in range(300):
    data.append([rand(0.75,0.84), rand(0.75,0.84), rand(0.75,0.84), rand(0.75,0.84), rand(0.75,0.84), rand(0.75,0.84), rand(0.75,0.84), rand(0.75,0.84), 5])

# Classe 4 (prioritaire)
for _ in range(400):
    high = [rand(0.80,1.00), rand(0.80,1.00), rand(0.80,1.00), rand(0.80,1.00), rand(0.80,1.00), rand(0.80,1.00), rand(0.80,1.00)]
    low = rand(0.00,0.69)
    
    values = high + [low]
    random.shuffle(values)
    
    data.append([values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], 4])

# Classe 3
for _ in range(300):
    data.append([rand(0.60,0.74), rand(0.60,0.74), rand(0.60,0.74), rand(0.60,0.74), rand(0.60,0.74), rand(0.60,0.74), rand(0.60,0.74), rand(0.60,0.74), 3])

# Classe 2
for _ in range(300):
    data.append([rand(0.20,0.59), rand(0.20,0.59), rand(0.20,0.59), rand(0.20,0.59), rand(0.20,0.59), rand(0.20,0.59), rand(0.20,0.59), rand(0.20,0.59), 2])

# Classe 1
for _ in range(200):
    data.append([rand(0.00,0.19), rand(0.00,0.19), rand(0.00,0.19), rand(0.00,0.19), rand(0.00,0.19), rand(0.00,0.19), rand(0.00,0.19), rand(0.00,0.19), 1])

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