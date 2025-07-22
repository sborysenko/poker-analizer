# Data for players and cards locations on different tables
#
# Reference dimensions: w = 850, h = 615
#
# User player area w = 132, h  = 170
# Players positions and areas: w = 120, h = 146.
# Players positions: A, B, C, D, E, F, G, H, I. Position A is for user Player. All other positions clockwise
#
# Cards on table positions
# Card's top left conner area w = 27, h = 54
# 1 - 277, 245
# 2 - 357, 245
# 3 - 436, 245
# 4 - 516, 245
# 5 - 596, 245

width_ref = 850
height_ref = 615

class Rectangle:
    def __init__(self, x, y, width, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def to_box(self, ratio: tuple[float, float] = (1.0, 1.0)) -> tuple[float, float, float, float]:
        return self.x/ratio[0], self.y/ratio[1], (self.x + self.width)/ratio[0], (self.y + self.height)/ratio[1]

class Player:
    def __init__(self, pos, btn:Rectangle, cards: tuple[Rectangle, Rectangle], back: tuple[Rectangle, Rectangle], bb: Rectangle):
        self.pos: Rectangle = pos
        self.btn: Rectangle = btn
        self.cards: tuple[Rectangle, Rectangle] = cards
        self.back: tuple[Rectangle, Rectangle] = back
        self.bb: Rectangle = bb

A = (
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 0, 0, 0, 0), Rectangle( 0, 0, 0, 0)), bb= Rectangle(10, 126, 102, 24)),    # table for 0 players
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 0, 0, 0, 0), Rectangle( 0, 0, 0, 0)), bb= Rectangle(10, 126, 102, 24)),    # table for 1 player
    Player(pos=Rectangle( 365, 431, 120, 150), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 0, 0, 0, 0), Rectangle( 0, 0, 0, 0)), bb= Rectangle(10, 126, 102, 24)),    # table for 2 players
    Player(pos=Rectangle( 365, 431, 120, 150), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 0, 0, 0, 0), Rectangle( 0, 0, 0, 0)), bb= Rectangle(10, 126, 102, 24)),    # table for 3 players
    Player(pos=Rectangle( 365, 431, 120, 150), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 0, 0, 0, 0), Rectangle( 0, 0, 0, 0)), bb= Rectangle(10, 126, 102, 24)),    # table for 4 players
    Player(pos=Rectangle( 365, 431, 120, 150), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 0, 0, 0, 0), Rectangle( 0, 0, 0, 0)), bb= Rectangle(10, 126, 102, 24)),    # table for 5 players
    Player(pos=Rectangle( 365, 431, 120, 150), btn=Rectangle(362,430,5,5), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 0, 0, 0, 0), Rectangle( 0, 0, 0, 0)), bb= Rectangle(10, 126, 102, 24)),    # table for 6 players
    Player(pos=Rectangle( 365, 431, 120, 150), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 0, 0, 0, 0), Rectangle( 0, 0, 0, 0)), bb= Rectangle(10, 126, 102, 24)),    # table for 7 players
    Player(pos=Rectangle( 365, 431, 120, 150), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 0, 0, 0, 0), Rectangle( 0, 0, 0, 0)), bb= Rectangle(10, 126, 102, 24)),    # table for 8 players
    Player(pos=Rectangle( 365, 431, 120, 150), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 0, 0, 0, 0), Rectangle( 0, 0, 0, 0)), bb= Rectangle(10, 126, 102, 24)),    # table for 9 players
)
B = (
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 0 players
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 1 player
    Player(pos=Rectangle(   0,   0, 109, 131), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 2 players
    Player(pos=Rectangle(   0,   0, 109, 131), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 3 players
    Player(pos=Rectangle(   0,   0, 109, 131), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 4 players
    Player(pos=Rectangle(   0,   0, 109, 131), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 5 players
    Player(pos=Rectangle(  39, 348, 109, 131), btn=Rectangle(181,413,5,5), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 6 players
    Player(pos=Rectangle( 114, 370, 109, 131), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 7 players
    Player(pos=Rectangle( 124, 371, 109, 131), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 8 players
    Player(pos=Rectangle(   0,   0, 109, 131), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 9 players
)
C = (
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 0 players
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 1 player
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 2 players
    Player(pos=Rectangle(   0,   0, 109, 131), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 3 players
    Player(pos=Rectangle(   0,   0, 109, 131), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 4 players
    Player(pos=Rectangle(   0,   0, 109, 131), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 5 players
    Player(pos=Rectangle(  65, 101, 109, 131), btn=Rectangle(182,214,5,5), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 6 players
    Player(pos=Rectangle(  38, 166, 109, 131), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 7 players
    Player(pos=Rectangle(  14, 216, 109, 131), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 8 players
    Player(pos=Rectangle(   0,   0, 109, 131), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 9 players
)
D = (
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 0 players
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 1 player
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 2 players
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 3 players
    Player(pos=Rectangle(   0,   0, 109, 131), btn=Rectangle(  0,  0,5,5), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 4 players
    Player(pos=Rectangle(   0,   0, 109, 131), btn=Rectangle(  0,  0,5,5), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 5 players
    Player(pos=Rectangle( 371,  41, 109, 131), btn=Rectangle(379,180,5,5), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 6 players
    Player(pos=Rectangle( 259,  64, 109, 131), btn=Rectangle(  0,  0,5,5), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 7 players
    Player(pos=Rectangle( 144,  74, 109, 131), btn=Rectangle(  0,  0,5,5), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 8 players
    Player(pos=Rectangle(   0,   0, 109, 131), btn=Rectangle(  0,  0,5,5), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 9 players
)
E = (
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 0 players
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 1 player
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 2 players
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 3 players
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 4 players
    Player(pos=Rectangle(   0,   0, 109, 131), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 5 players
    Player(pos=Rectangle( 676, 101, 109, 131), btn=Rectangle(650,214,5,5), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 6 players
    Player(pos=Rectangle( 483,  64, 109, 131), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 7 players
    Player(pos=Rectangle( 370,  41, 109, 131), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 8 players
    Player(pos=Rectangle(   0,   0, 109, 131), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 9 players
)
F = (
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 0 players
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 1 player
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 2 players
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 3 players
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 4 players
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 5 players
    Player(pos=Rectangle( 703, 348, 109, 131), btn=Rectangle(651,413,5,5), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 6 players
    Player(pos=Rectangle( 704, 166, 109, 131), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 7 players
    Player(pos=Rectangle( 607,  74, 109, 131), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 8 players
    Player(pos=Rectangle(   0,   0, 109, 131), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 9 players
)
G = (
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 0 players
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 1 player
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 2 players
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 3 players
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 4 players
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 5 players
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 6 players
    Player(pos=Rectangle( 629, 370, 109, 131), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 7 players
    Player(pos=Rectangle( 728, 216, 109, 131), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 8 players
    Player(pos=Rectangle(   0,   0, 109, 131), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 9 players
)
H = (
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 0 players
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 1 player
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 2 players
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 3 players
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 4 players
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 5 players
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 6 players
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 7 players
    Player(pos=Rectangle( 617, 371, 109, 131), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 8 players
    Player(pos=Rectangle(   0,   0, 109, 131), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 9 players
)
I = (
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 0 players
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 1 player
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 2 players
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 3 players
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 4 players
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 5 players
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 6 players
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 7 players
    Player(pos=Rectangle(   0,   0,   0,   0), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 8 players
    Player(pos=Rectangle( 683, 371, 109, 131), btn=Rectangle(  0,  0,0,0), cards=(Rectangle( 0, 0, 0, 0),Rectangle( 0, 0, 0, 0)), back=(Rectangle( 30, 30, 5, 5), Rectangle( 80, 30, 5, 5)), bb= Rectangle(8, 104, 92, 21)),    # table for 9 players
)

players = (A, B, C, D, E, F, G, H, I)

table_cards = (
        (251, 257, 22, 22),
        (323, 257, 22, 22),
        (395, 257, 22, 22),
        (467, 257, 22, 22),
        (539, 257, 22, 22)
)

