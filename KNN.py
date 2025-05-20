import numpy as np
from math import sqrt
from collections import Counter
class KNN:
    def __init__(self,k,distance_method="euclidean"):
        self.k=k
        self.distance_method=distance_method
   
     #store and spilit data
    def fit(self,x,y):
        self.x_train=x
        self.y_train=y

    def predecit(self,X):
        predecArray=[self._predecit(x) for x in X]
        return predecArray
    # x (new point) xtrain all training data point
    def _predecit(self,x):
        if self.distance_method=="euclidean":
            dists=[self.euclidean_distance(x,x_train)for x_train in self.x_train]
        elif self.distance_method=="manhattan":
            dists=[self.manhattan_distance(x,x_train)for x_train in self.x_train]
        else:
            print("un vaild value")
        #get k nearest neihbour
        k_indecies=np.argsort(dists)[:self.k]
        k_nearest_label=[self.y_train[i]for i in k_indecies]
        #most common class
        most_common=Counter(k_nearest_label).most_common(1)
        return most_common[0][0]
    
    def euclidean_distance(self,x1.x2):
        return sqrt(np.sum(x1-x2)**2)
    def manhattan_distance(self,x1,x2):
        return np.sum(np.abs(x1-x2))