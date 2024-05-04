from PIL import Image
from libs import *
from process_image import *
from pynput.mouse import Controller, Button
import numpy as np
import time

class Img(Image.Image):
    def __init__(self, url, width, height):
        super().__init__()

        self.img = get_image_data_from_url(url)
        self.img = resize_image(self.img, width, height)
    
    def show(self):
        self.img.show()

    def change_palette(self, palette):
        self.palette = palette
        self.img = create_image_with_custom_palette(self.img, self.palette)

    def start_drawing(self, x_start, y_start):
        self.mouse = Controller()
        
        image_array = np.array(self.img)

        for x in range(image_array.shape[0]):
            for y in range(image_array.shape[1]):
                color = image_array[x, y]
                self.draw_pixel(x + x_start, y + y_start, color)

                time.sleep(0.001)

    def draw_pixel(self, x, y, color):
        for color_palette in self.palette:
            if color_palette == tuple(color):
                self.mouse.position = get_coords_from_color(color_palette)
                self.click()

                self.mouse.position = (x, y)
                self.click()

    def click(self):
        self.mouse.click(Button.left, 1)



