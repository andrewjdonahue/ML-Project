# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 12:49:21 2023

@author: stephanie.contino
"""
# import libraries
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# define url and names
url = '2022.csv'
names = ['objectid',
         'dc_dist', 
         'dispatch_date',
         'hour', 
         'location_block', 
         'text_general_code',
         'lat', 
         'lng']

# read graph csv
graph = read_csv(url, dtype = {'lat': float, 'lng': float})
graphset = graph[['lat', 'lng']]

# create scatterplot (becomes map of phl)
pyplot.scatter(graphset.lng, graphset.lat, c = "blue")
pyplot.show()

### BEGIN PROJECT CODE HERE (Last Edited: 6/29/23) ###

## List of Variables:

#PointValue = Crime1+Crime2+Crime3+Crime4...
#SafetyRating = 100-PointValue
SafetyWarning = "Warning: This safety recommendation is based only on the crime data for Philadelphia, therefore, even if a high safety rating is given and the area is safe relative to the rest of the city, there is always a risk of danger, especially at night. Personal discretion and caution should always be used."
InitialPrompt = "Please enter a street name within Philadelphia and time in 24-hr format. (Ex: LOCUST ST, 2100)"
AcceptanceMessage = "Street name and time accepted. Generating results..."
ErrorMessage1 = "Please enter a street name within Philadelphia."
ErrorMessage2 =  "The street name is misspelled, please try again."
ErrorMessage3 = "There is no data for the given street name, please try a nearby street."
#StreetInput = The street name that the user has input
#TimeInput - The time that the user has input
#UserInput = The whole user input (street and time), in string form.
#SafetyRating = 3-digit integer, assigned to every UserInput
#Breakdown = A summary of the crime statistics from given UserInput


print(SafetyWarning)
print(InitialPrompt)
print(AcceptanceMessage)
