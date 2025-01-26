#Import Library
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
import warnings
warnings.filterwarnings('ignore')

#Loading Datasets
df = pd.read_csv('hotel_bookings 2.csv')

#Exploratory Data Analysis and Data Cleaning
df.head()
#Import Library
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
import warnings
warnings.filterwarnings('ignore')

#Loading Datasets
df = pd.read_csv('hotel_bookings 2.csv')

#Exploratory Data Analysis and Data Cleaning
df.head()
print(df.head())

df.tail()
print(df.tail())

df.shape()
print(df.shape())

df.columns()
print(df.columns())

df.info()

df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])

df.describe(include = 'object')

for col in df.describe(include= 'object').columns:
    print(col)
    print(df[col].unique())
    print('_'*50)
    
df.isnull().sum()

df.drop(['company', 'agent'], axis = 1, inplace = True)
df.dropna(inplace= True)

df.isnull().sum()

df.describe()