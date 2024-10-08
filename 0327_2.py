# 논문 관리형

# https://www.zotero.org/download/
# Logseq 설정-기능에서 연동 가능

# https://endnote.com/



import pandas as pd

data = pd.read_csv("C:/Users/print/Downloads/tb.csv")

data

data.info()

data = pd.read_csv("C:/Users/print/Downloads/data/pew.txt", sep='\t')

data.loc[3, '$10-20k']

data.melt

data.melt('religion')

# data.set_index('religion').unstack().reset_index_index()

data

data.info()

data_melt = data.melt('religion')

data_melt

data_melt.groupby('religion')[['value']].mean()

data = pd.read_csv("C:/Users/print/Downloads/data/billboard.csv")

data

data.info()

data.columns

data.columns[:7]

data.melt(data.columns[:7])

data.melt(data.columns[:7]).dropna

data_bilboard = data.melt(data.columns[:7]).dropna()

data_bilboard.variable

data_bilboard.variable.str.extract('(Wd+)')

data_bilboard = data.melt(data.columns[:7], var_name = 'A', value_name = 'B')

data_bilboard

data = pd.read_csv("C:/Users/print/Downloads/tb.csv")

data

data.melt

data.melt(['iso2', 'year'])

data.melt(['iso2', 'year']).dropna()

data_tb = data.melt(['iso2', 'year']).dropna()

data_tb.variable.value_counts()

data_a = data.melt(data.columns[:2], var_name = 'A')

data_a

data_tb.variable.map(lambda x: 'U' if x == 'new sp' else x)

data_tb.variable.map(lambda x: 'F' if x.startswith('new_sp_f') else 'M' if x.startswith('new_sp_m') else 'U')

data = pd.read_csv("C:/Users/print/Downloads/data/weather.txt", sep='\t')

data.info()

data

data.melt(['id', 'year', 'month', 'element'])

# stack, unstack

data_weather = data.melt(['id', 'year', 'month', 'element']).dropna()

data_weather.drop(columns='variable').set_index(['id','year','month','element'])

data_weather.drop(columns='variable').set_index(['id','year','month','element']).unstack() # ERROR

data_weather.drop(columns=['id','variable']).set_index(['year','month','element']).unstack() # ERROR

data_weather.drop(columns=['id','year','month','element','variable']).set_index([]).unstack() # ERROR

data_weather.drop(columns=['id','year','month','element'])

temp = data_weather.drop(columns=['id','year','month','variable'])

temp.set_index('element', drop = False)

temp.set_index('element', drop = True)

data_weather.set_index(['id','year','element','month'])

data_weather.set_index(['id','year','element','month', 'variable']).unstack(0)

data_weather.set_index(['id','year','element','month', 'variable']).unstack(1)

data = pd.read_csv("C:/Users/print/Downloads/data/pew.txt", sep='\t')

data

data.set_index('religion').stack().reset_index()



import seaborn as sns

tips = sns.load_dataset("tips")

tips

import pandas as pd
import numpy as np
from itertools import groupby

tips.groupby(['tip', 'sex'])

tips.groupby(['day', 'smoker'])

tips['tip_pct'] = tips['tip'] / tips['total_bill']

tips



tips = tips.melt(['total_bill', 'tip', 'sex'])

tips

# tips.groupby(['tip', 'sex']).mean()
# tips.groupby(['tip', 'sex']).mean().plot.bar(stacked=True)
# tips.groupby(['sex', 'day'])[['size']]
# tips.groupby(['sex', 'day'])[['tip']].std()
# tips.groupby(['sex', 'day'])[['tip']].aggregate(['mean', 'std'])



tips = pd.read_csv("C:/Users/print/Downloads/tips.csv")
tips.head()

tips['tip_pct'] = tips['tip'] / tips['total_bill']
tips.head()

grouped = tips.groupby(['day', 'smoker'])

grouped_pct = grouped['tip_pct']

grouped_pct.agg('mean')

grouped_pct.agg(['mean', 'std'])

grouped_pct.agg([('평균', 'mean'), ('표준편차', np.std)])

functions = ['count', 'mean' ,'max']
result = grouped[['tip_pct', 'total_bill']].agg(functions)
result

result['tip_pct']

ftuples = [('평균', 'mean'), ('분산', np.var)]

grouped[['tip_pct', 'total_bill']].agg(ftuples)

grouped.agg({'tip': np.max, 'size': 'sum'})

grouped.agg({'tip_pct': ['min', 'max', 'mean'], 'size': 'sum'})

tips.groupby(['day', 'smoker']).mean()



