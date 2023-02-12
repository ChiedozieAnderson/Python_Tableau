# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 10:19:25 2023

@author: Ander
"""

import pandas as pd 
#file_name = pd.read_csv('file.csv') format of reading csv file
data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv', sep=';') #use the sep word when the columns are stored with ; insted of ,

#summary of the dataset
data.info()
#playing with data
var=range(10)
print(var) 
#('apple', 'pear', 'banana')
# [list], {dict}, (tuple=staic)

var1= {'name':'anderson', 'location':'nigeria'}
var2={'apple', 'pear', 'banana'}

#maths stuff for one item
CostPerItem=11.73
SellingPricePerItem=21.11
NumberOfItemsPurchased=6


ProfitPerItem=SellingPricePerItem-CostPerItem
ProfitPerTrans=ProfitPerItem*NumberOfItemsPurchased
CostPerTrans=CostPerItem*NumberOfItemsPurchased
SellingPricePerTrans=SellingPricePerItem*NumberOfItemsPurchased

#Column - aplpying them to colums
#variable = dataframe['Column_name']

CostPerItem=data['CostPerItem']
NumberOfItemsPurchased=data['NumberOfItemsPurchased']
CostPerTrans=CostPerItem*NumberOfItemsPurchased

#adding a new colum
data['CostPerTrans']=CostPerTrans
data['CostPerTrans']=data['CostPerItem']*data['NumberOfItemsPurchased'] #same as the one above

data['SalePerTrans']=data['SellingPricePerItem'] * data['NumberOfItemsPurchased']


#profit .. sale - cost
data['ProfitPerTrans'] = data['SalePerTrans'] - data['CostPerTrans']
#markup
data['Markup'] = data['ProfitPerTrans'] / data['CostPerTrans']

#Rounding markup
data['Markup'] = round(data['Markup'], 2)


#combining data fields
my_name = 'Ander' + 'Okolo' #it goes with same datatype.. doing int and str with give error, so you have to change it first

#changing the column type
day = data['Day'].astype(str)
year = data['Year'].astype(str)

print(day.dtype)
print(year.dtype)

data['Date'] = day + '-' + data['Month'] + '-' + year

#using iloc to view specific columns /rows
data.iloc[0]

data.iloc[0:3]

data.iloc[-5]
data.head(4)


data.iloc[:,2]

data.iloc[4,2]

#Spliting a colummn into many columns
#new_var = column.str.split('sep', expand = True)

split_column = data['ClientKeywords'].str.split(',', expand=True)

#creating new columns for the split columns in client keywords
data['ClientAge'] = split_column[0]
data['ClientType'] = split_column[1]
data['LengthofContract'] = split_column[2]

#using the replace function in python
data['ClientAge'] = data['ClientAge'].str.replace('[' , '')

data['LengthofContract'] = data['LengthofContract'].str.replace(']' , '')

#using the lower function to change item to lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower



seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

#merging files : 
   # merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')

#dropping columns
# df = df.drop('columnname', axis = 1)   #1 for col, 0 for row

#data = data.drop('ClientKeywords' , axis = 1)
#data = data.drop('Day', axis = 1)
#data = data.drop('Year', 'Month', axis = 1)


#export to csv
data.to_csv('ValueInc_Cleaned.csv', index = False)



















