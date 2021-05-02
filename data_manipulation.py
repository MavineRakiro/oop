"""import pandas as pd

data = pd.read_csv("titanic.csv")

print(data.head(10))
print(data.tail())

print(data.describe())

print(data.iloc[10:20])
data.head()

data.tail()
data.shape

data.columns

data.describe()
data.info()

data.iloc[0]

data.iloc[10:20]

data["Name"]
data["Age"]
data["Sex"].unique()
data["Sex"].nunique()
data["Sex"].value_counts()

data_male = data.loc[data["Sex"]=="male"]
data_male.shape

data_child = data.loc[data["Age"]<=18]
data_child.shape

data.loc[(data["Sex"]=='female') & (data["Age"]>50)].shape

mapper = {"male":1, "female":0}
data["Sex"].replace(mapper, True)

data.columns
data.rename(columns={"Name":"Person", "Sex":"Gender"}, inplace=True)
data.columns

data['Age'].()

data.info()
data.loc[data["Age"].isnull()==True, "Age"] = data["Age"].mean()

data.loc[12]
data.loc[12]

import numpy as np
data["Age"].quantile(0.75)
data.head()

data_notnull = data.loc[data["Age"].notnull()==True]
data_isnull = data.loc[data["Age"].isnull()==True]

np.percentile(data_notnull["Age"], 75)

data["Age"] = data["Age"].astype('float32')
data["Age"].dtype
data["Age"].quantile(0.75)

data.drop(["Sex"], axis=1, inplace=True)
data.head()

age = data.pop("Age")
age
data.head(2)
data.drop(data.columns[0], axis=1)
data.shape
data = data.drop_duplicates()
data.shape

data.shape
data.groupby("Survived").count()
data.groupby("Survived").mean()

data.groupby("Survived")["Age"].mean()
data["PClass"].value_counts()

data.head()
data["Name"].nunique()
extract_titles = lambda x : x.split(",")[-1].split()[0]
data["Name"] = data["Name"].astype("string")
data.Name.dtype
data["Titles"] = data["Name"].apply(extract_titles)

data["Titles"].value_counts()

/////

import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import Normalizer
data = np.array([
    [4598.45],
    [3900.8],
    [2267],
    [1198.765],
    [260.67]
])
#rescaling (x1 scaled = (x1 - min val)/(Max - Min val) )
minmax_scaler = preprocessing.MinMaxScaler(feature_range = (0,5))

scaled_data = minmax_scaler.fit_transform(data)
print(scaled_data)


#standardizing (default)- mean = 0 and standard deviation = 1
#principal component analysis often works better using standardization, while min-max scaling is often recommended for neural net‐ works

standard_scaler = preprocessing.StandardScaler()

standard_data = standard_scaler.fit_transform(data)
print(standard_data)


# standardization using median and quartile range

robust_scaler = preprocessing.RobustScaler()

robust_data = robust_scaler.fit_transform(data)

print(robust_data)

#Normalization - range of [0,1]

normalizer = Normalizer(norm='l1')

print(normalizer.transform(data))

#Polynomial features

from sklearn.preprocessing import PolynomialFeatures

polynomial_interaction = PolynomialFeatures(degree = 2, include_bias=False)

polynomial_data = polynomial_interaction.fit_transform(data)
print(polynomial_data)

from sklearn.preprocessing import FunctionTransformer

def sq(x):
    return x ** 2

sq_value = preprocessing.FunctionTransformer(sq)

sq_data = sq_value.fit_transform(data)
print(sq_data)





import pandas as pd
import  numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

houses = pd.read_csv("kc_house_data.csv")

print(houses.head())

print(houses.info())

print(houses['grade'][:3])

#correlations = houses.corr()
#sns.heatmap(correlations, annot = True)

#plt.show()

plt.title("House Price vs Squared feet.")
plt.xlabel("squared feet")
plt.ylabel("House price(in millions)")
sns.scatterplot(x = 'sqft_living', y = 'price', data = houses)

#plt.show()

from sklearn.model_selection import train_test_split

x =houses[['sqft_living']]

y = houses['price']

x_train, x_test, y_train,y_test = train_test_split(x,y)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
linreg = lr.fit(x_train, y_train)

print(linreg.intercept_)
print(linreg.coef_)

plt.plot(x_train, linre.coef_ * x_train + linreg.intercept_,
 '-r', label = 'Intercept: -39,163 \n Slope: 279.4')
 
plt.show()

#print(linreg.predict(x_train[0]))





from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
import pandas as pd

boston = load_boston()
features = boston.data[:, 0:2]
target = boston.target

house = pd.read_csv("kc_house_data.csv")
house_data = house[:3]

print(features)
print(house_data.head())

regression = LinearRegression()

model = regression.fit(features, target)


print(regression.intercept_)
print(regression.coef_)

print(model.intercept_)
print(model.coef_)

print(target[0]*1000)

print(model.predict(features)[0]*1000)

print(model.coef_[0]*1000)

from sklearn.preprocessing import PolynomialFeatures

interaction = PolynomialFeatures(degree=3, include_bias=False, interaction_only=True)
features_interaction = interaction.fit_transform(features)

regression_ = LinearRegression()

model_ = regression_.fit(features_interaction, target)

print(features[0])

import numpy as np

interaction_term = np.multiply(features[:, 0], features[:, 1])

print(interaction_term[0])
print(features_interaction[0])

#modeling a nonlinear relationship using polynomial features. that is polynomial regression
features = boston.data[:, 0:1]

polynomial = PolynomialFeatures(degree=3, include_bias=False)
features_polynomial  = polynomial.fit_transform(features)

regression = LinearRegression()

model = regression.fit(features_polynomial, target)

print(model.coef_)
print(model.intercept_)

print(features[0])
print(features[0]**2)
print(features[0]**3)
print(features_polynomial[0])

#reducing variance of linear regression model. using ridge and then lasso regression

from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler

boston = load_boston()
features = boston.data
target = boston.target

scaler = StandardScaler()
features_standardized = scaler.fit_transform(features)

regression = Ridge(alpha = 0.5)
model = regression.fit(features_standardized, target)

from sklearn.linear_model import RidgeCV

regr_cv = RidgeCV(alphas = [0.1, 1.0, 10.0])
model_cv = regr_cv.fit(features_standardized, target)

print(model_cv.coef_)

print(model_cv.alpha_)

from sklearn.linear_model import Lasso

regression = Lasso(alpha=0.5)
model = regression.fit(features_standardized, target)

print(model.coef_)

regression_a10 = Lasso(alpha = 10.0)
model_a10 = regression_a10.fit(features_standardized, target)

print(model_a10.coef_)
"""