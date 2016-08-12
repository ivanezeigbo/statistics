'''
Finding optimal k- Nearest Neighbor
data for this file is titled 'knn_data.csv' and also uploaded on Github
'''

#first I retrieved the file containing the data using the function 'loadDataSet"..

#NOTE: data for this code has been uploaded on Github and titled 'knn_data.csv'

import csv
import random
def loadDataset(filename, trainingSet=[] , testSet=[]):
    with open(filename) as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        #Next, I convert the two coordinates from their original string form to float.
        for x in range(len(dataset)):
            for y in range(2):
                dataset[x][y] = float(dataset[x][y])
            #Then I append every list in the data into the general lists: trainingSet and testSet
            #In order to brute force, I append all data in the training and test Set, so it searches through all neighbors.
            trainingSet.append(dataset[x])
            testSet.append(dataset[x])
#The next function calculates the distance between a neighbor from on reference testSet point/
#test instance. To minimize lines of codes, I import math.
import math
def euclideanDistance(instance1, instance2, length):
    #in calculating the euclidean distance, I initially assign zero to distance. Distance is to be the sum of the square of the differences of the coordinates.
    distance = 0
    #length here is number of coordinates I am considering for calculating distance. Here it would just be 2: x and y
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
        #to obtain the euclidean distance, I return the square root of distance.
    return math.sqrt(distance)
    #The next function provides the closest neighbors according to the k value given in main(). For instance, for k = 2, it returns the two closest neighbors.
    #It takes three inputs, the entire training set, the single point of the test set, and the k nearest neighbor value.
import operator
def getNeighbors(trainingSet, testInstance, k):
    #I produce an empty list, distance.
    distances = []
    #Here, I calculate length, subtracting one to exclude the label, and utilizing length in the euclidean distance function.
    length = len(testInstance) - 1
    #I then remove the test Instance from the training Set, so it that the test Instance does not calculate on itself but on its neighboring points.
    trainingSet.remove(testInstance)
    #Then I brute force, calculating the distance of the test Instance from every neighbor around the test Instance; i.e. every other point in the data.
    for x in range(len(trainingSet)):
        #here I call the euclidean distance function to obtain my distance.
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        #I then append a list of the training set Instance I am using and its distance from the test Instance into my empty list named distance.
        distances.append((trainingSet[x], dist))
    #I sort the list in the general diistance list in increasing order of distance ('dist')
    distances.sort(key=operator.itemgetter(1))
    #I then create an empty list where I can include my neighbors. For every reiteration of 'x' which calls this function in a 'for' loop in main(), this list is made empty again.
    neighbors = []
    #I then determine the nearest neighbors for the k value; i.e 2 neighbors for k = 2, 3 for 3 etc.
    for x in range(k):
        #Then I append the nearest neighbors into my empty list, neighbors.
        neighbors.append(distances[x][0])
        #Finally, I return my empty list, neighbors.
    return neighbors

#Then I create a function that predicts the label of the test Instance used in the function getNeighbors(a, b, c).
def getResponse(neighbors):
    #First, I create an empty dictionary.
    classVotes = {}
    for x in range(len(neighbors)):
        #It checks through all neighbors, according to k, and assigns response to the label (or last element in the list of neighbors) of each neighbor for each loop.
        response = neighbors[x][-1]
        #Then it adds 1 to the value of response if the dictionary already has a key with the same label, same 'response', else it creates a key of the label, response, and assigns it the value 1.
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
            #It then creates a tuple of the sorted dictionary, Class Votes, sorted according to the value of response in descending order.
    sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
    #Finally, it returns the most occuring label.
    return sortedVotes[0][0]

#This is just a function that produces a list of the coordinates and with my predicted label for plotting the graph.
#It accepts two inputs, the entire test Set and the result from getResponse; i.e. the predicted label.

def createpredictionLabel_list(testSet, predict):
    #I create an empty list for my predicted list.
    predictionLabel = []
    #Then I replace every label in the testSet with my predicted label.
    for x in range(len(testSet)):
        testSet[x].remove(testSet[x][-1])
        testSet[x].append(predict[x])
        #I then append the new testSet to my predicted label
        predictionLabel.append(testSet[x])
        #Finally, I return my predicted list.
    return predictionLabel

#The next function just compares the predicted label to the actual label to calculate accuracy of prediction.
#It accepts the input, the list of test Set, and the list of results from getResponse() made in main().

def getAccuracy(testSet, predictions):
    #I assign correct an initial value of 0.
    correct = 0
    for x in range(len(testSet)):
        #for everytime the prediction corresponds with the actual label, correct increases by 1.
        if testSet[x][-1] is predictions[x]:
            correct += 1
    #Then I return the accuracy: the number of correct ones over the total runs multiplied by 100.
    print ("correct:", correct, "testSet:", len(testSet))
    return (correct/(float(len(testSet)))) * 100.0

#This function plots my scatterplot for either the actual list or the predicted list
#first I import matplotlib.pyplot
import matplotlib.pyplot
import pylab

def Dataplot(data):
    #I create an empty list to distinguish the data according to their label
    label0 = []
    label1 = []
    #append either to label0 or label1 according to label
    for x in range(len(data)):
        if data[x][-1] == '0':
            label0.append(data[x])
        else:
            label1.append(data[x])
    #create x and y coordinate list for either both labels. x0 and y0 for label of 0 and x1 and y1 for label of 1.
    x0 = []
    y0 = []
    x1 = []
    y1 = []
    print (label0)
    print (label1)
    
    for x in range(len(label0)):
        x0.append(label0[x][0])
        y0.append(label0[x][1])
    for y in range(len(label1)):
        x1.append(label1[y][0])
        y1.append(label1[y][1])
        
    #color plots for label 0 red and that for label 1 green.
    matplotlib.pyplot.scatter(x0,y0, color='blue')
    matplotlib.pyplot.scatter(x1,y1, color='green')
    matplotlib.pyplot.show() #shows plot of graph
    
#This is the function that calls the other functions in calculating the k Nearest Neighbor. It also does the optimization of the algorithm.
def main():
    # prepare data
    #creates empty lists for training and test sets
    trainingSet=[]
    testSet=[]
    #calls the function that retrieves and appends training set and test set.
    loadDataset('knn_data.csv', trainingSet, testSet)
    print ('Train set: ' + repr(len(trainingSet)))
    print ('Test set: ' + repr(len(testSet)))
    k = 1 #asscribes k an initial value of 1.
    
    #empty lists optimizer and optimizerChecker serve for optimization.
    #optimizer stops the code from continously running when a likely optimal is reached, while optimizerChecker sorts according to the accuracy to find the optimal k.
    optimizer = []
    optimizerChecker = []
    #k Neighbors should be greater than 0 but less than 600; that is excluding the testInstance.
    while k > 0 and k <= (len(testSet)- 1):
        #predictions is the empty list where results from getResponse() is appended to compare with the testSet in getAccuracy()
        #listMaker creates a list of [k, accuracy] which it appends to optimizerChecker.
        predictions = []
        listMaker = []
        #I create an empty list similar to the above list predictions, but for my optimal k predicted list.
        optimal_prediction = []
        #this for loop tests the neighbors of every list or element in the testSet.
        for x in range(len(testSet)):
            #Here I created a new empty list for trainingSet and testSet because of the trainingSet.remove[testInstance] in getNeighbors()
            #This creates a new trainingSet for a new testInstance, thereby including the previously excluded testInstance back into the trainingSet for another iteration.
            trainingSet = []
            testSet = []
            loadDataset('knn_data.csv', trainingSet, testSet)
            #I call the getNeighbors function with the specified k Neighbor value to get the list of neighbors.
            neighbors = getNeighbors(trainingSet, testSet[x], k)
            #I use the neighbors as input in getResponse() to get the predictions
            result = getResponse(neighbors)
            #Then the predictions called 'result' is appended to the list called predictions
            predictions.append(result)
        #since the prediction list is arranged in the same order as the testInstance used in calculating them is arranged in testSet, I can then determine the accuracy by calling the function getAccuracy()
        accuracy = getAccuracy(testSet, predictions)
        print('Accuracy: ' + repr(accuracy) + '%', 'k =', k)
        #Optimization Part
        #with every calculated accuracy, the accuracy is appended to the list optimizer
        optimizer.append(accuracy)
        #the listMaker appends k and accuracy to create a list which is then appended to optimizerChecker.
        #for every iteration of k, the listMaker assumes the initially assigned empty list.
        listMaker.append(k)
        listMaker.append(accuracy)
        optimizerChecker.append(listMaker)
        #Now, in a series of iterations as k Nearest neighbor increases, if the last four show descent or no improvement in accuracy at all, the iteration stops.
        #that is if say x4 >= x3 >= x2 >= x1; thee is no improvement so the iteration stops. The optimization must be carried out if at least 4 nearest neighbors have been calculated.
        if (len(optimizer)>= 4) and (optimizer[-4] >= optimizer[-3])and (optimizer[-3] >= optimizer[-2]) and (optimizer[-2] >= optimizer[-1]):
            #optimizerChecker then sorts the listMakers according to descending magnitude of accuracy.
            optimizerChecker.sort(key=operator.itemgetter(1), reverse = True)
            #the optimal k Nearest Neighbor then becomes the first listMaker, the one with the highest accuracy.
            optimal_k = optimizerChecker[0][0]
            #this one just provides the accuracy of the optimal k Nearest neighbor.
            optimal_kAccuracy = optimizerChecker[0][1]
            print ("Optimal k Nearest Neighbor Value is", optimal_k, "and it has an accuracy of", str(optimal_kAccuracy) + ".")
            print ("Test list:", testSet)
            #plot test Set
            Dataplot(testSet)
            #in order to avoid tampering much with the testSet, I created a replica, testSet1, which becomes my input in my function that creates a predicted list.
            testSet1 = testSet
            #I then assign k as the optimal k to enable me follow the initial procedure in producing the predicted list from the function, createpredictionLabel_list()
            k = optimal_k
            for x in range(len(testSet)):
                trainingSet = []
                testSet = []
                loadDataset('knn_data.csv', trainingSet, testSet)
                neighbors = getNeighbors(trainingSet, testSet[x], k)
                result = getResponse(neighbors)
                optimal_prediction.append(result)
            predictionLabel_list = createpredictionLabel_list(testSet1, optimal_prediction)
            print ("Prediction Label List:", predictionLabel_list)
            #plot prediction list
            Dataplot(predictionLabel_list)
            #finally it returns the optimal k Nearest neighbor.
            return optimal_k
        else:
            k += 1 #if not, k increments by 1 and the iteration continues.
    #if it is possible that no sign that an optimal has been reached is detected (which is, by the way, likely impossible), the code runs for all possible k Nearest Neighbors, and then it picks the most optimal k from them all.
    #it follows a similar process with the if conditional, returning the optimal k of all results.

    optimizerChecker.sort(key=operator.itemgetter(1), reverse = True)
    optimal_k = optimizerChecker[0][0]
    optimal_kAccuracy = optimizerChecker[0][1]
    print ("Test list:", testSet)
    #plot testSet
    Dataplot(testSet)
    testSet1 = testSet
    k = optimal_k
    for x in range(len(testSet)):
        trainingSet = []
        testSet = []
        loadDataset('knn_data.csv', trainingSet, testSet)
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors)
        optimal_prediction.append(result)
        
    predictionLabel_list = createpredictionLabel_list(testSet1, predictions)
    print ("Prediction Label List:", predictionLabel_list)
    
    #plot predition list
    Dataplot(predictionLabel_list)
    print ("Optimal k Neighbors = ", optimal_k, "and it has an accuracy of", str(optimal_kAccuracy) + ".")
    return optimal_k


main() #here I run the main() function to find the k Nearest Neighbors.

