# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 10:06:33 2023

@author: Ander
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#method 1 to read json data
json_file = open('loan_data_json.json')
data =json.load(json_file)

#method 2 to read json file
with open ('loan_data_json.json') as json_file:
    data = json.load(json_file)
    
#transform to dataframe
loandata = pd.DataFrame(data)

#finging unique values
loandata['purpose'].unique()

#describing the data
loandata.describe()

#describe data of a specfici column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()


#using exp()to get annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annualincome'] = np.exp(loandata['log.annual.inc'])

#working with array
arr = np.array([1,2,3,4])

#1D array
arr = np.array[1]

#2D array
arr = np.array([[1,2,3,4], [2,3,4,5]])

#working with if statments
a = 40
b= 500

if b > a:
    print('b is gretaer than a')
    
#more conditions
a =40
b=500
c=1000
    
if b > a and b < c:
    print('b is greater than a but less than c')
    
#if conditions are not met
a =40
b=500
c=20

if b > a and b < c:
    print('b is greater than a but less than c')
else: 
    print('no conditions met')
    
    
#another conditon metries
a =40
b=0
c=30
if b > a and b < c:
    print('b is greater than a but less than c')
elif b > a and b > c:
    print('b is greater than a and c')
else: 
    print('no conditions met')
    
    
#using or 
a=40
b=500
c=30

if b > a or b < c:
    print('b is greater than a or less than c')
else: 
    print('no conditions met')
    
    
fico = 400

if fico >= 300 and fico < 400:
    ficocat = 'Very Poor'
elif fico >= 400 and fico  < 600:
    ficocat = 'Poor'
elif fico >= 601 and fico  < 660:
    ficocat = 'Fair'
elif fico >= 660 and fico  < 700:
    ficocat = 'Good'    
elif fico >= 700:
    ficocat = 'Excellent'
else:
    ficocat = 'Unknkown'
print(ficocat)
    


#for loop
fruits = ['apple', 'pear', 'banana', 'cherry']

for x in fruits:
    print(x)
    y=x+' fruits'
    print(y)

for x in range(0,4):
    y= fruits[x]+' for sale'
    print(y)
    
#applying the logic of loop to loandata

length = len(loandata)
ficocat = []
for x in range(0, length):
    category = loandata['fico'][x]
    
    try:
        
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif category >= 400 and category  < 600:
            cat = 'Poor'
        elif category >= 601 and category  < 660:
            cat = 'Fair'
        elif category >= 660 and category  < 700:
            cat = 'Good'    
        elif category >= 700:
            cat = 'Excellent'
        else:
            cat = 'Unknkown'
    except:
        cat = 'Unknown'
        
    ficocat.append(cat)
    

ficocat = pd.Series(ficocat)
loandata['fico.category'] = ficocat


# #whiel loops
# i=1
# while i < 10:
#     print(i)
#     i = i + 1

#df.loc as conditional stataments
# df.loc[df[col_name] condition, newcol_name] = 'value if the condition is met'

# for int rate, a new col is wanted. rate > 0.12 is high, else low

loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'
 
#number of loans/row by fico.category

catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color = 'green', width = 0.1)
plt.show()


purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color = 'red', width = 0.3)
plt.show()

#scatter plots
ypoint = loandata['annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color = '#4caf50')
plt.show()


#writing to csv
loandata.to_csv('loan_cleaned.csv', index = True)








































