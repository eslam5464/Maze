import pygame
import drawings
import data
import methods

pygame.init()
window_w, window_h = data.window_w, data.window_h
game_name = data.game_name
folder_location = data.folder_location

screen = pygame.display.set_mode((window_w, window_h))
background = pygame.Surface((window_w, window_h))

data.initialize()
drawings.draw_all(screen)
pygame.display.flip()

while True:
    # drawings.draw_all(screen)

    for event in pygame.event.get():
        keys = pygame.key.get_pressed()

        if(keys[pygame.K_ESCAPE]):
            pygame.quit()
            exit(0)

        if (keys[pygame.K_w] and keys[pygame.K_a]):
            key_name = "wa"
            if(data.player["body_angle"] != 135):
                data.player["body_angle"] = 135

        elif (keys[pygame.K_w] and keys[pygame.K_d]):
            key_name = "wd"
            if(data.player["body_angle"] != 45):
                data.player["body_angle"] = 45

        elif (keys[pygame.K_a] and keys[pygame.K_s]):
            key_name = "as"
            if(data.player["body_angle"] != 225):
                data.player["body_angle"] = 225

        elif (keys[pygame.K_d] and keys[pygame.K_s]):
            key_name = "ds"
            if(data.player["body_angle"] != 315):
                data.player["body_angle"] = 315

        elif (keys[pygame.K_w]):
            key_name = "w"
            if(data.player["body_angle"] != 90):
                data.player["body_angle"] = 90

        elif (keys[pygame.K_s]):
            key_name = "s"
            if(data.player["body_angle"] != 270):
                data.player["body_angle"] = 270

        elif (keys[pygame.K_a]):
            key_name = "a"
            if(data.player["body_angle"] != 180):
                data.player["body_angle"] = 180

        elif (keys[pygame.K_d]):
            key_name = "d"
            if(data.player["body_angle"] != 0):
                data.player["body_angle"] = 0

        else:
            key_name = ""

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    methods.check_key(key_name, (window_w, window_h))

    if(data.player["body_rect"].colliderect(data.objects["barrelGreen_side1"][1])):
        print(data.player["body_rect"].y,
              data.player["body_rect"].x, "collision")

    drawings.draw_all(screen)
    pygame.display.flip()
