from sklearn.datasets import load_iris
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import Ridge

iris = load_iris()
data = iris.data
target = iris.target

X_train, X_test, y_train, y_test = train_test_split(data, target, test_size = 0.3)

ridge_model = Ridge()
ridge_model.fit(X_train, y_train)

prédiction = ridge_model.predict(X_test)

avant_mean = mean_squared_error(y_test, prédiction)

avant_r2 = r2_score(y_test, prédiction)

print(avant_mean)
print(avant_r2)

param_grid = {
    "alpha" : [0.1, 1, 10, 100]
}

grid_shearch = GridSearchCV(ridge_model, param_grid, cv = 2)
grid_shearch.fit(X_train, y_train)

print(grid_shearch. best_params_)

best_alpha = grid_shearch.best_params_["alpha"]
best_modal = Ridge(alpha = best_alpha)

best_modal.fit(X_train, y_train)

prédiction = best_modal.predict(X_test)

mean = mean_squared_error(y_test, prédiction)
r2 = r2_score(y_test, prédiction)

print(mean)
print(r2)