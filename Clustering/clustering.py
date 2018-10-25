#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import random as rd

def open_dataset():
    
    data_object = open("data/g3-generated.txt", "r")
    data = data_object.readlines()
    # Formatting the data in a python list
    data = data[0].split(';')

    x = []
    y = []

    for i in range(len(data)//2) : 
        x.append(data[2*i])
        y.append(data[2*i+1])
    return x, y

x, y = open_dataset()

if (len(x) == len(y)):
    plt.plot(x, y, 'ro', alpha=0.3)
    plt.axis('off')
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.show()

