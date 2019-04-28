# Martina O'Brien - 22- 04-2019
# Programme and Scripting Project 2019 - Iris Data Set 

import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

iris_data = pd.read_csv("Iris-data-set.csv") #setting up a variable for use in the program
#Associated tables should save to repository once the program is executed.
iris_data.columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'Species'] #bringing in the names of the columns
sns.set(style="whitegrid", rc={'figure.figsize':(10,6)}) #sns.set is helping to set up the display box that you will be showing your graph in.

print(' ') #use of space to make the output more user friendly

print ("Investigations on Iris Dataset") #Title of program being run
print ("All Graphs within this program will be automatically saved in the folder for viewing")
print('Species Name') # this programme is being run to allow the user to indentify the three types of iris flower in the dataset
print(' ')
print(iris_data['Species'].unique()) #prints out the three types of iris species captured

print(' ')
print('------------------------------------------------------------------------------------------------------------')
print(' ')
# the above block is used as a spacing tool for ease of usability and readability for the users

print('Shape of the Iris Dataset')# Provides an overview of the data captured and potential outputs of further investigation Sourced: https://stackoverflow.com/questions/10200268/what-does-shape-do-in-for-i-in-rangey-shape0
print(' ')
print(iris_data.shape) #Prints the number of data entries in the data set along with number of the attributes
#.shape is a module from the pandas package

print(' ')
print('------------------------------------------------------------------------------------------------------------')
print(' ')

print ('Sample of Data contained in the Iris Dataset of all 150 records')# random sample of the dataset. source: https://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.DataFrame.sample.html
print (iris_data.sample (5)) #Prints 5 complete data entries from the set at random
x = iris_data.sample(5)
#.sample is a module from the pandas package to enable to user to see a random seletion of data from the dataset

print(' ')
print('------------------------------------------------------------------------------------------------------------')
print(' ')

print ("Summary of Key Statistics from Iris Dataset of all 150 records") # generates statistical analysis of the features of the measures of centre points and distribution of values source:https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html
print (iris_data.describe()) #Prints in tabular from key statistics from the data to provide high level analysis for the user
#.describe - a module that outputs the key statistics of the dataset
#output sets the scene for following investigations that are more indepth and particular to each species
print(' ')
print('------------------------------------------------------------------------------------------------------------')
print(' ')

print('Median of attributes from Iris Dataset of all 150 records') #this is an additional analysis conducted on the centre points of the data source: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.median.html
print(' ')
print(iris_data.median()) #Print the median of each of the attributes in tabular form

print(' ')
print('------------------------------------------------------------------------------------------------------------')
print(' ')

print ('Minimum, Maximum, Mean and Median of each attribute for each species in dataset') #the following analysis looks at the maximum, minimum, mean and median of each of the numerical categories
print(' ')
#all modules are from the pandas package
print('Min ') # Extracts the minimum values of each of the attributes 
print(iris_data.groupby('Species').min()) # Prints in tabular form and also groups the data by the three species
#Graph variables set up for bar chart to be displayed and saved into the repository
iris_min = iris_data.groupby('Species').min()
iris_min.plot.bar() #module to create table of minimum values for each species. Source: https://pandas.pydata.org/pandas-docs/version/0.23/generated/pandas.DataFrame.plot.bar.html
plt.gcf().subplots_adjust(bottom=0.15) #adjusting the table to enable table to be fully seen in the window. Source: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplots_adjust.html
plt.xlabel('Species', fontsize=18, weight='bold')#applying text and font to the table on the x axis. Source: https://stackoverflow.com/questions/12444716/how-do-i-set-the-figure-title-and-axes-labels-font-size-in-matplotlib
plt.ylabel("Min Values", fontsize=18, weight='bold')#applying text and font to the table on the x axis
title = "Min Value of Attributes in Iris dataset" #Applying a title to the dataset
filename = "Min Value of Attributes in Iris dataset.jpg" #the name of the file to which the graph will be saved to
plt.title(title, fontsize=26, weight='bold') #apply text and font detail to the title
plt.gcf().subplots_adjust(bottom=0.3)
#plt.show()
#plt.close()
filename = "Min of Attributes in Iris dataset.jpg"
plt.savefig(filename) #file will be saved and then will close to allow continuing of the program execution. Source:https://stackoverflow.com/questions/44383638/how-to-save-matplotlib-plot-with-the-same-file-name-as-its-filename-py
plt.close()
print(' ')


print('Max')  # Extracts the maximum values of each of the attributes 
print(iris_data.groupby('Species').max()) # The sources and explaination are the same for all tables in this group
#Graph variables set up for bar chart to be displayed and saved into the repository
iris_max = iris_data.groupby('Species').max()
iris_max.plot.bar()
plt.gcf().subplots_adjust(bottom=0.15)
plt.xlabel('Species', fontsize=18, weight='bold')
plt.ylabel("Max Values", fontsize=18, weight='bold')
title = "Max Value of Attributes in Iris dataset"
plt.title(title, fontsize=26, weight='bold')
plt.gcf().subplots_adjust(bottom=0.3)
#plt.show()
#plt.close()
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
#plt.show()
#plt.close()
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
#plt.show()
filename = "Median of Attributes in Iris dataset.jpg"
plt.savefig(filename)
plt.close()
print(' ')

print('This is a summary of all species and their attributes') #This program aims to output all the summary data for the three species
for i in iris_data['Species'].unique(): #while the .unique module is running, the program will gather data for each of the unique values and output a summary table
    build_list = iris_data['Species'] == i # this for loop will run for a long as there are new data being generated from the Species column.
    species = iris_data[build_list] # the module build list, creates a table for each species annd outputs the summary data as per.describe module
    print('\n', i, '\n', species.describe(), '\n')
    

print(' ')
print('------------------------------------------------------------------------------------------------------------')
print(' ')

print ("Distributions of Each Attributes")
print(' ')
print ("All Graphs within this program will be automatically saved in the folder for viewing")
print(' ')
title="Compare the Distributions of Sepal Length"
sns.boxplot(x="Species", y="sepal length", data=iris_data) #the seaborn boxplot function enables comparison between the distributions of each attribute. Source: https://seaborn.pydata.org/generated/seaborn.boxplot.html
plt.title(title, fontsize=26, weight='bold') # Further sources: https://python-graph-gallery.com/30-basic-boxplot-with-seaborn/
plt.gcf().subplots_adjust(bottom=0.3)
plt.xlabel('Species', fontsize=18, weight='bold')
plt.ylabel("Sepal Length", fontsize=18, weight='bold')
filename = "Compare the Distributions of Sepal Length.jpg"
plt.savefig(filename)
plt.close()
print(' ')

title="Compare the Distributions of Sepal Width"
sns.boxplot(x="Species", y="sepal width", data=iris_data)
plt.title(title, fontsize=26, weight='bold')
plt.gcf().subplots_adjust(bottom=0.3)
plt.xlabel('Species', fontsize=18, weight='bold')
plt.ylabel("Width", fontsize=18, weight='bold')
filename = "Compare the Distributions of Sepal Width.jpg"
plt.savefig(filename)
plt.close()
print(' ')

title="Compare the Distributions of Petal Length"
sns.boxplot(x="Species", y="petal length", data=iris_data)
plt.title(title, fontsize=26, weight='bold')
plt.gcf().subplots_adjust(bottom=0.3)
plt.xlabel('Species', fontsize=18, weight='bold')
plt.ylabel("Petal Length", fontsize=18, weight='bold')
filename = "Compare the Distributions of Petal Length.jpg"
plt.savefig(filename)
plt.close()
print(' ')

title="Compare the distributions of Petal Width"
sns.boxplot(x="Species", y="petal width", data=iris_data)
plt.title(title, fontsize=26, weight='bold')
plt.gcf().subplots_adjust(bottom=0.3)
plt.xlabel('Species', fontsize=18, weight='bold')
plt.ylabel("Petal Width", fontsize=18, weight='bold')
filename = "Compare the Distributions of Petal Width.jpg"
plt.savefig(filename)
plt.close()

print(' ')
print('------------------------------------------------------------------------------------------------------------')
print(' ')

print ("Correlation between the Sepal Characteristics and the Petal Characteristics to examine prediction factors")
print ("All Graphs within this program will be automatically saved in the folder for viewing")
print('Correlation OF ALL')
print(iris_data.iloc[0:].corr())

#Plotting Petal Length vs Petal Width & Sepal Length vs Sepal width
plt.figure() #Source:https://www.kaggle.com/sridharcr/data-analysis-iris-dataset
fig,ax=plt.subplots(1,2,figsize=(17, 9)) # Apadted from: https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation
iris_data.plot(x="sepal length",y="sepal width",kind="scatter",ax=ax[0],sharex=False,sharey=False,label="Sepal",color='r')
iris_data.plot(x="petal length",y="petal width",kind="scatter",ax=ax[1],sharex=False,sharey=False,label="Petal",color='b')
ax[0].set(title='Sepal comparasion ', ylabel='Sepal Width')
ax[1].set(title='Petal Comparasion',  ylabel='Petal Width')
ax[0].set(xlabel='Sepal Length')
ax[1].set(xlabel='Petal Length')
ax[0].legend()
ax[1].legend()
plt.gcf().subplots_adjust(bottom=0.3)
filename = "Corellation between Petal Length vs Petal Width & Sepal Length vs Sepal width.jpg"
plt.savefig(filename)
plt.close()


