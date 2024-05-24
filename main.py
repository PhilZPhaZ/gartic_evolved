from img import Img
from libs import get_palette_from_data
import time


def main():
    image = Img("https://static.vecteezy.com/ti/vecteur-libre/p1/6895992-ordinateur-portable-cartoon-illustration-icone-avec-panneau-lcd-vide-vectoriel.jpg", 100, 100)

    image.change_palette(get_palette_from_data())

    image.rotate(90)

    time.sleep(10)

    image.check_lines()

    image.start_drawing_speed_lines(558, 353)

main()