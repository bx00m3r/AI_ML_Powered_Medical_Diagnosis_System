import pandas as pd
import numpy as np
import joblib

data = pd.read_csv(r"C:\B tech\internship ACITE\Dataset\prepocessed_lungs_data.csv")
print(data.head(5))
y=data.iloc[:,-1].values
x=data.iloc[:,1:-1].values

print("__________________")
print(x[:5])
print(y[:5])

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.25,random_state = 400)

print(x_test)
print(y_test)

from sklearn.ensemble import RandomForestClassifier
sc = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
sc.fit(x_train,y_train)
joblib.dump(sc,"C:/B tech/internship ACITE/lungs.pkl")

y_pred = sc.predict(x_test)

from sklearn.metrics import confusion_matrix,accuracy_score,f1_score,recall_score
print(confusion_matrix(y_test, y_pred))
print(accuracy_score(y_test, y_pred))
print(f1_score(y_test, y_pred))
print(recall_score(y_test, y_pred))