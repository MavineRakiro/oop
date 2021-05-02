import pandas as pd
import numpy as np


data = pd.read_csv("titanic.csv")
print(data.head())
print(data.tail(10))
#default head and tail print out 5 rows.
print(data.columns)

print(data['Name'][:3])
#print(data.Name[:3])
print(data[['Name', 'Age', 'Fare', 'Cabin', 'Embarked']][:3])

print(data.iloc[1:4])
print(data.iloc[1:4, 2])

data1 = data.loc[data['Survived'] == 1]
print(data1.shape)

data2 = data.loc[(data['Survived'] == 1) & (data['Pclass'] == 1)]
#The or operator is |

print(data2.shape)
print(data.describe())
print(data.info())

print(data.sort_values(['Name', 'Fare'])[:11])

print(list(data.columns))

data2.to_csv('Manipated_Data.csv')
print(data.groupby(['Fare']).mean())
#replace mean with count and see what happens


for i in pd.read_csv('titanic.csv', chunksize = 20):
    print(i.shape)
    
import this
print(dir(this))