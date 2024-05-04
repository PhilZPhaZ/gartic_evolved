from PIL import Image
import numpy as np

def get_closest_color(color, palette):
    # convert color and palette to numpy arrays for faster computation
    color_array = np.array(color)
    palette_array = np.array(palette)

    # calculate the Euclidean distance between color and each color in the palette
    distances = np.sum((palette_array - color_array) ** 2, axis=1)

    # find the index of the closest color
    closest_index = np.argmin(distances)

    # return the closest color
    closest_color = palette[closest_index]
    return closest_color

# create a new image from the given image but with a custom color palette
def create_image_with_custom_palette(image, palette):
    # convert image to numpy array for faster pixel access
    image_array = np.array(image)

    # create a new image array with the same shape as the original image
    new_image_array = np.empty_like(image_array)

    # iterate over the pixels and change the color to the closest color in the palette
    for x in range(image_array.shape[0]):
        for y in range(image_array.shape[1]):
            new_image_array[x, y] = get_closest_color(image_array[x, y], palette)

    # create a new image from the new image array
    new_image = Image.fromarray(new_image_array, mode="RGB")

    return new_image

