# Martina O'Brien - 22- 04-2019
# Programme and Scripting Project 2019 - Iris Data Set 

import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

iris_data = pd.read_csv("Iris-data-set.csv") #setting up a variable for use in the program

iris_data.columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'Species']
sns.set(style="whitegrid", rc={'figure.figsize':(10,6)}) #sns.set is helping to set up the display box that you will be showing your graph in.
'''
print(' ')

print ("Investagations on Iris Dataset")

print('Species Name')
print(' ')
print(iris_data['Species'].unique()) #prints out the three types of iris species captured

print(' ')
print('------------------------------------------------------------------------------------------------------------')
print(' ')

print('Shape of the Iris Dataset')# Provides an overview of the data captured and potential outputs of further investigation Sourced: https://stackoverflow.com/questions/10200268/what-does-shape-do-in-for-i-in-rangey-shape0
print(' ')
print(iris_data.shape) #Prints the number of data entries in the data set along with number of the attributes


print(' ')
print('------------------------------------------------------------------------------------------------------------')
print(' ')

print ('Sample of Data contained in the Iris Dataset of all 150 records')# random sample of the dataset. source: https://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.DataFrame.sample.html
print (iris_data.sample (5)) #Prints 5 complete data entries from the set at random
x = iris_data.sample(5)

print(' ')
print('------------------------------------------------------------------------------------------------------------')
print(' ')

print ("Summary of Key Statistics from Iris Dataset of all 150 records") # generates statistical analysis of the features of the measures of centre points and distribution of values source:https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html
print (iris_data.describe()) #Prints in tabular from key statistics from the data to provide high level analysis for the user

print(' ')
print('------------------------------------------------------------------------------------------------------------')
print(' ')

print('Median of attributes from Iris Dataset of all 150 records') #this is an additional analysis conducted on the centre points of the data source: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.median.html
print(' ')
print(iris_data.median()) #Print the median of each of the attributes in tabular form

print(' ')
print('------------------------------------------------------------------------------------------------------------')
print(' ')


print ('Minimum, Maximum and Mean of each attribute for each species in dataset') #the following analysis looks at the maximum and minimum of each of the numerical categories
print(' ')

print('Min ') # Extracts the minimum values of each of the attributes 
print(iris_data.groupby('Species').min()) # Prints in tabular form

#Graph variables set up for bar chart to be displayed and saved into the repository
iris_min = iris_data.groupby('Species').min()
iris_min.plot.bar()
plt.gcf().subplots_adjust(bottom=0.15)
plt.xlabel('Species', fontsize=18, weight='bold')
plt.ylabel("Min Values", fontsize=18, weight='bold')
title = "Min Value of Attributes in Iris dataset"
filename = "Min Value of Attributes in Iris dataset.jpg"
plt.title(title, fontsize=26, weight='bold')
plt.gcf().subplots_adjust(bottom=0.3)
plt.show()
plt.close()
filename = "Min of Attributes in Iris dataset.jpg"
plt.savefig(filename)
plt.close()
print(' ')


print('Max')  # Extracts the maximum values of each of the attributes 
print(iris_data.groupby('Species').max()) # Prints in tabular form

#Graph variables set up for bar chart to be displayed and saved into the repository
iris_max = iris_data.groupby('Species').max()
iris_max.plot.bar()
plt.gcf().subplots_adjust(bottom=0.15)
plt.xlabel('Species', fontsize=18, weight='bold')
plt.ylabel("Max Values", fontsize=18, weight='bold')
title = "Max Value of Attributes in Iris dataset"
filename = "Max Value of Attributes in Iris dataset.jpg"
plt.title(title, fontsize=26, weight='bold')
plt.gcf().subplots_adjust(bottom=0.3)
plt.show()
plt.close()
filename = "Max of Attributes in Iris dataset.jpg"
plt.savefig(filename)
plt.close()
print(' ')


print('Mean')  # Extracts the maximum values of each of the attributes 
print(iris_data.groupby('Species').mean()) # Prints in tabular form
print(' ')

#Graph variables set up for bar chart to be displayed and saved into the repository
iris_mean = iris_data.groupby('Species').mean()
iris_mean.plot.bar()
plt.gcf().subplots_adjust(bottom=0.15)
plt.xlabel('Species', fontsize=18, weight='bold')
plt.ylabel("Mean Values", fontsize=18, weight='bold')
title = "Mean Value of Attributes in Iris dataset"
filename = "Mean Value of Attributes in Iris dataset.jpg"
plt.title(title, fontsize=26, weight='bold')
plt.gcf().subplots_adjust(bottom=0.3)
plt.show()
plt.close()
filename = "Mean of Attributes in Iris dataset.jpg"
plt.savefig(filename)
plt.close()
print(' ')

print('Median')  # Extracts the median values of each of the attributes 
print(iris_data.groupby('Species').median()) # Prints in tabular form
print(' ')



#Graph variables set up for bar chart to be displayed and saved into the repository
iris_median = iris_data.groupby('Species').median()
iris_median.plot.bar()
plt.gcf().subplots_adjust(bottom=0.15)
plt.xlabel('Species', fontsize=18, weight='bold')
plt.ylabel("Median Values", fontsize=18, weight='bold')
title = "Median Value of Attributes in Iris dataset"
filename = "Median Value of Attributes in Iris dataset.jpg"
plt.title(title, fontsize=26, weight='bold')
plt.gcf().subplots_adjust(bottom=0.3)
plt.show()
plt.close()
filename = "Median of Attributes in Iris dataset.jpg"
plt.savefig(filename)
plt.close()
print(' ')

Print 'This is a summary of all species and their attributes'
for i in iris_data['Species'].unique():
    build_list = iris_data['Species'] == i
    species = iris_data[build_list]
    print('\n', i, '\n', species.describe(), '\n')
    
all above this line works
----------------------------------------------------------------------------------------------------------
'''

title="Compare the Distributions of Sepal Length"
sns.boxplot(x="Species", y="sepal length", data=iris_data)
# increasing font size
plt.title(title, fontsize=26, weight='bold')
plt.gcf().subplots_adjust(bottom=0.3)
plt.xlabel('Species', fontsize=18, weight='bold')
plt.ylabel("Sepal Length", fontsize=18, weight='bold')
filename = "Compare the Distributions of Sepal Length"
plt.show()
plt.savefig(filename)
plt.close()
print(' ')


title="Compare the Distributions of Sepal Width"
sns.boxplot(x="Species", y="sepal width", data=iris_data)
# increasing font size
plt.title(title, fontsize=26, weight='bold')
plt.gcf().subplots_adjust(bottom=0.3)
plt.xlabel('Species', fontsize=18, weight='bold')
plt.ylabel("Width", fontsize=18, weight='bold')
filename = "Compare the Distributions of Sepal Width"
plt.show()
plt.savefig(filename)
plt.close()
print(' ')
# ----------------------------------------------------------------------------------------------------------------

title="Compare the Distributions of Petal Length"
sns.boxplot(x="Species", y="petal length", data=iris_data)
plt.title(title, fontsize=26, weight='bold')
plt.gcf().subplots_adjust(bottom=0.3)
plt.xlabel('Species', fontsize=18, weight='bold')
plt.ylabel("Petal Length", fontsize=18, weight='bold')
filename = "Compare the Distributions of Petal Length"
plt.show()
plt.savefig(filename)
plt.close()
print(' ')

# ---------------------------------------------------------------------------------------------------------------

title="Compare the distributions of Petal Width"
sns.boxplot(x="Species", y="petal width", data=iris_data)
# increasing font size
plt.title(title, fontsize=26, weight='bold')
plt.gcf().subplots_adjust(bottom=0.3)
plt.xlabel('Species', fontsize=18, weight='bold')
plt.ylabel("Petal Width", fontsize=18, weight='bold')
filename = "Compare the Distributions of Petal Width"
plt.show()
plt.savefig(filename)
plt.close()
print(' ')


'''
# not working yet


#Importing seaborn to give more data visualisation properties to the dataset e.g. grids, barcharts, histogram and adding features such as legend, assign colour to doeeference attributes
sns.set(style="whitegrid", rc={'figure.figsize':(10,6)}) #sns.set is helping to set up the display box that you will be showing your graph in.
file = open('test_write.py', 'a+') #opens a file in end repository to save graphs generated by the following code

print ('Analysis of Mean values across sepcies and attributes')
print('Species Name')
print(' ')
print(iris_data['Species'].unique()) #3 types of species are considered unique and used to distinguish numberical categories



plt.xlabel('Species', fontsize=18, weight='bold', rotation=180)
plt.ylabel("Mean Values", fontsize=18, weight='bold')

title = "Mean of Attributes in Iris dataset"

filename = "Mean of Attributes in Iris dataset.jpg"

plt.title(title, fontsize=26, weight='bold')

plt.show()

filename = "Mean of Attributes in Iris dataset.jpg"
plt.savefig(filename)


print(' ')
print('------------------------------------------------------------------------------------------------------------')
print(' ')
print ('Analysis of Max values across sepcies and attributes')
print('Species Name')
print(' ')
print(iris_data['Species'].unique()) #3 types of species are considered unique and used to distinguish numberical categories

iris_max = iris_data.groupby('Species').max()
iris_max.plot.bar()
plt.gcf().subplots_adjust(bottom=0.15)
plt.xlabel('Species', fontsize=18, weight='bold', rotation=180)
plt.ylabel("Mean Values", fontsize=18, weight='bold')
title = "Max Value of Attributes in Iris dataset"
filename = "Max Value of Attributes in Iris dataset.jpg"
plt.title(title, fontsize=26, weight='bold')
plt.show()
filename = "Max of Attributes in Iris dataset.jpg"
plt.savefig(filename)

print(' ')
print('------------------------------------------------------------------------------------------------------------')
print(' ')

print ('Analysis of Min values across sepcies and attributes')
print('Species Name')
print(' ')
print(iris_data['Species'].unique()) #3 types of species are considered unique and used to distinguish numberical categories

iris_min = iris_data.groupby('Species').min()

iris_min.plot.bar()
plt.gcf().subplots_adjust(bottom=0.15)

plt.xlabel('Species', fontsize=18, weight='bold', rotation=180)
plt.ylabel("Minimum Values", fontsize=18, weight='bold')

title = "Min Value of Attributes in Iris dataset"

filename = "Min Value of Attributes in Iris dataset.jpg"

plt.title(title, fontsize=26, weight='bold')

plt.show()

filename = "Min of Attributes in Iris dataset.jpg"
plt.savefig(filename)

print(' ')
print('------------------------------------------------------------------------------------------------------------')
print(' ')

#Plotting Petal Length vs Petal Width & Sepal Length vs Sepal width
#warnings.simplefilter("ignore")#Supress any warning

plt.figure()
fig,ax=plt.subplots(1,2,figsize=(17, 9))
iris_data.plot(x="sepal length",y="sepal width",kind="scatter",ax=ax[0],sharex=False,sharey=False,label="sepal",color='r')
iris_data.plot(x="petal length",y="petal width",kind="scatter",ax=ax[1],sharex=False,sharey=False,label="petal",color='b')
ax[0].set(title='Sepal comparasion ', ylabel='sepal-width')
ax[1].set(title='Petal Comparasion',  ylabel='petal-width')
ax[0].legend()
ax[1].legend()
plt.show()
plt.close()

# we can see that  there are some petals which are smaller than rest of petal.
#Let's examine them

plt.figure()
fig,ax=plt.subplots(1,2,figsize=(21, 10))

setosa.plot(x="sepal length", y= "sepal width", kind="scatter",ax=ax[0],label='setosa',color='r')
versicolor.plot(x="sepal length",y="sepal width",kind="scatter",ax=ax[0],label='versicolor',color='b')
virginica.plot(x="sepal length", y="sepal width", kind="scatter", ax=ax[0], label='virginica', color='g')

setosa.plot(x="petal length", y="petal-width", kind="scatter",ax=ax[1],label='setosa',color='r')
versicolor.plot(x="petal length",y="petal-width",kind="scatter",ax=ax[1],label='versicolor',color='b')
virginica.plot(x="petal length", y="petal-width", kind="scatter", ax=ax[1], label='virginica', color='g')

ax[0].set(title='Sepal comparasion ', ylabel='sepal-width')
ax[1].set(title='Petal Comparasion',  ylabel='petal-width')
ax[0].legend()
ax[1].legend()

plt.show()
plt.close()

'''