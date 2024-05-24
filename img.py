import itertools
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
            if color_palette == tuple(color) and tuple(color) != (255, 255, 255):
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

            for x in range(image_array.shape[0]):
                for y in range(image_array.shape[1]):
                    color = image_array[x, y]
                    if color_palette == tuple(color) and tuple(color) != (255, 255, 255):
                        self.mouse.position = (5 * x + x_start, 5 * y + y_start)
                        self.click()

                        time.sleep(0.001)


    def start_drawing_speed_lines(self, x_start, y_start):
        # same for start_drawing_speed but this time, when there are lines of the same color, draw a line and not a series of points
        self.mouse = Controller()

        image_array = np.array(self.img)

        self.heigh = image_array.shape[0]

        for color_palette in self.palette:
            self.mouse.position = get_coords_from_color(color_palette)
            self.click()

            for index, start_pixel in self.lines.items():
                if color_palette == start_pixel[2] and start_pixel[2] != (255, 255, 255):
                    x_start_line, y_start_line = start_pixel[0], start_pixel[1]
                    self.mouse.position = (5 * x_start_line + x_start, 5 * y_start_line + y_start)
                    self.press()

                    try:
                        end_pixel = self.lines[index + 1]
                        y_end_line = end_pixel[1] - 1

                        relative_y = y_end_line - y_start_line

                        time.sleep(0.002)

                        self.move_from_relative_y(relative_y)
                    except KeyError:
                        relative_y = self.heigh - y_start_line

                        self.move_from_relative_y(relative_y)

    def move_from_relative_y(self, relative_y):
        self.mouse.move(0, 5 * relative_y)

        time.sleep(0.0001)

        self.release()

    def click(self):
        self.mouse.click(Button.left, 1)

    def press(self):
        self.mouse.press(Button.left)

    def release(self):
        self.mouse.release(Button.left)

    def check_lines(self):
        image_array = np.array(self.img)

        self.lines = {}

        idx = 0

        for x, y in itertools.product(range(image_array.shape[0]), range(image_array.shape[1])):
            color = tuple(image_array[x, y])
            last_color = tuple(image_array[x, y-1])

            try:
                # check if the last color was the same
                if color == last_color:
                    continue
                else:
                    self.lines[idx] = [x, y, color]
            except IndexError:
                self.lines[idx] = [x, y, color]

            idx += 1
