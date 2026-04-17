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
import joblib

iris = load_iris()
x = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

rf_model = RandomForestClassifier()
rf_model.fit(X_train, y_train)
prédiction = rf_model.predict(X_test)
accuracy = accuracy_score(y_test, prédiction)
print(accuracy)

model_filename = "Test_base_de_donne.joblib"

joblib.dump(rf_model, model_filename)

loaded_model = joblib.load("Test_base_de_donne.joblib")

new_data_point = [[5.1, 3.5, 1.4, 0.2]]

prédiction = loaded_model.predict(new_data_point)

print(prédiction)