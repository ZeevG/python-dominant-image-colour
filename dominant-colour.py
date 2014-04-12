import Image


def average_colour(image):
    mean_colour = [None, None, None]

    for val in range(3):
        pixels = image.getdata(val)
        pixel_array = []
        for pixel in pixels:
            pixel_array.append(pixel)

        mean_colour[val] = hex(sum(pixel_array)/len(pixel_array))

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

    return [R, G, B]


def average_colour_in_k_clusters(image, k):
    pass


def main():
    image = Image.open("Lenna.png")
    print average_colour(image)
    print most_frequent_color(image)

if __name__ == "__main__":
    main()
