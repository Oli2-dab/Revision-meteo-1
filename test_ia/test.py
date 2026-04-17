import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score

donné = pd.read_csv("basedonne.csv")
x = donné[["taux_humidité", "taux_réchauffement", "taux_refroidissement"]]
y = donné["résultat"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model = RandomForestClassifier(random_state = 42)
model.fit(x_train, y_train)
prédiction = model.predict(x_test)
accuracy = accuracy_score(y_test, prédiction)
print(accuracy)



param_grid = {
    "alpha" : [0.1, 1, 10, 100]
}

grid_shearch = GridSearchCV(model, param_grid, cv = 2)
grid_shearch.fit(x_train, y_train)

print(grid_shearch. best_params_)

best_alpha = grid_shearch.best_params_["alpha"]
best_modal = Ridge(alpha = best_alpha)

best_modal.fit(x_train, y_train)

prédiction = best_modal.predict(x_test)

r2 = r2_score(y_test, prédiction)
print(r2)