import data


def get_color(name):
    name = name.lower()
    colors = {"white": (255, 255, 255),
              "black": (0, 0, 0),
              "red": (255, 0, 0),
              "green": (0, 255, 0),
              "blue": (0, 0, 255),
              "brown": (150, 75, 0),
              "background": (172, 159, 171)}
    return colors[name]


def draw_chars(screen):
    from pygame import transform, sprite
    player_body = transform.rotate(
        data.player["body"], data.player["body_angle"])

    screen.blit(player_body,
                (data.player["posX"], data.player["posY"]))


def draw_background(screen):
    screen.fill(get_color("red"))


def draw_objects(screen):
    from pygame import Rect, draw
    screen.blit(data.objects["barrelGreen_side1"][0], (data.objects["barrelGreen_side1"][1].x,data.objects["barrelGreen_side1"][1].y))


def draw_all(screen):
    draw_background(screen)
    draw_chars(screen)
    draw_objects(screen)
