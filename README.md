# HousePricesInSanDiego

+ [Table of Contents](#sub-sub-heading-1)
    + [Credits](#credits)
    + [Project Goal and procedure](#project-goal-and-procedure)
    + [Code and Resources](#code-and-resources)
    + [Part 1- Scraping Data using Scrapy](#part-1--scraping-data-using-scrapy)
    + [Part 2- Data Cleaning and Feature Engineering](#part-2--data-cleaning-and-feature-engineering)
    + [Part 3- Exploratory Data Analysis](#part-3--exploratory-data-analysis)
    + [Part 4- Model Building](#part-4--model-building)
    + [Part 5- Flask Server](#part-5--flask-server)
    + [Part 6- Project Limitation](#part-6--project-limitation)
    
<img src='./images/image2.jpg' width=600>
    
 ### Credits: 
 A big thank you goes to [KenJee](https://www.youtube.com/channel/UCiT9RITQ9PW6BhXK0y2jaeg), [Codebasics](https://www.youtube.com/channel/UCh9nVJoWXmFb7sLApWGcLPQ), [Krish Naik](https://www.youtube.com/user/krishnaik06), [Keith Galli](https://www.youtube.com/channel/UCq6XkhO5SZ66N04IcPbqNcw)  and to the whole [Edureka Team](https://www.youtube.com/user/edurekaIN) who put a lot of effort to teach people Data Science,Machine Learning, Statistics and a lot of other related topics for free.
 
 ### Project Goal and Procedure
 * Goal: Build a Model which can predict monthly prices for renting apartments in San Diego, CA. 
 * Scraped apartment and price information from [Zillow.com](https://www.zillow.com/) using Python and Scrapy. 
 * Saved results in a csv file and manipulated and worked with the data using the pandas package
 * visualization of data using seaborn and matplotlib packages
 * Built a linear regression model with an accuracy of 75%
 * Turned the model into an API using Flask
 

### Code and Resources

* Python Version: 3.8
* Environment: Visual Studio, Pycharm, Jupyter Notebook
* Packages: Scrapy, Matplotlib, Seaborn, Numpy, Scikit-learn, Flask
* Other tools: Postman 

## Part 1- Scraping Data using Scrapy
Data was extracted by scraping the website's API and storing the results in a csv file. Scrapy is a common framework for extracting, processing, and storing web data. Zillow is a US- Real Estate market place. 


<img src='./images/image1.PNG' width=450> 

#### Data Scraped:
* City
* State
* Area in Sqft
* Baths
* Beds
* Latitude
* Longitude
* Price 

<img src='./images/image3.PNG' width=900>

### Output in pandas after scraping (first 5 entries)
<img src='./images/image4.PNG' width=600> 

## Part 2- Data Cleaning and Feature Engineering
After scraping the data and storing it in csv and pandas, I had to do some cleaning steps like:
* remove rows where data is missing
* make the data machine readable (e.g. changing the data types, removing string elements from specific columns)
* rename some columns
* remove 'addressCity' and 'addressState' columns because just San Diego data is analyzed so we dont get any additional value from that information 

Example of using the matplotlib visualization package to get an overview what data is missing:
<img src='./images/image5.PNG' width=450>

When data is missing you can either take the median or the mean of the available data for the missing values or remove the row completely. I decided to remove every row where data is missing. In total, more than 40% of the data rows were deleted (Before removing: 840 entries, After removing: 485 entries). After the rows were deleted, the same visualization technique shows that we do not have missing values in our dataset anymore:

<img src='./images/image6.PNG' width=450>

#### After modifying the data, the rows and the columns, our data frame looks like this (first 5 entries):

<img src='./images/image7.PNG' width=500>

## Part 3- Exploratory Data Analysis

#### Monthly house price distribution

<img src='./images/image8.PNG' width=600>

#### Heatmap showing the correlations between the features and target

<img src='./images/image9.PNG' width=600>

#### Correlation between the area and the monthly price

<img src='./images/image10.PNG' width=600>

#### Correlation between the number of bedrooms and the monthly price

<img src='./images/image11.PNG' width=600>


## Part 4- Model Building

In the model building part I decided to take the Linear Regression in order to build a prediction model for monthly housing prices in San Diego. I decided to take just three columns as the independent variables (area in sqft, bathrooms, bedrooms) to predict the target variable (monthly price in $). I used the train_test_split function from the Scikit-learn package in order to train the model. The test size was set to 10%, the training size to 90%. The accuracy of the Linear Regression Model Score is 75,79%.

#### Scatterplot which shows the predicted and the actual values

<img src='./images/image12.PNG' width=600>


Finally, the results were saved as a pickle file and a json file which we need for building the Flask Server in the next step.
.


## Part 5- Flask Server

In this last step, I developed a flask (web framework) API endpoint following along with the Codebasics tutorial which I mentioned in the beginning. The purpose is to create a website which can reach out to the backend and get a response. In this simplified website a user would be able to enter the desired area, the number of bedrooms and bathrooms and would get back a monthly price. This response information is based on the model which was created in the previous steps

<img src='./images/image13.PNG' width=1000>


## Part 6- Project Limitation

Since a lot of rows were deleted due to imcomplete data, the dataset is not that big to build a reliable model. Furthermore I chose to use the multiple linear regression approach to make predictions. For further projects GridSearchCV can be used which is a common machine technique in the area of machine learning to find out which model with which parameters performs best. Furthermore the deployment in AWS can be considered as a next step. Finally, more features (districts, parking lot available etc.) can be used as additional independent variables to build a more reliable model.










