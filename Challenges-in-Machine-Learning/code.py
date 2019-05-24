# --------------
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Code starts here
df = pd.read_csv(path)
print(df.head())
print(df.info())
cols = ['INCOME','HOME_VAL','BLUEBOOK','OLDCLAIM','CLM_AMT']
for x in cols:
    print(x)
    df[x] = df[x].str.replace('$','').str.replace(',','')

X = df.drop(['CLAIM_FLAG'],1)
y = df['CLAIM_FLAG']
count = y.count()
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3,random_state = 6)


# Code ends here


# --------------
# Code starts here

for x in cols:
    print(x)
    X_train[x] = X_train[x].astype(float)
    X_test[x] = X_test[x].astype(float)
X_train.isna().sum()
X_test.isna().sum()
# Code ends here


# --------------
# Code starts here


X_train.dropna(subset=['YOJ','OCCUPATION'],inplace=True)
X_test.dropna(subset=['YOJ','OCCUPATION'],inplace=True)
y_train = y_train[X_train.index]
y_test = y_test[X_test.index]
cols = ['AGE','CAR_AGE','INCOME','HOME_VAL']
for x in cols:
    print(x)
    X_train[x].fillna((X_train[x].mean()), inplace=True)
    X_test[x].fillna((X_test[x].mean()), inplace=True)

# Code ends here


# --------------
from sklearn.preprocessing import LabelEncoder
columns = ["PARENT1","MSTATUS","GENDER","EDUCATION","OCCUPATION","CAR_USE","CAR_TYPE","RED_CAR","REVOKED"]

# Code starts here
le = LabelEncoder()
for x in columns:
    X_train[x] = le.fit_transform(X_train[x].astype(str))
    X_test[x] = le.fit_transform(X_test[x].astype(str))

# Code ends here



# --------------
from sklearn.metrics import precision_score 
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression



# code starts here 
model = LogisticRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
score = model.score(X_test, y_test)
precision = precision_score(y_test, y_pred)


# Code ends here


# --------------
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE

# code starts here

smote = SMOTE(random_state=9)
X_train,y_train = smote.fit_sample(X_train, y_train)
scaler = StandardScaler()
scaler.fit_transform(X_train) 

# Code ends here


# --------------
# Code Starts here
model = LogisticRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
score = model.score(X_test, y_test)
print(score)
# Code ends here


