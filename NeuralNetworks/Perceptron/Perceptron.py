#!/usr/bin/env python

""""Artificial Neurone: Perceptron"""

__author__ = "William CLOT, williamclot.github.com"
__license__ = "MIT"
__date__ = "27/08/2018"

import random

class Perceptron:
    def __init__(self, input_count):
        self.weights = [random.uniform(0, 1) for i in range(input_count + 1)]
        self.bias = self.weights[0]

    def sign(self, x):
        if (x>0): return 1
        else: return 0

    def feed_forward(self, inputs):
        sigma = 0
        for index, value in enumerate(inputs):
            sigma += value*self.weights[index]
        return self.sign(sigma)

    def test_perceptron(self, inputs):
        sigma = 0
        inputs = [-1] + inputs
        return self.feed_forward(inputs)

    def train(self, training_inputs, desired_output):
        train = []
        for train_input in training_inputs:
    		train.append([-1] + train_input) # adds x0=-1

        done = False
        i = 0
        weights_changed = False

        while not done:
            y = self.feed_forward(train[i])
            error = desired_output[i] - y 

            if (error != 0):
                for j in range(len(self.weights)):
                    self.weights[j]+=error*train[i][j]
                    weights_changed = True
            i += 1
            if (i==len(training_inputs)):
                done = True
                if weights_changed: done=False
                i = 0; weights_changed = False

                


