# Martina O'Brien - 22- 04-2019
# Programme and Scripting Project 2019 - Iris Data Set 

import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

iris_data = pd.read_csv("Iris-data-set.csv") #setting up a variable for use in the program

iris_data.columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'iris']
print(' ')

print ("Investagations on Iris Dataset")

print(' ')
print('------------------------------------------------------------------------------------------------------------')
print(' ')

print('Shape of the Iris Dataset')# Provides an overview of the data captured and potential outputs of further investigation Sourced: https://stackoverflow.com/questions/10200268/what-does-shape-do-in-for-i-in-rangey-shape0
print(' ')
print(iris_data.shape)

print(' ')
print('------------------------------------------------------------------------------------------------------------')
print(' ')

print ('Sample of Data contained in the Iris Dataset')# random sample of the dataset. source: https://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.DataFrame.sample.html
print (iris_data.sample (5))
x = iris_data.sample(5)

print(' ')
print('------------------------------------------------------------------------------------------------------------')
print(' ')

print ("Summary of Key Statistics from Iris Dataset") # generates statistical analysis of the features of the measures of centre points and distribution of values source:https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html
print (iris_data.describe())

print(' ')
print('------------------------------------------------------------------------------------------------------------')
print(' ')

print('Iris Median') #this is an additional analysis conducted on the centre points of the data source: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.median.html
print(' ')
print(iris_data.median())

print(' ')
print('------------------------------------------------------------------------------------------------------------')
print(' ')

df1 = iris_data[iris_data['iris'].str.contains("Iris-setosa")] 
df1_mean = df1.mean()
df1_describe = df1.describe()
print('Iris-setosa mean')
print(' ')
print(df1_mean)

print(' ')
print('------------------------------------------------------------------------------------------------------------')
print(' ')

print ('Maximum and Minimum of the Dataset')
df = iris_data
print (df.max()) # will return max value of each column
print (df.min())

print(' ')
print('------------------------------------------------------------------------------------------------------------')
print(' ')

#title="Compare the Distributions of Sepal Width"
#sns.boxplot(x="iris", y="sepal width", data=iris_data)
# increasing font size
#plt.title(title, fontsize=26)
# Show the plot
#plt.show()



#for i in iris_data['iris'].unique():
#build_list = iris_data['iris'] == i
#species = iris_data[build_list]
#print('\n', i, '\n', species.describe(), '\n')
    #for j in ['sepal length', 'sepal width', 'petal length', 'petal width']:
       # title = i
        #plt.title(title)
        #x = species[j]
        #sns.distplot(x)
    #    plt.show()
