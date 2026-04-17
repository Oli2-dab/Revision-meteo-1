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

iris = load_iris()
data = iris.data
target = iris.target

X_train, X_test, y_train, y_test = train_test_split(data, target, test_size = 0.3)

dt_classifier = RandomForestClassifier()
dt_classifier = dt_classifier.fit(X_train, y_train)
prédictions = dt_classifier.predict(X_test)
accuracy  = accuracy_score(y_test, prédictions)
print(accuracy)
param_grid = {
    "n_estimators" : [50, 150, 200, 250],
    "max_depth" : [None, 10, 20, 30]
}
grid_search = GridSearchCV(dt_classifier, param_grid, cv = 3)
grid_search. fit(X_train, y_train)

print(grid_search.best_params_)

best_estimator = grid_search.best_params_["n_estimators"]
best_depth = grid_search.best_params_["max_depth"]
best_dt_class = RandomForestClassifier(n_estimators = best_estimator, max_depth = best_depth)
best_dt_class.fit(X_train, y_train)

prediction = best_dt_class.predict(X_test)
print(accuracy_score(y_test, prediction))