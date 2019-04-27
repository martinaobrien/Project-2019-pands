## Project-2019-pands

#### Objective of the Project
Using the well known Fisher Iris Dataset, research, investigate and summarise using Python programming to extract key statistics and trends from the set.

#### Background Information to the Project
The Iris Flower DataSet was collected in 1939 by Edgar Anderson and analysed by Ronald Fisher in his paper "The use of multiple measurements in taxonomic problem" (i) to investigate the classification and organisation of key attributes of three species of Iris flower(ii). Using three species of Iris: virginica, sertosa and versicolor, the dataset captures data on four charateristics of each of the three species (iii).  

In total the dataset contains 50 types of each of the 3 species, 150 samples in total. The data distribution is 50 sampples per identified species. The order in which the measurements were taken are sepal length, sepal width, petal length and petal width.
Two species of the data set were collected in the Gasle Pennisula, Quebec Canada by the same person, on the same day and analysed using the same apparatus (iv). Below is a picture of the images of each of the flowers captured in the dataset. This link to the picture can be found in the References section (v)
 
 ![ALT Our Subjects](https://payatu.com/wp-content/uploads/2018/04/Selection_004.png)

##### Prerequisites for the Project

Using python programming tools, this project will analyse, summise and visualise key invetigates using a number of packages. These include: 
  pandas - Installed from: https://anaconda.org/anaconda/pandas
  matplotlib - Installed from: https://anaconda.org/conda-forge/matplotlib
  numpy - Installed from: https://anaconda.org/anaconda/numpy
  
  Iris dataset ws downloaded from: http://www.saedsayad.com/datasets/Iris.xls. the file was then converted in to a .csv file for use in this project.
  
##### Investigations on the Iris Data Set:
 
Importing the dataset: 
The dataset was imported using the pandas module as a csv file (vi). The dataset was imported into this repository for this project. Several investigations were carried out to provide an insight in the dataset. The data is visulaised using tables and bar charts initially to provide the user with a high level overview of the dataset. The latter graphics include scatterplots and dotplots that provide a much more indepth view. 

Initial Investigations: 
The following is a list of investigations conducted on the Iris dataset. These are intended to inform the user about the contact and key attributes of the data using the shape function.

Shape of the Iris Dataset - number of individual samples and the number of charateristics contained in the set and gives the highest level of information about the date using the random function.

Overview of key statistics of the Irisset
This table displays the following analysis for all of the data entries combined:
Count - the total count of each value recorded. All counts are 150 representing a complete dataset and no null or void entries. 
Mean - A measure of the centre for a distribution of a numeric variable. The total of all values divided bu the total number of values
Standard deviation - a measure expressing the difference between numerical values and the mean of the category
minimum, 25%, 50%, 75% maximum values - the corresponding values of each of the attributes in each column



Random selection of the data - this table details the characteristics of 5 random data entries for the set for demonstrative purposes
  
Using the describe function, the program investigates the folowing features of the numerical data for sepal length, sepal width, petal length, petal width:
1. count
2. mean of each column
3. standard deviation
4. minimum value in each column

count    150.000000   150.000000    150.000000   150.000000
mean       5.843333     3.054000      3.758667     1.198667
std        0.828066     0.433594      1.764420     0.763161
min        4.300000     2.000000      1.000000     0.100000
25%        5.100000     2.800000      1.600000     0.300000
50%        5.800000     3.000000      4.350000     1.300000
75%        6.400000     3.300000      5.100000     1.800000
max
 
 ###### Three Dimensional Investigations
 
 
 
 ##### Analysis and Summary of the Iris Dataset


You need to 
1.	Research ways to tackle the project
2.	Research background information
3.	Summaries the background data set
4.	Keep a reference list on all sources used in the project
5.	Download the data set
6.	Write some code to investigate it
7.	Summarise the date set: 
8.	maximum, minimum and mean of each column of the data set
9.	Write a summary of the investigatations using python
10.	Supporting Tables - labelled
11.	Graphics  - relevant

Train of thought: 
 •	Investigate and explain the data set to someone with no prior knowledge of the data
•	Explain what investigating the data set entails and how Python can be used to do it
•	Present a write up and code
•	Well organised and detailed explanations
•	Well conceived and examples of interesting analysis that others have pursued



#### References: 
http://rcs.chemometrics.ru/Tutorials/classification/Fisher.pdf
https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342
http://archive.ics.uci.edu/ml/datasets/Iris
https://www.ritchieng.com/machine-learning-iris-dataset/
https://payatu.com/wp-content/uploads/2018/04/Selection_004.png
https://www.dataquest.io/blog/pandas-python-tutorial/




http://patrickhoey.com/downloads/Computer_Science/03_Patrick_Hoey_Data_Visualization_Dataset_paper.pdf

https://archive.ics.uci.edu/ml/datasets/Iris

https://pandas.pydata.org/pandas-docs/stable/getting_started/dsintro.html#dsintro

https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html

https://www.datacamp.com/community/blog/python-pandas-cheat-sheet

http://mirlab.org/jang/books/dcpr/dataSetIris.asp?title=2-2%20Iris%20Dataset

https://shapeofdata.wordpress.com/2013/10/01/case-study-1-iris/

http://cmdlinetips.com/2018/02/how-to-randomly-select-rows-in-pandas-pandas-tutorial/

https://shapeofdata.wordpress.com/2013/04/09/principle-component-analysis/

https://www.researchgate.net/publication/237010807_What_should_we_know_about_the_famous_Iris_data/download

https://www.tutorialspoint.com/python/python_2darray.htm

https://snakify.org/en/lessons/two_dimensional_lists_arrays/problems/chessboard/

https://www.tutorialspoint.com/python/python_2darray.htm

https://www.kaggle.com/lalitharajesh/iris-dataset-exploratory-data-analysis

https://www.kaggle.com/sridharcr/data-analysis-iris-dataset

https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342

https://github.com/RitRa/Project2018-iris/blob/master/Project%2B2018%2B-%2BFishers%2BIris%2Bdata%2Bset%2Banalysis.py

( http://archive.ics.uci.edu/ml/datasets/Iris).
