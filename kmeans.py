"""
Kmeans clustering algorithm for colour detection in images

Initialise a kmeans object and then use the run() method.
Several debugging methods are available which can help to
show you the results of the algorithm.
"""

import Image
import random
import numpy


class Cluster(object):

    def __init__(self):
        self.pixels = []
        self.centroid = None

    def addPoint(self, pixel):
        self.pixels.append(pixel)

    def setNewCentroid(self):

        R = [colour[0] for colour in self.pixels]
        G = [colour[1] for colour in self.pixels]
        B = [colour[2] for colour in self.pixels]

        R = sum(R) / len(R)
        G = sum(G) / len(G)
        B = sum(B) / len(B)

        self.centroid = (R, G, B)
        self.pixels = []

        return self.centroid


class Kmeans(object):

    def __init__(self, k=3, max_iterations=5, min_distance=5.0, size=200):
        self.k = k
        self.max_iterations = max_iterations
        self.min_distance = min_distance
        self.size = (size, size)

    def run(self, image):
        self.image = image
        self.image.thumbnail(self.size)
        self.pixels = numpy.array(image.getdata(), dtype=numpy.uint8)

        self.clusters = [None for i in range(self.k)]
        self.oldClusters = None

        randomPixels = random.sample(self.pixels, self.k)

        for idx in range(self.k):
            self.clusters[idx] = Cluster()
            self.clusters[idx].centroid = randomPixels[idx]

        iterations = 0

        while self.shouldExit(iterations) is False:

            self.oldClusters = [cluster.centroid for cluster in self.clusters]

            print iterations

            for pixel in self.pixels:
                self.assignClusters(pixel)

            for cluster in self.clusters:
                cluster.setNewCentroid()

            iterations += 1

        return [cluster.centroid for cluster in self.clusters]

    def assignClusters(self, pixel):
        shortest = float('Inf')
        for cluster in self.clusters:
            distance = self.calcDistance(cluster.centroid, pixel)
            if distance < shortest:
                shortest = distance
                nearest = cluster

        nearest.addPoint(pixel)

    def calcDistance(self, a, b):

        result = numpy.sqrt(sum((a - b) ** 2))
        return result

    def shouldExit(self, iterations):

        if self.oldClusters is None:
            return False

        for idx in range(self.k):
            dist = self.calcDistance(
                numpy.array(self.clusters[idx].centroid),
                numpy.array(self.oldClusters[idx])
            )
            if dist < self.min_distance:
                return True

        if iterations <= self.max_iterations:
            return False

        return True

    # ############################################
    # The remaining methods are used for debugging
    def showImage(self):
        self.image.show()

    def showCentroidColours(self):

        for cluster in self.clusters:
            image = Image.new("RGB", (200, 200), cluster.centroid)
            image.show()

    def showClustering(self):

        localPixels = [None] * len(self.image.getdata())

        for idx, pixel in enumerate(self.pixels):
                shortest = float('Inf')
                for cluster in self.clusters:
                    distance = self.calcDistance(cluster.centroid, pixel)
                    if distance < shortest:
                        shortest = distance
                        nearest = cluster

                localPixels[idx] = nearest.centroid

        w, h = self.image.size
        localPixels = numpy.asarray(localPixels)\
            .astype('uint8')\
            .reshape((h, w, 3))

        colourMap = Image.fromarray(localPixels)
        colourMap.show()


def main():

    image = Image.open("images/cows.jpg")

    k = Kmeans()

    result = k.run(image)
    print result

    k.showImage()
    k.showCentroidColours()
    k.showClustering()

if __name__ == "__main__":
    main()
