import pygame

win_config = {
    "wight": 500,
    "height": 500,
    "background": (0, 0, 0),
    "padding": 5
}

pygame.init()
win = pygame.display.set_mode((win_config["wight"], win_config["height"]))

pygame.display.set_caption("Genshin Impact")


walk_right = [
    pygame.image.load('sprites/right_1.png'),
    pygame.image.load('sprites/right_2.png'),
    pygame.image.load('sprites/right_3.png'),
    pygame.image.load('sprites/right_4.png'),
    pygame.image.load('sprites/right_5.png'),
    pygame.image.load('sprites/right_6.png'),
]

walk_left = [
    pygame.image.load('sprites/left_1.png'),
    pygame.image.load('sprites/left_2.png'),
    pygame.image.load('sprites/left_3.png'),
    pygame.image.load('sprites/left_4.png'),
    pygame.image.load('sprites/left_5.png'),
    pygame.image.load('sprites/left_6.png'),
]

background = pygame.image.load('sprites/background.jpg')

player_stand = pygame.image.load('sprites/idle.png')

clock = pygame.time.Clock()

player_x = 50
player_y = 419
player_widht = 60
player_height = 71
player_speed = 5
player_color = (255, 195, 249)


is_jump = False
jump_count = 10


move_left = False
move_right = False
animation_count = 0

def draw_window():
    global animation_count
    win.blit(background, (0, 0))

    if animation_count + 1 >= 30:
        animation_count = 0

    if move_left:
        win.blit(walk_left[animation_count // 5], (player_x, player_y))
        animation_count += 1
    elif move_right:
        win.blit(walk_right[animation_count // 5], (player_x, player_y))
        animation_count += 1
    else:
        win.blit(player_stand, (player_x, player_y))
    
    pygame.display.update()


run = True
while run:
    clock.tick(30)

    for eva_event in pygame.event.get():
        if eva_event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > win_config["padding"]:
        player_x -= player_speed
        move_left = True
        move_right = False
    elif keys[pygame.K_RIGHT] and player_x < win_config["wight"] - player_widht - win_config["padding"]:
        player_x += player_speed
        move_right = True
        move_left = False
    else:
        move_left = False
        move_right = False
        animation_count = 0
    if not(is_jump):
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -10:
            if jump_count < 0:
                player_y += (jump_count ** 2) / 2
            else:
                player_y -= (jump_count ** 2) / 2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10

    draw_window()  
pygame.quit()