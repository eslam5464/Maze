from pygame import image, display

window_w, window_h = 800, 600
movement_speed = 0.0003

game_name = "maze"
folder_location = "C:/Users/eslam/Documents/VC code" + "/" + game_name + "/"

# resources = {
#     "grass1": image.load("resources/terrain/tileGrass1.png"),
#     "grass2": image.load("resources/terrain/tileGrass2.png"),
#     "projectile_laser": image.load("resources/terrain/laser_small.png")
# }

characters = {
    "characterWhite1": image.load(folder_location + "resources/characters/White/characterWhite (1).png")
}

background = {
    "green1": image.load(folder_location + "resources/background/green1.png")
}

player = {
    "body": characters["characterWhite1"],
    "body_rect": characters["characterWhite1"].get_rect(),
    "posX": characters["characterWhite1"].get_rect().x,
    "posY": characters["characterWhite1"].get_rect().y,
    "body_size": characters["characterWhite1"].get_rect().size,
    "body_angle": 0
}

objects = {
    "box1": [image.load(folder_location + "resources/terrain/barrelBlack_side.png"), image.load(folder_location + "resources/terrain/barrelBlack_side.png").get_rect()],

    "barrelGreen_side1": [image.load(folder_location + "resources/terrain/barrelGreen_side.png"), image.load(folder_location + "resources/terrain/barrelGreen_side.png").get_rect()]
}


def initialize():
    player["body_rect"].x = player["posX"] = 0.5 * window_w
    player["body_rect"].y = player["posY"] = 0.5 * window_h
    objects["barrelGreen_side1"][1].x = 0.4 * window_w
    objects["barrelGreen_side1"][1].y = 0.5 * window_h
