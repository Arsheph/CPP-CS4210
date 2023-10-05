#-------------------------------------------------------------------------
# AUTHOR: Joshua Pao
# FILENAME: decision_tree_2.py
# SPECIFICATION: Contact Lenses csv decision trees
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

for ds in dataSets:

    dbTraining = []
    X = []
    Y = []

    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)

    #transform the original categorical training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
    # so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    #--> add your Python code here
    # [Age, Spec, Astig, Tear]
    for instance in dbTraining:
        
        # Age
        if instance[0] == "Young":
            ageVal = 0
        elif instance[0] == "Presbyopic":
            ageVal = 1
        else:
            ageVal = 2
            
        # Spec
        if instance[1] == "Myope":
            specVal = 0
        else:
            specVal = 1
            
        # Astig
        if instance[2] == "No":
            astigVal = 0
        else:
            astigVal = 1
            
        # Tear    
        if instance[3] == "No":
            tearVal = 0
        else:
            tearVal = 1
        
        X.append([ageVal, specVal, astigVal, tearVal])

    #transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    #--> add your Python code here
    # [Class]
    for instance in dbTraining:
        if instance[4] == "No":
            classVal = 0
        else:
            classVal = 1
        Y.append(classVal)

    #loop your training and test tasks 10 times here
    for i in range (10):

       #fitting the decision tree to the data setting max_depth=3
       clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
       clf = clf.fit(X, Y)

       #read the test data and add this data to dbTest
       #--> add your Python code here
       testSet = "contact_lens_test.csv"
       dbTest = []
       with open(testSet, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i > 0: #skipping the header
                   dbTest.append (row)
       
       predictArr = []
       accArr = []
       for instance in dbTest:
           #transform the features of the test instances to numbers following the same strategy done during training,
           #and then use the decision tree to make the class prediction. For instance: class_predicted = clf.predict([[3, 1, 2, 1]])[0]
           #where [0] is used to get an integer as the predicted class label so that you can compare it with the true label
           #--> add your Python code here
           
               # Age
               if instance[0] == "Young":
                   ageVal = 0
               elif instance[0] == "Presbyopic":
                   ageVal = 1
               else:
                   ageVal = 2
                   
               # Spec
               if instance[1] == "Myope":
                   specVal = 0
               else:
                   specVal = 1
                   
               # Astig
               if instance[2] == "No":
                   astigVal = 0
               else:
                   astigVal = 1
                   
               # Tear    
               if instance[3] == "No":
                   tearVal = 0
               else:
                   tearVal = 1
               
               class_predicted = clf.predict([[ageVal, specVal, astigVal, tearVal]])[0]
               predictArr.append(class_predicted)
           
           #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
           #--> add your Python code here
       actualArr = []
       for instance in dbTest:
              if instance[4] == "No":
                  classVal = 0
              else:
                  classVal = 1
              actualArr.append(classVal)
        
       predictIndex = 0
       wrongCount = 0
       for prediction in predictArr:
           if prediction != actualArr[predictIndex]: wrongCount = wrongCount + 1
           predictIndex = predictIndex + 1
       accRate = wrongCount/predictIndex
       accArr.append(accRate)

    #find the average of this model during the 10 runs (training and test set)
    #--> add your Python code here
    avgAcc = 0
    for entry in accArr:
        avgAcc = avgAcc + entry
    avgAcc = avgAcc / 10

    #print the average accuracy of this model during the 10 runs (training and test set).
    #your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    #--> add your Python code here
    print("Accuracy over 10 runs: " + str(avgAcc))
    
    # Disclaimer, I don't even know if the result is actually correct



