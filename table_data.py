# Data for players and cards locations on different tables
#
# Reference dimensions: w = 850, h = 615
#
# User player area w = 132, h  = 170
# Players positions and areas: w = 120, h = 146.
# Players positions: A, B, C, D, E, F, G, H. Position A is for user Player. All other positions clockwise
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

A = (
    (   0,   0,   0,   0),    # table for 0 players
    (   0,   0,   0,   0),    # table for 1 player
    ( 365, 431, 120, 150),    # table for 2 players
    ( 365, 431, 120, 150),    # table for 3 players
    ( 365, 431, 120, 150),    # table for 4 players
    ( 365, 431, 120, 150),    # table for 5 players
    ( 365, 431, 120, 150),    # table for 6 players
    ( 365, 431, 120, 150),    # table for 7 players
    ( 365, 431, 120, 150),    # table for 8 players
    ( 365, 431, 120, 150)     # table for 9 players
)
B = (
    (   0,   0,   0,   0),    # table for 0 players
    (   0,   0,   0,   0),    # table for 1 player
    (   0,   0, 109, 131),    # table for 2 players
    (   0,   0, 109, 131),    # table for 3 players
    (   0,   0, 109, 131),    # table for 4 players
    (   0,   0, 109, 131),    # table for 5 players
    (  39, 348, 109, 131),    # table for 6 players
    ( 114, 370, 109, 131),    # table for 7 players
    ( 124, 371, 109, 131),    # table for 8 players
    (   0,   0, 109, 131)     # table for 9 players
)
C = (
    (   0,   0,   0,   0),    # table for 0 players
    (   0,   0,   0,   0),    # table for 1 player
    (   0,   0,   0,   0),    # table for 2 players
    (   0,   0, 109, 131),    # table for 3 players
    (   0,   0, 109, 131),    # table for 4 players
    (   0,   0, 109, 131),    # table for 5 players
    (  65, 101, 109, 131),    # table for 6 players
    (  38, 166, 109, 131),    # table for 7 players
    (  14, 216, 109, 131),    # table for 8 players
    (   0,   0, 109, 131)     # table for 9 players
)
D = (
    (   0,   0,   0,   0),    # table for 0 players
    (   0,   0,   0,   0),    # table for 1 player
    (   0,   0,   0,   0),    # table for 2 players
    (   0,   0,   0,   0),    # table for 3 players
    (   0,   0, 109, 131),    # table for 4 players
    (   0,   0, 109, 131),    # table for 5 players
    ( 371,  41, 109, 131),    # table for 6 players
    ( 259,  64, 109, 131),    # table for 7 players
    ( 144,  74, 109, 131),    # table for 8 players
    (   0,   0, 109, 131)     # table for 9 players
)
E = (
    (   0,   0,   0,   0),    # table for 0 players
    (   0,   0,   0,   0),    # table for 1 player
    (   0,   0,   0,   0),    # table for 2 players
    (   0,   0,   0,   0),    # table for 3 players
    (   0,   0,   0,   0),    # table for 4 players
    (   0,   0, 109, 131),    # table for 5 players
    ( 676, 101, 109, 131),    # table for 6 players
    ( 483,  64, 109, 131),    # table for 7 players
    ( 370,  41, 109, 131),    # table for 8 players
    (   0,   0, 109, 131)     # table for 9 players
)
F = (
    (   0,   0,   0,   0),    # table for 0 players
    (   0,   0,   0,   0),    # table for 1 player
    (   0,   0,   0,   0),    # table for 2 players
    (   0,   0,   0,   0),    # table for 3 players
    (   0,   0,   0,   0),    # table for 4 players
    (   0,   0,   0,   0),    # table for 5 players
    ( 703, 348, 109, 131),    # table for 6 players
    ( 704, 166, 109, 131),    # table for 7 players
    ( 607,  74, 109, 131),    # table for 8 players
    (   0,   0, 109, 131)     # table for 9 players
)
G = (
    (   0,   0,   0,   0),    # table for 0 players
    (   0,   0,   0,   0),    # table for 1 player
    (   0,   0,   0,   0),    # table for 2 players
    (   0,   0,   0,   0),    # table for 3 players
    (   0,   0,   0,   0),    # table for 4 players
    (   0,   0,   0,   0),    # table for 5 players
    (   0,   0,   0,   0),    # table for 6 players
    ( 629, 370, 109, 131),    # table for 7 players
    ( 728, 216, 109, 131),    # table for 8 players
    (   0,   0, 109, 131)     # table for 9 players
)
H = (
    (   0,   0,   0,   0),    # table for 0 players
    (   0,   0,   0,   0),    # table for 1 player
    (   0,   0,   0,   0),    # table for 2 players
    (   0,   0,   0,   0),    # table for 3 players
    (   0,   0,   0,   0),    # table for 4 players
    (   0,   0,   0,   0),    # table for 5 players
    (   0,   0,   0,   0),    # table for 6 players
    (   0,   0,   0,   0),    # table for 7 players
    ( 617, 371, 109, 131),    # table for 8 players
    (   0,   0, 109, 131)     # table for 9 players
)
I = (
    (   0,   0,   0,   0),    # table for 0 players
    (   0,   0,   0,   0),    # table for 1 player
    (   0,   0,   0,   0),    # table for 2 players
    (   0,   0,   0,   0),    # table for 3 players
    (   0,   0,   0,   0),    # table for 4 players
    (   0,   0,   0,   0),    # table for 5 players
    (   0,   0,   0,   0),    # table for 6 players
    (   0,   0,   0,   0),    # table for 7 players
    (   0,   0,   0,   0),    # table for 8 players
    ( 683, 371, 109, 131)     # table for 9 players
)

players = (A, B, C, D, E, F, G, H, I)

cards = (
        (251, 257, 22, 22),
        (323, 257, 22, 22),
        (395, 257, 22, 22),
        (467, 257, 22, 22),
        (539, 257, 22, 22)
)

