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

iris = load_iris()
data = iris.data
target = iris.target

X_train, X_test, y_train, y_test = train_test_split(data, target, test_size = 0.3)

knn = KNeighborsClassifier()
knnfit = knn.fit(X_train, y_train)
prédiction = knn.predict(X_test)
print(accuracy_score(y_test, prédiction))

param_grid = {"n_neighbors" : range(1,30)}
grid_search = GridSearchCV(knn, param_grid, cv = 2)
grid_search.fit(X_train, y_train)
best_k = grid_search.best_params_["n_neighbors"]
best_knn = KNeighborsClassifier(n_neighbors = best_k)
best_knn.fit(X_train, y_train)
prédiction = best_knn.predict(X_test)
accuracy = accuracy_score(y_test, prédiction)
print(accuracy)