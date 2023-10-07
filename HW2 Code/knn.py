#-------------------------------------------------------------------------
# AUTHOR: Joshua Pao
# FILENAME: knn.py
# SPECIFICATION: KNN calculator for 1NN on file
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []
numWrong = 0
numTotal = 0

#reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         numTotal = numTotal + 1

#loop your data to allow each instance to be your test set
for row in db:

    #add the training features to the 2D array X removing the instance that will be used for testing in this iteration. For instance, X = [[1, 3], [2, 1,], ...]]. Convert each feature value to
    # float to avoid warning messages
    #--> add your Python code here
    X=[]
    for rowX in db:
        if rowX == row: pass
        else: 
            rowX0 = float(rowX[0])
            rowX1 = float(rowX[1])
            rowXP = [rowX0, rowX1]
            X.append(rowXP)
        
    #transform the original training classes to numbers and add to the vector Y removing the instance that will be used for testing in this iteration. For instance, Y = [1, 2, ,...]. Convert each
    #  feature value to float to avoid warning messages
    #--> add your Python code here
    Y=[]
    for rowY in db:
        if rowY == row: pass
        else: 
            if rowY[2] == '+':
                rowY = 1
            else:
                rowY = 0
            Y.append(rowY)

    #store the test sample of this iteration in the vector testSample
    #--> add your Python code here
    if row[2] == '+':
        rowClass = 1
    else:
        rowClass = 0
        
    rowProcessed = [float(row[0]), float(row[1])]
    testSample = rowProcessed;

    #fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

    #use your test sample in this iteration to make the class prediction. For instance:
    #class_predicted = clf.predict([[1, 2]])[0]
    #--> add your Python code here
    class_predicted = clf.predict([testSample])[0]

    #compare the prediction with the true label of the test instance to start calculating the error rate.
    #--> add your Python code here
    if class_predicted != rowClass: numWrong = numWrong + 1

#print the error rate
#--> add your Python code here
errorRate = numWrong/numTotal
print(1 - errorRate)





