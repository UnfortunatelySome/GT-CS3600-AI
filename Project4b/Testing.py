from NeuralNetUtil import buildExamplesFromCarData,buildExamplesFromPenData
from NeuralNet import buildNeuralNet
import cPickle 
from math import pow, sqrt
from numpy import *

def average(argList):
    return sum(argList)/float(len(argList))

def stDeviation(argList):
    mean = average(argList)
    diffSq = [pow((val-mean),2) for val in argList]
    return sqrt(sum(diffSq)/len(argList))

penData = buildExamplesFromPenData() 
def testPenData(hiddenLayers = [24]):
    return buildNeuralNet(penData,maxItr = 200, hiddenLayerList =  hiddenLayers)

carData = buildExamplesFromCarData()
def testCarData(hiddenLayers = [16]):
    return buildNeuralNet(carData,maxItr = 200,hiddenLayerList =  hiddenLayers)
#car = []
#pen = []
#for _ in range(5):
    #result = testPenData()
    #car.append(result[1])
    #result = testPenData()
    #pen.append(result[1])
#a = sum(car)/float(len(car))
#print std(car, axis = 0)
#print("Pen avg, max, std.", a, max(car), std(car, axis = 0))

f = open("results7.txt", "w")
for i in range(0, 4, 5):
    #pen = []
    car = []
    for _ in range(5):
        #print "car", i
	result = testPenData([i])
        car.append(result[1])
    a = sum(car)/float(len(car))
    f.write("Pen " + str(i) + "\n")
    f.write(str(a) + "\n" + str(max(car)) + "\n" + str(std(car, axis = 0)) + "\n")
f.close()
