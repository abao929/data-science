from operator import truediv
import numpy as np
import random
import math
import time

class Kmeans:
    def __init__(self, X, K, max_iters):
        # Data
        self.X = X
        # Number of clusters
        self.K = K
        # Number of maximum iterations
        self.max_iters = max_iters
        # Initialize centroids
        self.centroids = self.init_centroids()

    def init_centroids(self):
        """
        Selects k random rows from inputs and returns them as the chosen centroids.
        You should randomly choose these rows without replacement and only
        choose from the unique rows in the dataset. Hint: look at
        Python's random.sample function as well as np.unique
        :return: a Numpy array of k cluster centroids, one per row
        """
        # TODO
        unique = np.unique(self.X, axis=0).tolist()
        cent = np.array(random.sample(unique, self.K))
        self.centroids = cent
        print(cent)
        return cent

    def euclidean_dist(self, x, y):
        """
        Computes the Euclidean distance between two points, x and y

        :param x: the first data point, a Python numpy array
        :param y: the second data point, a Python numpy array
        :return: the Euclidean distance between x and y
        """
        # TODO
        return np.linalg.norm(abs(x-y))

    def closest_centroids(self):
        """
        Computes the closest centroid for each data point in X, returning
        an array of centroid indices

        :return: an array of centroid indices
        """
        # TODO
        indices = []
        for x in self.X:
            min = np.inf
            ind = 0          
            for c in range(len(self.centroids)):
                dist = self.euclidean_dist(x, self.centroids[c])
                if dist < min:
                    min = dist
                    ind = c
            indices.append(ind)
        return np.array(indices)


    def compute_centroids(self, centroid_indices):
        """
        Computes the centroids for each cluster, or the average of all data points
        in the cluster. Update self.centroids.

        Check for convergence (new centroid coordinates match those of existing
        centroids) and return a Boolean whether k-means has converged

        :param centroid_indices: a Numpy array of centroid indices, one for each datapoint in X
        :return boolean: whether k-means has converged
        """
        # TODO
        start = time.time()
        new_cents = []
        for x in range(len(self.centroids)):
            new_cents.append(np.mean(self.X[centroid_indices == x], axis=0))
        old_cents = self.centroids
        # print(f'centroid indices are: {centroid_indices}')
        # print(f'old cents is: {old_cents}')
        # print(f'new cents is: {new_cents}')
        # print(f'both should be: {self.K}')
        self.centroids = np.array(new_cents)
        print(f'centroids took {time.time() - start} seconds to run')
        return bool(np.all(old_cents == new_cents))

    def run(self):
        """
        Run the k-means algorithm on dataset X with K clusters for max_iters.
        Make sure to call closest_centroids and compute_centroids! Stop early
        if algorithm has converged.
        :return: a tuple of (cluster centroids, indices for each data point)
        Note: cluster centroids and indices should both be numpy ndarrays
        """
        # TODO
        indices = self.closest_centroids()
        count = 0
        start = time.time()
        while self.compute_centroids(indices) is False and count < self.max_iters:
            indices = self.closest_centroids()
            print(f'cycle {count} total time is {time.time() - start} seconds')
            count += 1
        return (self.centroids, indices)

    def inertia(self, centroids, centroid_indices):
        """
        Returns the inertia of the clustering. Inertia is defined as the
        sum of the squared distances between each data point and the centroid of
        its assigned cluster.

        :param centroids - the coordinates that represent the center of the clusters
        :param centroid_indices - the index of the centroid that corresponding data point it closest to
        :return inertia as a float
        """
        # TODO
        dist = 0
        for x in range(len(self.X)):
            dist += np.square(self.euclidean_dist(self.X[x], centroids[centroid_indices[x]]))
        return dist