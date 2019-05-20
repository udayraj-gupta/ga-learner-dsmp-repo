# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#Code starts here
data = pd.read_csv(path)
data['Rating'].hist()
data = data[data['Rating']<=5]
data['Rating'].hist()

#Code ends here


# --------------
# code starts here
total_null = data.isnull().sum()
percent_null = (total_null/data.isnull().count())*100
missing_data = pd.concat([total_null,percent_null],axis=1,keys=['Total','Percentage'])
print(missing_data)

data = data.dropna()
total_null_1 = data.isnull().sum()
percent_null_1 = (total_null_1/data.isnull().count())*100
missing_data_1 = pd.concat([total_null_1,percent_null_1],axis=1,keys=['Total','Percentage'])
print(missing_data_1)
# code ends here


# --------------

#Code starts here

a = sns.catplot(x='Category',y='Rating',data=data, kind="box", height = 10)
a.set_xticklabels(rotation=90)
a.set_titles('Rating vs Category [BoxPlot]')

#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here
le = LabelEncoder()
#data['Installs'] = data['Installs'].str.replace(',','').str.replace('+','')
data['Installs'] = data['Installs'].apply(lambda x : x.replace(',','')).apply(lambda x : x.replace('+',''))
data['Installs'] =data['Installs'].astype(int)
print(data['Installs'])
data['Installs'] = le.fit_transform(data['Installs'])
a = sns.regplot(x="Installs", y="Rating" , data=data)
a.set_title('Rating vs Installs [RegPlot]')


#Code ends here



# --------------
#Code starts here
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
import seaborn as sns
#Code starts here
d=data['Price'].value_counts()
print(d)
data['Price']=data['Price'].apply(lambda x : x.replace('$',''))
d=data['Price'].value_counts()
print(d)
data['Price']=data['Price'].astype(float)
#le=LabelEncoder()
#data['Installs'] = le.fit_transform(data['Installs'])
y=sns.regplot(data=data,x='Price',y='Rating')
y.set_title('Rating vs Installs [RegPlot]')


#Code ends here


# --------------
#Code starts here

data['Genres']=data['Genres'].str.split(';').str[0]
#print(data['Genres'])
df=data[['Genres','Rating']]
gr_mean=df.groupby(['Genres'],as_index=False).mean()


gr_mean=gr_mean.sort_values(by=['Rating'])
gr_mean=pd.DataFrame(gr_mean)
print(gr_mean)#,gr_mean[-1,:])
#Code ends heree


# --------------

#Code starts here

import seaborn as sns
data['Last Updated'] = pd.to_datetime(data['Last Updated'])
print(data['Last Updated'].max())
max_date=data['Last Updated'].max()
data['Last Updated Days']=max_date-data['Last Updated']
data['Last Updated Days']=data['Last Updated Days'].dt.days

sns.regplot(data=data,x='Last Updated Days',y='Rating').set_title('Rating vs Last Updated [RegPlot]')

#Code ends here


