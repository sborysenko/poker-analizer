# Extract areas for each player and card

from PIL import Image

from recognizer import card_recognizer, value_player_recognizer
from table_data import *

def load_image(image_path):
    img = Image.open(image_name)
    w, h = img.size
    r: tuple[float, float] = (width_ref / w, height_ref / h)

    return img, r


def get_players_number(_image: Image, _ratio: tuple[float, float]):
    for p in range(9, 1, -1):
        _images = extruct_areas(p, _image, _ratio)

        _detected = True
        for i in range(1, len(_images)):
            val = value_player_recognizer(_images[i], _ratio)
            if val is None:
                _detected = False
                break

        if _detected:
            return p

    return 0


def extruct_areas(_players_number: int, _image: Image, _ratio: tuple[float, float]):
    _images: list[Image] = list()
    for i in range(_players_number):
        _images.append(_image.crop((players[i][_players_number][0] / _ratio[0], players[i][_players_number][1] / _ratio[1], (players[i][_players_number][0] + players[i][_players_number][2]) / _ratio[0], (players[i][_players_number][1] + players[i][_players_number][3]) / _ratio[1])))

    return _images


def extract_cards(_image: Image, _ratio: tuple[float, float]):
    extracted_cards: list[Image] = list()
    for i in range(5):
        extracted_cards.append(_image.crop(
            (cards[i][0] / _ratio[0],
             cards[i][1] / _ratio[1],
             (cards[i][0] + cards[i][2]) / _ratio[0],
             (cards[i][1] + cards[i][3]) / _ratio[1])))
    return extracted_cards


if __name__ == '__main__':
    # image_name = "screens/screens/6_players/screenshot_00000006.png"
    image_name = "screens/screens/6_players/screenshot_00000023.png"
    # image_name = "screens/screens/6_players/screenshot_00000046.png"
    # image_name = "screens/screens/6_players/screenshot_00000065.png"
    # image_name = "screens/screens/6_players/screenshot_00000085.png"
    # image_name = "screens/screens/6_players/screenshot_00000089.png"
    # image_name = "screens/screens/6_players/screenshot_00000130.png"
    # image_name = "screens/screens/6_players/screenshot_00000131.png"
    # image_name = "screens/screens/6_players/screenshot_00000147.png"
    # image_name = "screens/screens/6_players/screenshot_00000178.png"
    # image_name = "screens/screens/8_players/screenshot_1.png"
    # image_name = "screens/screens/8_players/screenshot_20.png"
    # image_name = "screens/screens/8_players/screenshot_27.png"
    # image_name = "screens/screens/8_players/screenshot_32.png"
    # image_name = "screens/screens/8_players/screenshot_33.png"

    image, ratio = load_image(image_name)
    get_players_number(image, ratio)

    # image_names = (
    #     "screens/screens/6_players/screenshot_00000006.png",
    #     "screens/screens/6_players/screenshot_00000023.png",
    #     "screens/screens/6_players/screenshot_00000046.png",
    #     "screens/screens/6_players/screenshot_00000065.png",
    #     "screens/screens/6_players/screenshot_00000085.png",
    #     "screens/screens/6_players/screenshot_00000089.png",
    #     "screens/screens/6_players/screenshot_00000130.png",
    #     "screens/screens/6_players/screenshot_00000131.png",
    #     "screens/screens/6_players/screenshot_00000147.png",
    #     "screens/screens/6_players/screenshot_00000178.png"
    # )
    # image_names = (
    #     "screens/screens/7_players/screenshot_8.png",
    #     "screens/screens/7_players/screenshot_9.png",
    #     "screens/screens/7_players/screenshot_23.png"
    # )
    # image_names = (
    #     "screens/screens/8_players/screenshot_1.png",
    #     "screens/screens/8_players/screenshot_20.png",
    #     "screens/screens/8_players/screenshot_27.png",
    #     "screens/screens/8_players/screenshot_32.png",
    #     "screens/screens/8_players/screenshot_33.png"
    # )

    # players_number = 8
    # number = 1
    # for image_name in image_names:
    #     image, ratio = load_image(image_name)
    #
    #     print(f"Extracting {image_name}")
    #     images = extruct_areas(players_number, image, ratio)
    #     for image in images:
    #         image.save(f"screens/players/player_{number:08d}.png")
    #         number += 1

    # image, ratio = load_image(image_name)
    # extracted_cards = extract_cards(image, ratio)
    # for card in extracted_cards:
    #     card_value = card_recognizer(card)
    #     print(card_value)
    #     # card.show()
