## Project-2019-pands

#### Objective of the Project
Using the well known Fisher Iris Dataset, research, investigate and summarise using Python programming to extract key statistics and trends from the set.

#### Background Information to the Project
The Iris Flower DataSet was collected in 1939 by Edgar Anderson and analysed by Ronald Fisher in his paper "The use of multiple measurements in taxonomic problem" (i) to investigate the classification and organisation of key attributes of three species of Iris flower(ii). Using three species of Iris: virginica, sertosa and versicolor, the dataset captures data on four charateristics of each of the three species (iii).  

In total the dataset contains 50 types of each of the 3 species, 150 samples in total. The data distribution is 50 sampples per identified species. The order in which the measurements were taken are sepal length, sepal width, petal length and petal width.
Two species of the data set were collected in the Gasle Pennisula, Quebec Canada by the same person, on the same day and analysed using the same apparatus (iv). Below is a picture of the images of each of the flowers captured in the dataset. This link to the picture can be found in the References section (v)
 
 ![ALT Our Subjects](https://payatu.com/wp-content/uploads/2018/04/Selection_004.png)

##### Prerequisites for the Project

Using python programming tools, this project will analyse, summise and visualise key invetigates using a number of packages. These include (Python was installed through Anaconda so some packages were already av were avaiable to me): 
  
  pandas - Installed from: https://anaconda.org/anaconda/pandas
  
  matplotlib - Installed from: https://anaconda.org/conda-forge/matplotlib
  
  numpy - Installed from: https://anaconda.org/anaconda/numpy
  
  seaborn - Installed from: https://anaconda.org/anaconda/seaborn
  
  Iris dataset ws downloaded from: http://www.saedsayad.com/datasets/Iris.xls. the file was then converted in to a .csv file for use in this project.
  
#### Investigations on the Iris Data Set:

Importing the dataset: 

The dataset was imported using the pandas module as a csv file (vi). The dataset was imported into this repository for this project. Several investigations were carried out to provide an insight in the dataset. The data is visulaised using tables and bar charts initially to provide the user with a high level overview of the dataset. The latter graphics include scatterplots and dotplots that provide a much more indepth view. 

##### List of Investigations: 

These are intended to inform the user about the contact and key attributes of the data using the shape function. This investigation is accompanied by a brief description of the investigation. A full list of the graphs outputted from the program code can be found at the end of this section. 

Shape of the Iris Dataset - number of individual samples and the number of charateristics contained in the set and gives the highest level of information about the date using the random function.

Species Name: The purpose is to identify the three types of Iris species included in the dataset

Overview of key statistics of the Iris dataset: To provide a high level statistics to the user

This table displays the following analysis for all of the data entries combined:

Count - the total count of each value recorded. All counts are 150 representing a complete dataset and no null or void entries. 

Mean - A measure of the centre for a distribution of a numeric variable. The total of all values divided bu the total number of values

Standard deviation - a measure expressing the difference between numerical values and the mean of the category

minimum, 25%, 50%, 75% maximum values - the corresponding values of each of the attributes in each column

Median: A measure of the centre for a distribution of a numeric variable. It splits the data in half with half the observations above and below.

Sample of Data contained in the Iris Dataset of all 150 records. The table aims to give a sample of the data but is locked at 5 entries

Minimum, Maximum, Mean and Median of each attribute for each species in dataset. This is done for each of the attributes: sepal length, sepal width, petal length and petal width across all species. 



##### List of Graphs: 

Graph 1: Min of Attributes in Dataset

Graph 2: Max of Attributes in Dataset

Graph 3. Mean of Attributes in Dataset

Graph 4: Median of Attributes in Dataset

Graph 5: Compare the distribution of sepal length

Graph 6: Compare the distribution of sepal width

Graph 7: Compare the distribution of petal length

Graph 8: Compare the distribution of petal width

Graph 9: Correlation between Petal Length and Petal Width versus Sepal Length and Sepal Width



#### Analysis and Summary of the Iris Dataset

This project has examined the key statistics of the attributes for the Iris flower dataset such as the maximum, medium and standard deviation for all the data and also the individual species.The purpose of this project is to explore any distinctions betweek attributes and species that may exist that could be considered predictors in identfying the different types of species. 

To investigate this further, the max and min functions were used to identify the flowers asscoiated with the data, allowing us to assume that sertosa will be among the smallest data entries collected and virgininca will be among the largest data entries collected. It is well documented that the iris-sertosa and iris-virginica has more distinguishable attributes than the iris-versicolor (vii). Using descriptive analysis, this pattern begins to emerge. 

The mean and median of the attributes were also calculated as calculating the centre points for the data are important in exploing predictors. Initial analysis would suggest that the central points for the sepal length and sepal width are less than .1, suggesting the mean and median are quite similiar. The difference between the mean and median are more pronounced in the petal length and petal width, greater that .5. This suggests that the data on petal lengths and petal widths may prove to be more indicative of the data entries species. 

To further visualise this data, Figure 1.0 "Plotting Petal Length vs Petal Width & Sepal Length vs Sepal width" demonstrates the spread of sepal sizes and petal sizes across the whole data set. (viii). It is clear from the data set that there is a high correlation between the petal length and the petal width for the Iris species research. The cam cannot be said for the sepal measurements as you can see from Graph 9, there is nore obvious pattern emerging.

Ascertaining the centre properties of each of the attributes for each species is central to establishing patterns. The next Boxplots to further investigate how each distribution of the attributes (sepal length, sepal width, petal length and petal width) compared across the three species (iris sertosa, iris virginica, iris versicolor). It also identifies any outliers that may serve to skew the data. In this instance, there are very little outliers to be found in the data but due to the distance between the outliers and the centre in the boxplot, the mean figures may be skewed. 

Another interesting point to not that three out the four attributes seem to follow a loose pattern according to the graphs generating boxplots on the distribution of each of the attributes in relation to the type of flower. In the case of petal length, petal width and sepal length, there is an increase in sixe from sertosa to versicolor to virgininca. The difference between them is more pronounced in the petal attributes, a fact that is correlated in Graph 9. 

#### References: 
i. http://rcs.chemometrics.ru/Tutorials/classification/Fisher.pdf

ii. https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342

iii. http://archive.ics.uci.edu/ml/datasets/Iris

iv. https://www.ritchieng.com/machine-learning-iris-dataset/

v. https://payatu.com/wp-content/uploads/2018/04/Selection_004.png

vi. https://www.dataquest.io/blog/pandas-python-tutorial/

vii. http://patrickhoey.com/downloads/Computer_Science/03_Patrick_Hoey_Data_Visualization_Dataset_paper.pdf

viii. https://www.oreilly.com/library/view/python-data-science/9781491912126/ch04.html

http://statweb.stanford.edu/~jtaylo/courses/stats202/visualization.html


#### Useful Links used

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


### Notes
* Python was installed through Anaconda so some packages installed through Anaconda were already available to me
