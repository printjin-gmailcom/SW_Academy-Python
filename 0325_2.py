import pandas as pd

# data.go.kr - 소상공인시장진흥공단_상가(상권)정보 260mg

data = pd.read_csv("C:/Users/print/Downloads/seoul.csv")

data

data.info()

data.dtypes

data.head()

data.tail()

data.sample()

# indexing 과 slicing

dir(data)

data



import seaborn as sns

iris = sns.load_dataset('iris')

iris



data[['상호명', '상가업소번호']]

data['상호명']

data.상호명

data.select_dtypes('object')

data.select_dtypes(['object', 'float64'])

data.filter(regex='^상권')

data.filter(like='분류')



tips = sns.load_dataset('tips')

tips.size



iris.iloc[3]

iris.iloc[3:10]

iris.iloc[3:10].iloc[1:4]

iris.loc[3]

iris.loc[3:10, 'sepal_length':'sepal_width']

iris.iloc[3:10,1:3]

iris.iat[3,3]

iris.iat[3,3] = 1

iris.iat[3,3]

iris.iloc[3:10,3]

iris.iloc[3:10,1:3] = 3

iris.iloc[3:10,1:3]



data['상권업종대분류명'] == '음식'

data[data['상권업종대분류명'] == '음식']

data[(data['상권업종대분류명'] == '음식')&(data['상권업종소분류명'] == '카페')]

data[(data['상권업종대분류명'] == '음식')|(data['상권업종소분류명'] == '카페')]



