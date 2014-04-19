import Image
import sys



def average_colour(image):

    colour_tuple = [None, None, None]
    for channel in range(3):

        # Get data for one channel at a time
        pixels = image.getdata(band=channel)

        values = []
        for pixel in pixels:
            values.append(pixel)

        colour_tuple[channel] = sum(values) / len(values)

    return tuple(colour_tuple)


def most_frequent_colour(image):

    w, h = image.size
    pixels = image.getcolors(w * h)

    most_frequent_pixel = pixels[0]

    for count, colour in pixels:
        if count > most_frequent_pixel[0]:
            most_frequent_pixel = (count, colour)

    return most_frequent_pixel[1]


def average_colour_in_k_clusters(image, k):
    pass


def compare(title, image, colour_tuple):
    image.show(title=title)
    image = Image.new("RGB", (200, 200,), colour_tuple)
    return image


def kmeans(pixels, k):
    numFeatures = len(pixels)

    centroids = getRandomCentroids(numFeatures, k)

    iterations = 0
    oldCentroids = None

    while not shouldStop(oldCentroids, centroids, iterations):

        oldCentroids = centroids

        interations += 1


def save(name, result, image):
    image.save("images/results/{}.jpg".format(name))
    sample = Image.new("RGB", (200, 200,), result)
    sample.save("images/results/{}-result.jpg".format(name))


def main():
    image = Image.open("images/DSC_6883.jpg")

    if "mode" in sys.argv:
        result = most_frequent_colour(image)

    if "ave" in sys.argv:
        result = average_colour(image)

    save("Wheatbelt", result, image) 


if __name__ == "__main__":
    main()
