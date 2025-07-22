import os
import time

import numpy as np
from PIL import Image
import easyocr

from table_data import players, Player

# Dimensions of player's BB area: x, y, w, h
bb_player = (12, 121, 100, 21)
# Dimensions of user's BB area: x, y, w, h
bb_user = (12, 141, 110, 24)

# Dimensions for value box for user and layer
user_value = (4, 84, 25, 18)
player_value = (3, 66, 23, 16)

def bb_player_recognizer(_image: Image, _player: Player, _ratio: tuple[float, float]) -> str:
    bb_area = _image.crop(_player.bb.to_box(_ratio))
    bb_area = bb_area.resize((bb_area.size[0]*10, bb_area.size[1]*10))
    text =  text_recognizer(bb_area, ['uk'])
    return text

def value_player_recognizer(image: Image, ratio: tuple[float, float]):
    value_area = image.crop(((player_value[0] + 2) / ratio[0],
                             (player_value[1] + 2) / ratio[1],
                             (player_value[0] + player_value[2] - 2) / ratio[0],
                             (player_value[1] + player_value[3] - 2) / ratio[1]))
    value_area = value_area.resize((100, 100))
    value = text_recognizer(value_area, ['en'])
    return value


def text_recognizer(image: Image, lang: list[str]) -> str:
    reader = easyocr.Reader(lang)
    # Run OCR on a Pillow image
    results = reader.readtext(np.array(image))  # img = PIL.Image

    text = []
    if results:
        for result in results:
            text.append(result[1])
        return " ".join(text)
    else:
        # print("No text found.")
        return None

def card_recognizer(image: Image):
    resized = image.resize((100, 100))
    value = text_recognizer(resized, ['en'])
    if value:
        suit = suit_recognizer(image.crop((0,19,3,22)))
        if suit:
            value = value + suit

    return None

def suit_recognizer(_image: Image) -> str:
    suit = None
    if is_point_colored(_image, [[-1, 220, 130]], [[10, 230, 150]]):  # +
        suit =  'H' # Red (Черви)
    elif is_point_colored(_image, [[85, 225, 118]], [[95, 245, 145]]): # +
        suit =  'C' # Green (Крести)
    elif is_point_colored(_image, [[145, 220, 135]], [[155, 230, 150]]): # +
        suit =  'D' # Blue (Бубни)
    elif is_point_colored(_image, [[80, 0, 26],[200, 0, 26]], [[90, 10, 51],[220, 20, 51]]):  #
        suit =  'S' # Black (Піки)
    elif is_point_colored(_image, [[20, 140, 158]], [[35, 187, 180]]):     # +
        suit =  'B' # Yellow (Рубашка)
    else:
        suit =  None

    return suit

def is_point_yellow(_image: Image) -> bool:
    return is_point_colored(_image, [[30, 100, 100]], [[55, 255, 255]])

def is_point_colored(image: Image, lower_bounds: list[list[int]], upper_bounds: list[list[int]], threshold: float = 0.75) -> bool:
    # 1. Convert the area to the HSV color space
    hsv_image = image.convert('HSV')
    hsv_array = np.array(hsv_image)

    # Initialize a combined mask that will be True for any pixel within any of the defined ranges
    combined_mask = np.zeros(hsv_array.shape[:2], dtype=bool)

    # Iterate through each set of lower and upper bounds
    for i in range(len(lower_bounds)):
        lower_threshold = np.array(lower_bounds[i])
        upper_threshold = np.array(upper_bounds[i])

        # Create a mask for the current color range
        current_mask = np.all((hsv_array >= lower_threshold) & (hsv_array <= upper_threshold), axis=-1)

        # Combine with the overall mask using logical OR
        combined_mask = combined_mask | current_mask

    # 4. Calculate the percentage of color pixels from the combined mask
    total_pixels = image.width * image.height
    color_pixels = np.sum(combined_mask)
    percentage = color_pixels / total_pixels

    # 5. Check if the percentage exceeds the threshold
    return percentage >= threshold


def has_player_cards(_image: Image, _player: Player, _ratio: tuple[float, float]) -> (str, bool):
    suit_1 = suit_recognizer(_image.crop(_player.back[0].to_box(_ratio)))
    suit_2 = suit_recognizer(_image.crop(_player.back[1].to_box(_ratio)))
    return f"{suit_1} {suit_2}", (suit_1 is not None) and (suit_2 is not None)

def get_button_player(_players_number: int, image: Image) -> int:
    for i in range(_players_number):
        if is_point_yellow(image.crop(players[i][_players_number].btn.to_box())):
            return i

    return -1



def _test_get_button_player():
    files = [
        "screenshots/screenshot_00011390.png",
        "screenshots/screenshot_00012384.png",
        "screenshots/screenshot_00012880.png",
        "screenshots/screenshot_00013582.png",
        "screenshots/screenshot_00013904.png",
        "screenshots/screenshot_00014832.png",
        "screenshots/screenshot_00014872.png",
        "screenshots/screenshot_00015475.png",
        "screenshots/screenshot_00015478.png",
        "screenshots/screenshot_00019109.png",
    ]
    for f in files:
        print(f, "->", get_button_player(6, Image.open(f)))

def _test_has_player_cards():
    # files = [
    #     "player_00000049.png",
        # "player_00000013.png",
        # "player_00000025.png",
        # "player_00000031.png",
        # "player_00000052.png",
        # "player_00000054.png",
        # "player_00000059.png",
        # "player_00000061.png",
        # "player_00000068.png",
        # "player_00000073.png",
        # "player_00000074.png",
        # "player_00000080.png",
        # "player_00000081.png",
        # "player_00000086.png",
        # "player_00000092.png",
        # "player_00000100.png",
        # "player_00000102.png",
        # "player_00000106.png",
        # "player_00000108.png",
        # "player_00000109.png",
    # ]

    # for f in files:
    #     path = f'screens/players/{f}'
    #     image = Image.open(path)
    #     print(f"{f}: {has_player_cards(image, players[1][6], ratio)}")

    for f in os.listdir('screens/players'):
        path = f'screens/players/{f}'
        image = Image.open(path)
        print(f"{f}: {has_player_cards(image, players[1][6], ratio)}")

def _test_get_player_bb():
    # files = [
    #     "player_00000004.png",
    #     "player_00000010.png",
    #     "player_00000018.png",
    #     "player_00000036.png",
    #     "player_00000042.png",
    #     "player_00000082.png",
    #     "player_00000090.png",
    #     "player_00000096.png",
    #     "player_00000114.png",
    #     ]
    # for f in files:
    for f in os.listdir('screens/players'):
        path = f'screens/players/{f}'
        image = Image.open(path)
        w, h = image.size
        if h == 150:
            print(f"{f}: {bb_player_recognizer(image, players[0][6], ratio)}")
        else:
            print(f"{f}: {bb_player_recognizer(image, players[1][6], ratio)}")

if __name__ == '__main__':
    start = time.time()
    ratio = (1,1)

    # _test_get_button_player()
    # _test_has_player_cards()
    _test_get_player_bb()


    print(f"Time taken: {time.time() - start} seconds")
