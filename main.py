from img import Img
from libs import get_palette_from_data
import time


def main():
    image = Img("https://img.freepik.com/vecteurs-premium/tigre-dessin-anime-isole-blanc_29190-5158.jpg", 100, 100)

    image.change_palette(get_palette_from_data())

    image.rotate(90)

    time.sleep(10)

    image.start_drawing_speed(558, 353)

main()