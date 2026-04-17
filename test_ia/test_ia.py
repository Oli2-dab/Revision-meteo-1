from sklearn.datasets import load_iris
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

iris = load_iris()
data = iris.data
target = iris.target
print(data)
print(target)
print("Feature Names", iris.feature_names)
print("Target", iris.target_names)
print("Data shape", data.shape)

##df = pd.DataFrame(data, columns = iris.feature_names)
##df["Targets"] = target
##df.isnull().sum()

##scaler = MinMaxScaler()
##normdata = scaler.fit_transform(data)

##scaler2 = StandardScaler()
##scaleddata = scaler2.fit_transform(data)
##X_train, X_test, y_train, y_test = train_test_split(data, target, test_size = 0.2)

##knn = KNeighborsClassifier(n_neighbors=2)
##knn.fit(X_train, y_train)
##prediction = knn.predict(X_test)
##accuracy = accuracy_score(y_test, prediction)

##score = precision_score(y_test, prediction, average="weighted")
##rapelle = recall_score(y_test, prediction, average="weighted")
##f1 = f1_score(y_test, prediction, average="weighted")
##confusion = confusion_matrix(y_test, prediction)



####y = data[:,0]
####X_train, X_test, y_train, y_test = train_test_split(data, y, test_size=0.2)

####reg_model = LinearRegression()
####reg = reg_model.fit(X_train, y_train)
####prédiction = reg.predict(X_test)
####erreur = mean_squared_error(y_test, prédiction)
####score = r2_score(y_test, prédiction)
####print(score)