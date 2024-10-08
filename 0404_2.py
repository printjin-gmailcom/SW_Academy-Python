# https://www.kaggle.com/competitions/titanic



import seaborn as sns

from sklearn.datasets import fetch_openml

titanic = sns.load_dataset('titanic')

titanic_sk=fetch_openml('titanic')

titanic_sk

titanic_sk.frame

titanic_sk=fetch_openml('titanic', version=1)

titanic_sk

titanic_sk.frame

titanic

titanic.info()

titanic.isna().any()

titanic.columns[titanic.isna().any()]

titanic[titanic.isna().any()]

titanic.isna().any().index

titanic.isna().all()

titanic.age

titanic.age.isna()

sum(titanic.age.isna())

t = titanic.age.isna()

t.sum(skipna=True)

t.sum(skipna=False)

tiatanic.age.sum(skipna=False)

import missingno as mimo

mimo.matrix(titanic)

titanic.drop(columns='deck')

titanic[titanic.embarked.isna()]

titanic.embarked

titanic[titanic.embarked.isna()].embarked.fillna(0)

t.fillna

titanic[titanic.embarked.isna()].embarked.fillna([0,1])

titanic[titanic.embarked.isna()].embarked.fillna({61:0, 829:3})

tt = titanic[titanic.embarked.isna()].embarked

titanic.embarked.value_counts()

tt.fillna({61:0, 829:3})

titanic[titanic.embarked.isna()].embarked.fillna(method='bfill')

titanic.loc[58:63].embarked.fillna(method='bfill')

titanic.loc[58:63].embarked.fillna(method='pad')

titanic.loc[58:63].embarked.map(lambda x: 0 if x==None else x)

mimo.matrix(tiatanic)

titanic.loc[58:63].embarked.map(lambda x: 0 if x==np.nan else x)

mimo.matrix(tiatanic)

titanic.loc[58:63].embarked.map(lambda x: 0 if x is None else x)

mimo.matrix(tiatanic)

import numpy as np

x = np.ma.array([1,2,3], mask=[True, False, True])

x

x.count()

x.mask

x.sum()



titanic.loc[58:63].embarked.map(lambda x: 0 if x == float('nan') else x)

mimo.matrix(tiatanic)

titanic.loc[58:63].embarked.map(lambda x: 0 if x.isna() else x)

titanic.embarked.value_counts().index.values



from sklearn.impute import SimpleImputer

si = SimpleImputer()

si.fit(titanic.age)

si.fit(titanic.age.reshape(1, -1))

si.fit(tiatanic[['age']])

si.transform(tiatanic[['age']])

si.fit_transform(tiatanic[['age']])

from sklearn.impute import KNNImputer

k = KNNImputer()

# 인스턴스화 하기

k.fit_transform(titanic[['age']])

from sklearn.experimental import enable_iterative_imputer

from sklearn.impute import IterativeImputer

import pandas as pd

pd.NA

titanic.loc[58:63].embarked.map(lambda x: 0 if x==1 else x)

titanic.loc[58:63].embarked.map(lambda x: 0 if x==pd.NA else x)



tips = sns.load_dataset('tips')

tips

tips.dtypes

tips.sex.value_counts()

tips.sex.map({'Male':0, 'Femaile':1})

tips.sex.cat.codes

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

le.fit_transform(tips.sex)

le.inverse_transform([0])

iris = sns.load_dataset('iris')

iris



from sklearn.preprocessing import OrdinalEncoder

le = OrdinalEncoder()

le.fit_transform(tips[['sex']])



# one-hot encoder

tips.sex.str.get_dummies()

tips.day.str.get_dummies()

# multi-hot

from sklearn.preprocessing import OneHotEncoder

one = OneHotEncoder()

one.fit_transform(tips.sex)

one.fit_transform(tips[['sex']])

one.inverse_transform([[0,1]])

from sklearn.datasets import load_iris

data = load_iris(as_frame=True)

iris = data.frame

from sklearn.naive_bayes import GaussianNB

gb = GaussianNB()

gb.fit(iris.iloc[:,:-1], iris.target)

iris.iloc[:,:-1].columns

gb.predict([[1,2,3,2]])

data.target_names



# training data, test set

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(iris.iloc[:,:-1], iris.target)

gb.fit(X_train, y_train)

gb.predict(X_test) == y_test

(gb.predict(X_test) == y_test).sum()

len(y_test)

# hold-out

# occam's razer



