import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1000, 800)) #flags=pygame.NOFRAME)
pygame.display.set_caption("Tanks")
icon = pygame.image.load("images/vehicle_16003491.png")
pygame.display.set_icon(icon)

bg = pygame.image.load("images/texture_1000x800.jpg").convert()

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

gameplay = True

running = True
while running:

    screen.blit(bg, (0, 0))

    if gameplay:

        keys = pygame.key.get_pressed()
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

        if keys[pygame.K_a] and player_x > 0:
            player_x -= player_speed
        elif keys[pygame.K_d] and player_x < 930:
            player_x += player_speed
        elif keys[pygame.K_w] and player_y > 0:
            player_y -= player_speed
        elif keys[pygame.K_s] and player_y < 800:
            player_y += player_speed

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

        if keys[pygame.K_j] and enemy_x > 0:
            enemy_x -= enemy_speed
        elif keys[pygame.K_l] and enemy_x < 930:
            enemy_x += enemy_speed
        elif keys[pygame.K_i] and enemy_y > 0:
            enemy_y -= enemy_speed
        elif keys[pygame.K_k] and enemy_y < 800:
            enemy_y += enemy_speed

        player_rect = player.get_rect(topleft=(player_x, player_y))
        enemy_rect = enemy.get_rect(topleft=(enemy_x, enemy_y))

        if player_shot_list:
            for (i, shot) in enumerate(player_shot_list):
                screen.blit(shell_player, (shot.x, shot.y))
                if shot.x > 1000 or shot.x < 0 or shot.y > 800 or shot.y < 0:
                    player_shot_list.pop(i)

                if shell_player == shell_player_right:
                    shot.x += 50
                elif shell_player == shell_player_left:
                    shot.x -= 50
                elif shell_player == shell_player_up:
                    shot.y -= 50
                elif shell_player == shell_player_down:
                    shot.y += 50

                if shot.colliderect(enemy_rect):
                    player_shot_list.pop(i)

        if enemy_shot_list:
            for (i, shot) in enumerate(enemy_shot_list):
                screen.blit(shell_enemy, (shot.x, shot.y))
                if shot.x > 1000 or shot.x < 0 or shot.y > 800 or shot.y < 0:
                    enemy_shot_list.pop(i)

                if shell_enemy == shell_enemy_right:
                    shot.x += 50
                elif shell_enemy == shell_enemy_left:
                    shot.x -= 50
                elif shell_enemy == shell_enemy_up:
                    shot.y -= 50
                elif shell_enemy == shell_enemy_down:
                    shot.y += 50

                if shot.colliderect(player_rect):
                    enemy_shot_list.pop(i)

        screen.blit(player, (player_x, player_y))
        screen.blit(enemy, (enemy_x, enemy_y))

        #if enemy_rect.colliderect(shell_player_rect):
        #    gameplay = False
    else:
        screen.fill("Blue")

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
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