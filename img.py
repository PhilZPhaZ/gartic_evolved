from PIL import Image
from libs import *
from process_image import *
from pynput.mouse import Controller, Button
import numpy as np
import time

class Img:
    def __init__(self, url, width, height):
        self.img = get_image_data_from_url(url)
        self.img = resize_image(self.img, width, height)

    def show(self):
        self.img.show()

    def rotate(self, angle):
        self.img = self.img.rotate(angle, expand=True)

    def change_palette(self, palette):
        self.palette = palette
        self.img = create_image_with_custom_palette(self.img, self.palette)

    def start_drawing_slow(self, x_start, y_start):
        self.mouse = Controller()

        image_array = np.array(self.img)

        for x in range(image_array.shape[0]):
            for y in range(image_array.shape[1]):
                color = image_array[x, y]
                self.draw_pixel(5 * x + x_start, 5 * y + y_start, color)

    def draw_pixel(self, x, y, color):
        for color_palette in self.palette:
            if color_palette == tuple(color):
                if tuple(color) != (255, 255, 255):
                    self.mouse.position = get_coords_from_color(color_palette)
                    self.click()

                    self.mouse.position = (x, y)
                    self.click()

                    time.sleep(0.01)
    
    def start_drawing_speed(self, x_start, y_start):
        self.mouse = Controller()

        image_array = np.array(self.img)

        for color_palette in self.palette:
            self.mouse.position = get_coords_from_color(color_palette)
            self.click()

            self.lines(x_start, y_start, x_start, y_start + 20)

            for x in range(image_array.shape[0]):
                for y in range(image_array.shape[1]):
                    color = image_array[x, y]
                    if color_palette == tuple(color):
                        if tuple(color) != (255, 255, 255):
                            self.mouse.position = (5 * x + x_start, 5 * y + y_start)
                            self.click()

                            time.sleep(0.001)
    
    def start_drawing_speed_lines(self, x_start, y_start):
        # same for start_drawing_speed but this time, when there are lines of the same color, draw a line and not a series of points
        self.mouse = Controller()
        
        image_array = np.array(self.img)


    def click(self):
        self.mouse.click(Button.left, 1)
    
    def lines(self, x1, y1, x2, y2):
        self.mouse.press(Button.left)
        self.mouse.move(x2 - x1, y2 - y1)
        self.mouse.release(Button.left)
