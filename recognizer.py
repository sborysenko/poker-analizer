import os
import time

import numpy as np
from PIL import Image
import easyocr

# Dimensions of player's BB area: x, y, w, h
bb_player = (12, 121, 100, 21)
# Dimensions of user's BB area: x, y, w, h
bb_user = (12, 141, 110, 24)

# Dimensions for value box for user and layer
user_value = (4, 84, 25, 18)
player_value = (3, 66, 23, 16)

def bb_player_recognizer(image: Image, ratio: tuple[float, float]):
    bb_area = image.crop((bb_player[0] / ratio[0],
                          bb_player[1] / ratio[1],
                          (bb_player[0] + bb_player[2]) / ratio[0],
                          (bb_player[1] + bb_player[3]) / ratio[1]))
    # bb_area.show()

    text_recognizer(bb_area, ratio)

def bb_user_recognizer(image: Image, ratio: tuple[float, float]):
    bb_area = image.crop((bb_user[0] / ratio[0],
                          bb_user[1] / ratio[1],
                          (bb_user[0] + bb_user[2]) / ratio[0],
                          (bb_user[1] + bb_user[3]) / ratio[1]))
    # bb_area.show()

    return text_recognizer(bb_area)

def value_player_recognizer(image: Image, ratio: tuple[float, float]):
    value_area = image.crop(((player_value[0] + 2) / ratio[0],
                             (player_value[1] + 2) / ratio[1],
                             (player_value[0] + player_value[2] - 2) / ratio[0],
                             (player_value[1] + player_value[3] - 2) / ratio[1]))
    value_area = value_area.resize((100, 100))
    value_area.show()
    value = text_recognizer(value_area)
    return value


def text_recognizer(image: Image):
    reader = easyocr.Reader(['en'])
    # Run OCR on a Pillow image
    results = reader.readtext(np.array(image))  # img = PIL.Image

    if results:
        # Each result is (bbox, text, confidence)
        best_result = max(results, key=lambda x: x[2])
        bbox, text, confidence = best_result
        # print(f"Most confident result: '{text}' (confidence: {confidence:.2f})")
        return text
    else:
        # print("No text found.")
        return None

def card_recognizer(image: Image):
    # image.show()
    resized = image.resize((100, 100))
    value = text_recognizer(resized)
    if value:
        value = value + suit_recognizer(image.crop((0,19,3,22)))

    return value

def suit_recognizer(image: Image):
    r, g, b = image.getpixel((1, 1))

    if r > 100 and g < 90 and b < 90:
        return 'H'
    elif g > 100 and r < 90 and b < 90:
        return 'C'
    elif b > 100 and r < 90 and g < 90:
        return 'D'
    elif r < 50 and g < 50 and b < 50:
        return 'S'
    else:
        return ''

if __name__ == '__main__':
    start = time.time()
    ratio = (1,1)

    for f in os.listdir('screens/cards'):
        path = f'screens/cards/{f}'
        print(path)
        card_recognizer(Image.open(path))

    # bb_user_recognizer(Image.open('screens/players/player_a.png'), ratio)
    # bb_player_recognizer(Image.open('screens/players/player_b.png'), ratio)
    # bb_player_recognizer(Image.open('screens/players/player_c.png'), ratio)
    # bb_player_recognizer(Image.open('screens/players/player_d.png'), ratio)
    # bb_player_recognizer(Image.open('screens/players/player_e.png'), ratio)
    # bb_player_recognizer(Image.open('screens/players/player_f.png'), ratio)
    # bb_player_recognizer(Image.open('screens/players/player_g.png'), ratio)
    # bb_player_recognizer(Image.open('screens/players/player_h.png'), ratio)

    print(f"Time taken: {time.time() - start} seconds")
