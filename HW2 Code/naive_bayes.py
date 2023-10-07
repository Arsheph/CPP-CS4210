#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv

trainData = []
header = []
#reading the training data in a csv file
#--> add your Python code here
with open('weather_training.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0:
         trainData.append (row)
      elif i == 0:
          header.append(row)

#transform the original training features to numbers and add them to the 4D array X.
#For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
trainX = []

for instance in trainData:
        
        # Skip Day
    
        # Outlook
        if instance[1] == "Sunny":
            outVal = 1
        elif instance[1] == "Overcast":
            outVal = 2
        else: # Rain
            outVal = 3
            
        # Temperature
        if instance[2] == "Cold":
            tempVal = 1
        elif instance[2] == "Mild":
            tempVal = 2
        else: # Hot
            tempVal = 3
            
        # Humidity
        if instance[3] == "Normal":
            humVal = 1
        else: # High
            humVal = 2
            
        # Wind    
        if instance[4] == "Weak":
            windVal = 1
        else: # Strong
            windVal = 2
        
        trainX.append([outVal, tempVal, humVal, windVal])

#transform the original training classes to numbers and add them to the vector Y.
#For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
trainY = []

for instance in trainData:
    
    # Class    
        if instance[5] == "Yes":
            classVal = 1
        else: # No
            classVal = 2
        
        trainY.append(classVal) # would these numbers not be better as Zero and One?
        # I will have them as One and Two to follow the example, but I still am not sure if it makes a difference
 
#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(trainX, trainY)

#reading the test data in a csv file
#--> add your Python code here
testData = []
with open('weather_test.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         testData.append (row)
         
testX = []

for instance in trainData:
        
        # Skip Day
    
        # Outlook
        if instance[1] == "Sunny":
            outVal = 1
        elif instance[1] == "Overcast":
            outVal = 2
        else: # Rain
            outVal = 3
            
        # Temperature
        if instance[2] == "Cold":
            tempVal = 1
        elif instance[2] == "Mild":
            tempVal = 2
        else: # Hot
            tempVal = 3
            
        # Humidity
        if instance[3] == "Normal":
            humVal = 1
        else: # High
            humVal = 2
            
        # Wind    
        if instance[4] == "Weak":
            windVal = 1
        else: # Strong
            windVal = 2
        
        testX.append([outVal, tempVal, humVal, windVal])

#printing the header os the solution
#--> add your Python code here
header[0].append("Confidence")
print(header)

#use your test samples to make probabilistic predictions. For instance: clf.predict_proba([[3, 1, 2, 1]])[0]
#--> add your Python code here
testInd = 0
for instance in testX:
    likelyRate = clf.predict_proba([instance])[0]
    
    if likelyRate[1] >= 0.75:
        trainData[testInd].append(round(likelyRate[1], 2))
        print(trainData[testInd])
    elif likelyRate[0] >= 0.75:
        trainData[testInd].append(round(likelyRate[0], 2))
        print(trainData[testInd])
    else:
        pass
    
    testInd = testInd + 1
