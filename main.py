from img import Img
from libs import get_palette_from_data
import time


def main():
    image = Img("https://static.vecteezy.com/ti/vecteur-libre/p1/7528259-chat-cartoon-couleur-clipart-illustration-gratuit-vectoriel.jpg", 200, 200)

    image.change_palette(get_palette_from_data())

    time.sleep(10)

    image.start_drawing(558, 353)

main()