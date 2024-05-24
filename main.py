from img import Img
from libs import get_palette_from_data
import time


def main():
    image = Img("https://media.discordapp.net/attachments/910960207465680959/1081664497934151760/3B3616EF-EB6C-49F1-9E2A-3E9CB299D547.jpg?ex=665197d0&is=66504650&hm=12a1f12e04e70f7c0d18aff57bd2246aeff62fb007f926babb60f46cc3c48fd7&=&format=webp&width=611&height=621", 100, 100)

    image.change_palette(get_palette_from_data())

    image.rotate(90)

    time.sleep(10)

    image.check_lines()

    image.start_drawing_speed_lines(558, 353)
    # image.start_drawing_speed(558, 353)

main()