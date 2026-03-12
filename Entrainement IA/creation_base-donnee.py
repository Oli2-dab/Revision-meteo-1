import random
import pandas as pd

data = []

def rand(a, b):
    return round(random.uniform(a, b), 2)

# Classe 7
for _ in range(20):
    data.append([rand(0.95,1.00), rand(0.95,1.00), rand(0.95,1.00), 7])

# Classe 6
for _ in range(30):
    data.append([rand(0.85,0.94), rand(0.85,0.94), rand(0.85,0.94), 6])

# Classe 5
for _ in range(30):
    data.append([rand(0.75,0.84), rand(0.75,0.84), rand(0.75,0.84), 5])

# Classe 4 (prioritaire)
for _ in range(40):
    high = [rand(0.80,1.00), rand(0.80,1.00)]
    low = rand(0.00,0.69)
    
    values = high + [low]
    random.shuffle(values)
    
    data.append([values[0], values[1], values[2], 4])

# Classe 3
for _ in range(30):
    data.append([rand(0.60,0.74), rand(0.60,0.74), rand(0.60,0.74), 3])

# Classe 2
for _ in range(30):
    data.append([rand(0.20,0.59), rand(0.20,0.59), rand(0.20,0.59), 2])

# Classe 1
for _ in range(20):
    data.append([rand(0.00,0.19), rand(0.00,0.19), rand(0.00,0.19), 1])

df = pd.DataFrame(
    data,
    columns=[
        "taux_humidité",
        "taux_réchauffement",
        "taux_refroidissement",
        "résultat"
    ]
)

df = df.sample(frac=1).reset_index(drop=True)

df.to_csv("basedonne.csv", index=False)

print("Base de données créée : basedonne_IA.csv")
print("Nombre de lignes :", len(df))