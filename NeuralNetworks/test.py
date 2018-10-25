#!/usr/bin/env python

import random
import matplotlib.pyplot as plt
import Perceptron

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

Perceptron = Perceptron.Perceptron(2)

def trainPerceptron(trainSet, output):
    print("Initial state of the weights: ")
    print(Perceptron.weights)
    Perceptron.train(trainSet, output)
    print("Final state of the weights: ")
    print(Perceptron.weights)
    print('')

def test(inputs):
    return Perceptron.test_perceptron(inputs)

# -----~~ Dataset ~~-------

AND_Train_Set = [[0, 0],[0, 1], [1, 0], [1, 1]]
AND_Desired_Output = [0, 0, 0, 1]

OR_Train_Set = [[0, 0],[0, 1], [1, 0], [1, 1]]
OR_Desired_Output = [0, 1, 1, 1]

# ------~ Results ~~-------

print("Training for AND binary operation:")
trainPerceptron(AND_Train_Set, AND_Desired_Output)

print(bcolors.OKGREEN+"1 AND 1 : "+str(test([1,1]))+bcolors.ENDC)
print(bcolors.OKGREEN+"0 AND 1 : "+str(test([0,1]))+bcolors.ENDC)
print(bcolors.OKGREEN+"1 AND 0 : "+str(test([1,0]))+bcolors.ENDC)
print(bcolors.OKGREEN+"0 AND 0 : "+str(test([0,0]))+bcolors.ENDC)
print('')

print("Training for OR binery operation:")
trainPerceptron(OR_Train_Set, OR_Desired_Output)

print(bcolors.OKGREEN+"1 OR 1 : "+str(test([1,1]))+bcolors.ENDC)
print(bcolors.OKGREEN+"0 OR 1 : "+str(test([0,1]))+bcolors.ENDC)
print(bcolors.OKGREEN+"1 OR 0 : "+str(test([1,0]))+bcolors.ENDC)
print(bcolors.OKGREEN+"0 OR 0 : "+str(test([0,0]))+bcolors.ENDC)
print('')
