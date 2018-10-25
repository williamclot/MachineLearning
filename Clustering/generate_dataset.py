#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import random as rd

def generate_dataset(k=3, sigma=7, size=400):
    '''Function generating the dataset with k different gaussian clusters'''

    colors=['green', 'blue', 'red', 'purple', 'orange', 'gray']
    file = open('testfile.txt','w') 
    
    def gaussian2D(mu, sigma, size):
        '''Function generating the gaussian 2D distribution around each centroid'''
        x, y = [], []
        for i in range(size):
            x.append(rd.gauss(mu['x'], sigma))
            y.append(rd.gauss(mu['y'], sigma))
        return x,y

    for i in range(k):
        # Fixing some random points in space as centroids for the gaussian distribution
        ck = {'x': rd.random()*100, 'y': rd.random()*100}
        x, y = gaussian2D(ck, sigma, size)
        for j in range(size):
            file.write(str(x[j])+';'+str(y[j])+';')
        plt.plot(x, y, 'ro', alpha=0.3, color=colors[i])
        plt.plot(ck['x'], ck['y'], 'ro', color='black')


    plt.axis('off')
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.show()
    file.close() 


generate_dataset()


