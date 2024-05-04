import requests
import json
from PIL import Image
from io import BytesIO

def get_image_data_from_url(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

def get_palette_from_data():
    palette = []
    # open data.json and get the palette
    with open('data.json', 'r') as file:
        data = json.load(file)
        for elem in data:
            palette.append(tuple(elem['color']))

    return palette

def get_coords_from_color(color):
    with open('data.json', 'r') as file:
        data = json.load(file)
        for elem in data:
            if tuple(elem['color']) == color:
                return (elem['x'], elem['y'])

# resize image but keep the ratio
def resize_image(image, width, height):
    original_width, original_height = image.size
    ratio = min(width / original_width, height / original_height)
    new_width = int(original_width * ratio)
    new_height = int(original_height * ratio)
    new_image = image.resize((new_width, new_height))
    return new_image
