import pandas as pd
import numpy as np
import joblib

data = pd.read_csv(r"C:\B tech\internship ACITE\Dataset\diabetes_prediction_dataset.csv")
print(data.head())

from sklearn.preprocessing import LabelEncoder
LE = LabelEncoder()
data.iloc[:,0] = LE.fit_transform(data.iloc[:,0]) 
x=data.iloc[:,:-1]
y=data.iloc[:,-1]

print(x.head())
print(y.head())

#print(data.head())
distinct_count = x['smoking_history'].nunique()
print(f'smoking_history = {distinct_count}')
print(x.isnull().sum())

x = pd.get_dummies(x, columns=['smoking_history'], dtype=int)
print(x.columns)

# Count occurrences of each unique value
value_counts = data['diabetes'].value_counts()
print(value_counts)

x,y=x.values,y.values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=400)

print(x_test)
print(y_test)

from sklearn.ensemble import RandomForestClassifier
sc = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
sc.fit(x_train,y_train)
joblib.dump(sc,"C:/B tech/internship ACITE/diabetes.pkl")

y_pred = sc.predict(x_test)

from sklearn.metrics import confusion_matrix,accuracy_score,f1_score,recall_score
print(confusion_matrix(y_test, y_pred))
print(accuracy_score(y_test, y_pred))
print(f1_score(y_test, y_pred))
print(recall_score(y_test, y_pred))