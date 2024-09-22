import pandas as pd


df = pd.read_csv('big-mac-full-index.csv')

print(df.head())

#index method

print(df.index)
''''
for index in df.index:
    print(df['date'][index],df[])
    '''
#using loc

#.index accessing each row (0, 1, 2)
'''
for index in range(len(df)):
    print(df.loc[index, 'name'])
'''
#iloc
"""

for index in range(len(df)):
    print(df.iloc[index, 0], df.iloc[index, 1])

"""

''''

#Using Iterrows r is row
for i,r in df.iterrows():
    print(r,['date'],
          r['name'])
'''
#itertuples
'''

for row in df.itertuples():
    print(getattr(row, 'date'),
      getattr(row, 'name'))
'''
#Using APPLY method

print(df.apply(lambda row: row['name'], axis = 1))