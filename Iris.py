# Martina O'Brien - 22- 04-2019
# Iris Data Set

import pandas as pd #importing the pandas module as part of the Anaconda package for use in this project
data = pd.read_csv("Iris-data-set.csv") #data set on Iris Flowers (Fisher:1936), this is imported into Git Hub

ans = input ("To see complete iris data set, please enter Yes/No: ")
if ans == "Yes":
    print (data) # this date is the imported data from Git Hub respository
    print ("___________________________________________________") # will print to distinguish end of programme
else:
    print ("This is the first five lines of the Iris Data Set")
    print (data.iloc [:5 , : 5]) #data.iloc is a panda module that will enable users to see the first five columns and rows of data
    print ("___________________________________________________") 




#print (data.loc [ : , "sepal length"].head)


#print (data.describe())

#print (data.shape)
#print (data.head(7))

#print (data.loc [ : , "sepal length"])
#print (variable.function[row,"label"]