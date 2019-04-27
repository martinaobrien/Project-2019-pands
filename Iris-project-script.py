# Martina O'Brien - 22- 04-2019
# Programme and Scripting Project 2019 - Iris Data Set 

import pandas as pd 
import numpy as np

iris_data = pd.read_csv("Iris-data-set.csv") #setting up a variable for use in the program

print ("Investagations on Iris Dataset")

print(' ')
print('------------------------------------------------------------------------------------------------------------')
print(' ')

print('Shape of the Iris Dataset - number of individual sampls and the number of charateristics contained in the set') # gives the highest level of information about the date. Sourced: https://stackoverflow.com/questions/10200268/what-does-shape-do-in-for-i-in-rangey-shape0
print(' ')
print(iris_data.shape)

print(' ')
print('------------------------------------------------------------------------------------------------------------')
print(' ')

print('Iris Median')
print(' ')
print(iris_data.median())

print(' ')
print('------------------------------------------------------------------------------------------------------------')
print(' ')

print ("Summary of Key Statistics from Iris Dataset")
print (iris_data.describe())

print(' ')
print('------------------------------------------------------------------------------------------------------------')
print(' ')







