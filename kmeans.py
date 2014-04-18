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

    def __init__(self, image, size=200):
        self.image = image
        self.image.thumbnail((size, size))
        self.pixels = numpy.array(image.getdata(), dtype=numpy.uint8)

    def run(self, k):
        self.clusters = [None for i in range(k)]
        self.oldClusters = None

        randomPixels = random.sample(self.pixels, k)

        for idx in range(k):
            self.clusters[idx] = Cluster()
            self.clusters[idx].centroid = randomPixels[idx]

        iterations = 0

        while self.shouldExit(iterations):

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

        if iterations >= 3:
            return False

        return True

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
        localPixels = numpy.asarray(localPixels).astype('uint8').reshape((h, w, 3))
        colourMap = Image.fromarray(localPixels)
        colourMap.show()


def main():

    image = Image.open("images/spikey_thing.jpg")
    # image = image.convert(mode="CMYK")

    k = Kmeans(image, size=200)
    result = k.run(3)
    print result

    k.showImage()
    k.showCentroidColours()
    k.showClustering()

if __name__ == "__main__":
    main()
