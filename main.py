import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1000, 800)) #flags=pygame.NOFRAME)
pygame.display.set_caption("Tanks")
icon = pygame.image.load("images/vehicle_16003491.png")
pygame.display.set_icon(icon)

bg = pygame.image.load("images/texture_1000x800.jpg").convert()
font = pygame.font.Font("fonts/RobotoCondensed-Medium.ttf", 48)
mouse = pygame.mouse.get_pos()

btn_play = pygame.Rect(400, 300, 200, 60)
btn_quit = pygame.Rect(400, 400, 200, 60)
#PLAYER
player_right = pygame.image.load("images/player/player_right.png").convert_alpha()
player_left = pygame.image.load("images/player/player_left.png").convert_alpha()
player_up = pygame.image.load("images/player/player_up.png").convert_alpha()
player_down = pygame.image.load("images/player/player_down.png").convert_alpha()

player_shot_list = []

player = player_right

player_speed = 1.6
player_x = 150
player_y = 358.5

#ENEMY
enemy_up = pygame.image.load("images/enemy/enemy_up.png").convert_alpha()
enemy_down = pygame.image.load("images/enemy/enemy_down.png").convert_alpha()
enemy_right = pygame.image.load("images/enemy/enemy_right.png").convert_alpha()
enemy_left = pygame.image.load("images/enemy/enemy_left.png").convert_alpha()

enemy_shot_list = []

enemy = enemy_left

enemy_speed = 1.6
enemy_x = 800
enemy_y = 358.5

#SHELLS
shell_player_right= pygame.image.load("images/shells/shell_player_right.png").convert_alpha()
shell_player_left = pygame.image.load("images/shells/shell_player_left.png").convert_alpha()
shell_player_up = pygame.image.load("images/shells/shell_player_up.png").convert_alpha()
shell_player_down = pygame.image.load("images/shells/shell_player_down.png").convert_alpha()

shell_player_count = 500

shell_player = shell_player_right

shell_enemy_right = pygame.image.load("images/shells/shell_enemy_right.png").convert_alpha()
shell_enemy_left = pygame.image.load("images/shells/shell_enemy_left.png").convert_alpha()
shell_enemy_up = pygame.image.load("images/shells/shell_enemy_up.png").convert_alpha()
shell_enemy_down = pygame.image.load("images/shells/shell_enemy_down.png").convert_alpha()

shell_enemy_count = 500

shell_enemy = shell_enemy_right

gameplay = False
running = False
running1 = True
inter = False

win_label_blue = font.render("Синий победил", True, (0, 4, 255))
win_label_red = font.render("Красный победил", True, (255, 0, 0))
restart_label = font.render("Играть заново", True, (255, 255, 255))

# ТЕКСТ КНОПОК
text_play = font.render("Играть", True, (255, 255, 255))
text_quit = font.render("Выйти", True, (255, 255, 255))

text_play_rect = text_play.get_rect(center=btn_play.center)
text_quit_rect = text_quit.get_rect(center=btn_quit.center)

# ГЛАВНОЕ МЕНЮ
while running1:

    mouse = pygame.mouse.get_pos()

    screen.fill((51, 51, 51))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running1 = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if btn_play.collidepoint(event.pos):
                inter = True
                gameplay = True
                running = True
                running1 = False

            elif btn_quit.collidepoint(event.pos):
                running1 = False

    #КНОПКА ИГРАТЬ
    if btn_play.collidepoint(mouse):
        pygame.draw.rect(screen, (100, 100, 100), btn_play)
    else:
        pygame.draw.rect(screen, (65, 65, 65), btn_play)

    pygame.draw.rect(screen, (255, 255, 255), btn_play, 2)
    screen.blit(text_play, text_play_rect)

    #КНОПКА ВЫЙТИ
    if btn_quit.collidepoint(mouse):
        pygame.draw.rect(screen, (100, 100, 100), btn_quit)
    else:
        pygame.draw.rect(screen, (65, 65, 65), btn_quit)

    pygame.draw.rect(screen, (255, 255, 255), btn_quit, 2)
    screen.blit(text_quit, text_quit_rect)

    pygame.display.flip()
    clock.tick(60)

while running:

    if inter:
        if gameplay:
            screen.blit(bg, (0, 0))
            keys = pygame.key.get_pressed()

            #ПОВОРОТЫ СПРАЙТОВ СИНЕГО
            if keys[pygame.K_d]:
                shell_player = shell_player_right
                player = player_right
            elif keys[pygame.K_a]:
                shell_player = shell_player_left
                player = player_left
            elif keys[pygame.K_w]:
                shell_player = shell_player_up
                player = player_up
            elif keys[pygame.K_s]:
                shell_player = shell_player_down
                player = player_down

            #ДВИЖЕНИЕ СИНЕГО
            if keys[pygame.K_a] and player_x > 0:
                player_x -= player_speed
            elif keys[pygame.K_d] and player_x < 930:
                player_x += player_speed
            elif keys[pygame.K_w] and player_y > 0:
                player_y -= player_speed
            elif keys[pygame.K_s] and player_y < 800:
                player_y += player_speed

            #ПОВОРОТЫ СПРАЙТОВ КРАСНОГО
            if keys[pygame.K_l]:
                shell_enemy = shell_enemy_right
                enemy = enemy_right
            elif keys[pygame.K_j]:
                shell_enemy = shell_enemy_left
                enemy = enemy_left
            elif keys[pygame.K_i]:
                shell_enemy = shell_enemy_up
                enemy = enemy_up
            elif keys[pygame.K_k]:
                shell_enemy = shell_enemy_down
                enemy = enemy_down

            #ДВИЖЕНИЕ КРАСНОГО
            if keys[pygame.K_j] and enemy_x > 0:
                enemy_x -= enemy_speed
            elif keys[pygame.K_l] and enemy_x < 930:
                enemy_x += enemy_speed
            elif keys[pygame.K_i] and enemy_y > 0:
                enemy_y -= enemy_speed
            elif keys[pygame.K_k] and enemy_y < 800:
                enemy_y += enemy_speed

            #КОЛЛИЗИЯ ИГРОКОВ
            player_rect = player.get_rect(topleft=(player_x, player_y))
            enemy_rect = enemy.get_rect(topleft=(enemy_x, enemy_y))

            #СТРЕЛЬБА СИНЕГО
            if player_shot_list:
                for (i, shot) in enumerate(player_shot_list):
                    screen.blit(shell_player, (shot.x, shot.y))
                    if shot.x > 1000 or shot.x < 0 or shot.y > 800 or shot.y < 0:
                        player_shot_list.pop(i)

                    if shell_player == shell_player_right:
                        shot.x += 30
                    elif shell_player == shell_player_left:
                        shot.x -= 30
                    elif shell_player == shell_player_up:
                        shot.y -= 30
                    elif shell_player == shell_player_down:
                        shot.y += 30

                    if shot.colliderect(enemy_rect):
                        player_shot_list.pop(i)
                        gameplay = False

            #СТРЕЛЬБА КРАСНОГО
            if enemy_shot_list:
                for (i, shot) in enumerate(enemy_shot_list):
                    screen.blit(shell_enemy, (shot.x, shot.y))
                    if shot.x > 1000 or shot.x < 0 or shot.y > 800 or shot.y < 0:
                        enemy_shot_list.pop(i)

                    if shell_enemy == shell_enemy_right:
                        shot.x += 30
                    elif shell_enemy == shell_enemy_left:
                        shot.x -= 30
                    elif shell_enemy == shell_enemy_up:
                        shot.y -= 30
                    elif shell_enemy == shell_enemy_down:
                        shot.y += 30

                    if shot.colliderect(player_rect):
                        enemy_shot_list.pop(i)
                        gameplay = False

            #ОТРИСОВКА ИГРОКОВ
            screen.blit(player, (player_x, player_y))
            screen.blit(enemy, (enemy_x, enemy_y))

        else:
            screen.fill("Gray")



    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        #УПРАВЛЕНИЕ СИНЕГО
        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_SPACE and shell_player_count > 0:
            if player == player_left:
                player_shot_list.append(shell_player_left.get_rect(topleft=(player_x - 20, player_y + 30)))
            elif player == player_right:
                player_shot_list.append(shell_player_right.get_rect(topleft=(player_x + 82, player_y + 30)))
            elif player == player_up:
                player_shot_list.append(shell_player_up.get_rect(topleft=(player_x + 30, player_y - 20)))
            elif player == player_down:
                player_shot_list.append(shell_player_down.get_rect(topleft=(player_x + 30, player_y + 83)))
            shell_player_count -= 1

        #УПРАВЛЕНИЕ КРАСНОГО
        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_n and shell_enemy_count > 0:
            if enemy == enemy_left:
                enemy_shot_list.append(shell_enemy_left.get_rect(topleft=(enemy_x - 20, enemy_y + 30)))
            elif enemy == enemy_right:
                enemy_shot_list.append(shell_enemy_right.get_rect(topleft=(enemy_x + 82, enemy_y + 30)))
            elif enemy == enemy_up:
                enemy_shot_list.append(shell_enemy_up.get_rect(topleft=(enemy_x + 30, enemy_y - 20)))
            elif enemy == enemy_down:
                enemy_shot_list.append(shell_enemy_down.get_rect(topleft=(enemy_x + 30, enemy_y + 83)))
            shell_enemy_count -= 1

    clock.tick(60)