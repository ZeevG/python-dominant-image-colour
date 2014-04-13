import Image
import sys



def average_colour(image):
    mean_colour = [None, None, None]
    colour_tuple = [None, None, None]

    for val in range(3):
        pixels = image.getdata(val)
        pixel_array = []
        for pixel in pixels:
            pixel_array.append(pixel)

        colour_tuple[val] = sum(pixel_array)/len(pixel_array)
        mean_colour[val] = hex(sum(pixel_array)/len(pixel_array))

    compare("Average", image, tuple(colour_tuple))

    return mean_colour


def most_frequent_color(image):

    w, h = image.size
    pixels = image.getcolors(w * h)

    most_frequent_pixel = pixels[0]

    for pixel in pixels[1:]:
        if pixel[0] > most_frequent_pixel[0]:
            most_frequent_pixel = pixel

    R = hex(most_frequent_pixel[1][0])
    G = hex(most_frequent_pixel[1][1])
    B = hex(most_frequent_pixel[1][2])

    compare("Most Common", image, most_frequent_pixel[1])

    return [R, G, B]


def average_colour_in_k_clusters(image, k):
    pass


def compare(title, image, colour_tuple):
    image.show(title=title)
    image = Image.new("RGB", (50, 50,), colour_tuple)
    image.show(title=title)


def kmeans(pixels, k):
    numFeatures = len(pixels)

    centroids = getRandomCentroids(numFeatures, k)

    iterations = 0
    oldCentroids = None

    while not shouldStop(oldCentroids, centroids, iterations):

        oldCentroids = centroids

        interations += 1

        

def main():
    image = Image.open("images/spikey_thing.jpg")

    if "mode" in sys.argv:
        print most_frequent_color(image)
    if "ave" in sys.argv:
        print average_colour(image)


if __name__ == "__main__":
    main()
