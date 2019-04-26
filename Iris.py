# Martina O'Brien - 22- 04-2019
# Iris Data Set

import pandas as pd #importing the pandas module as part of the Anaconda package for use in this project
import random
data = pd.read_csv("Iris-data-set.csv") #data set on Iris Flowers (Fisher:1936), this is imported into Git Hub

print (data.describe())
