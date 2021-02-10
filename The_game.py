import pygame, sys, random
from pygame.math import Vector2


class ENEMY(pygame.sprite.Sprite):
    def __init__(self, image = pygame.image.load('assets/bluebird-midflap.png'), boos = False, move_to_left = True):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(780, random.randint(20, 780)))
        self.boos = boos
        self.move_to_left = move_to_left

    def return_rect_enemy(self):
        return self.rect

    def draw_enemy(self):
        screen.blit(self.image, self.rect)

    def moving_enemy_by_level(self, levels):
        global game_on, score
        if self.move_to_left:
            if self.boos:
                self.rect.x = self.rect.x - 1
            if levels >= 1 and levels < 20:
                self.rect.x -= 1
            elif levels >= 20 and levels < 30:
                self.rect.x -= 2
        else:
            if self.boos:
                self.rect.x = self.rect.x + 1
            if levels >= 1 and levels < 20:
                self.rect.x += 1
            elif levels >= 20 and levels < 30:
                self.rect.x += 2


        if self.rect.midleft[0] <= 1:
            self.move_to_left = False
        elif  self.rect.midright[0] >= 799:
            self.move_to_left = True


    def get_rect(self):
        return self.rect


class SPACE_SHIP:
    def __init__(self):
        # self.spaceship = pygame.transform.flip(pygame.image.load('assets/bluebird-upflap.png'), True, False)
        self.spaceship = pygame.image.load('assets/head_right.png').convert_alpha()
        # self.rect_spaceship = self.spaceship.get_rect(center=(100, 100))
        self.rect_spaceship = Vector2(400,400)
        self.vector_move = Vector2(0,0)
        self.vector_dirction = Vector2(0,0)
        self.dirction_of_the_space = 'right'
        self.rect = self.spaceship.get_rect(midleft = (self.rect_spaceship))

    def draw(self):
        screen.blit(self.spaceship, self.rect_spaceship)


    def update_rect(self):
        self.rect = self.spaceship.get_rect(midleft = (self.rect_spaceship) + (0,11))


    def update(self):
        self.rect_spaceship = self.rect_spaceship + self.vector_move
        self.update_rect()


    def move_spaceship(self, key):
        if key == 'right':
            #move right
            self.vector_dirction = Vector2(1,0)
            self.vector_move = Vector2(8,0)
            self.spaceship = pygame.image.load('assets/head_right.png').convert_alpha()
            self.dirction_of_the_space = 'right'
        if key == 'left':
            # move left
            self.vector_dirction = Vector2(-1, 0)
            self.vector_move = Vector2(-8,0)
            self.spaceship = pygame.transform.flip(pygame.image.load('assets/head_right.png').convert_alpha(), True, False)
            self.dirction_of_the_space = 'left'
        if key == 'down':
            # move down
            if self.dirction_of_the_space == 'right':
                self.vector_dirction = Vector2(1, 0)
                self.vector_move = Vector2(0,8)
            elif self.dirction_of_the_space =='left':
                self.vector_dirction = Vector2(-8, 0)
                self.vector_move = Vector2(0, 8)
            else:
                self.vector_move = Vector2(0, 8)

        if key == 'up':
            # move up
            if self.dirction_of_the_space == 'right':
                self.vector_dirction = Vector2(1, 0)
                self.vector_move = Vector2(0, -8)
            elif self.dirction_of_the_space =='left':
                self.vector_dirction = Vector2(-1, 0)
                self.vector_move = Vector2(0, -8)
            else:
                self.vector_move = Vector2(0, -8)

    def get_vector_move_direction_x(self):
        return self.vector_dirction.x


    def get_vector_move_direction_y(self):
        return self.vector_dirction.y


    def bounce_spacehip(self): # need to fix this
        # print(self.rect.x)
        if self.rect.x == 800:
            self.vector_dirction = Vector2(-10, 0)
        if self.rect.midleft[0] == 0:
            self.vector_dirction = Vector2(10, 0)


class BULLET(pygame.sprite.Sprite):
    def __init__(self, width, hegiht, pos_x, pos_y, color, diriction):
        super().__init__()
        self.image = pygame.Surface([width,hegiht])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.diriction = diriction
        if self.diriction == 'right':
            self.rect.midleft = [pos_x + 50, pos_y + 8]
        if self.diriction == 'left':
            self.rect.center = [pos_x - 20, pos_y + 8]

    def update(self):
        if self.diriction == 'right':
            self.rect.x += 5
        if self.diriction == 'left':
            self.rect.x -= 5
    # def get_diriction(self):
    #     return self.diriction

    # def get_rect(self):
    #     return self.rect


class COIN:
    def __init__(self, collect  = False, SuperPower = False,):
        self.SuperPower = SuperPower
        self.position = (random.randint(10, 780) , random.randint(20, 780))
        if self.SuperPower:
            self.coin = pygame.image.load('assets/body_tl.png').convert_alpha()
            self.rect_coin = self.coin.get_rect(center=(self.position))
            # list_of_powers = [2, 2, 2]   if I want to add more powers
            # self.choose_power_random = random.choice(list_of_powers)
            # if self.choose_power_random == 1:  # the ability to live for 5 sec
            #     self.coin = pygame.image.load('assets/body_tl.png').convert_alpha()
            #     self.rect_coin = self.coin.get_rect(center=(self.position))
            # if self.choose_power_random == 2:  # one more live
            #     self.coin = pygame.image.load('assets/body_tl.png').convert_alpha()
            #     self.rect_coin = self.coin.get_rect(center=(self.position))
            # if self.choose_power_random == 3:  # kill all the enemies
            #     self.coin = pygame.image.load('assets/body_tl.png').convert_alpha()
            #     self.rect_coin = self.coin.get_rect(center=(self.position))
        else:
            self.coin = pygame.image.load('assets/coin.png').convert_alpha()
        self.rect_coin = self.coin.get_rect(center = (self.position))
        self.collect = collect

    def draw(self):
         self.rect_coin = self.coin.get_rect(center=(self.position))
         screen.blit(self.coin, self.rect_coin)


    def collect_or_not(self):
        global lives
        if not self.collect:
            self.collect = True
        if self.collect:
            self.position = (random.randint(10, 380), random.randint(20, 270))
            if self.SuperPower:
                lives += 1


def draw_background():
    bg_surface = pygame.transform.scale(pygame.image.load('assets/background.png').convert_alpha(), (1600,1000))
    screen.blit(bg_surface, (0, 0))


def Moving_enemy(enemy_group):
    for enemy_spirit in enemy_group:
        enemy_spirit.moving_enemy_by_level(level)


def SHOW_BOSS(level, bullet_group):
    global hits_until_elimnation_boss, show_boss, score
    if level >= 2 and show_boss and hits_until_elimnation_boss > 0:
        BOSS_ENEMY.draw_enemy()
        rect_boss = BOSS_ENEMY.get_rect()
        BOSS_ENEMY.moving_enemy_by_level(level)
        for bullets in bullet_group:
            if rect_boss.topleft[0] - 1 <= bullets.rect.x <= rect_boss.topright[0] + 2 and\
                    rect_boss.bottom + 2 >= bullets.rect.y >= rect_boss.top - 2:
                bullets.kill()
                hits_until_elimnation_boss -= 1
        if hits_until_elimnation_boss <= 0:
            show_boss = False
            score += 1


    # print(show_boss)
    # print(hits_until_elimnation_boss)
    #     hit_boss = SHOW_BOOS(level, bullet_group)
    #     if hit_boss:
    #         hits_until_elimnation_boss -= 1
    #     if hits_until_elimnation_boss == 0:
    #         show_boss = False
    #         hits_until_elimnation_boss = 30
    #
    #
    # if hits_until_elimnation_boss > 0 :
    #     BOSS_ENEMY.draw_enemy()
    #     rect_boss = BOSS_ENEMY.get_rect()
    #     BOSS_ENEMY.moving_enemy(level)
    #     for bullets in bullet_group:
    #         if rect_boss.topleft[0] - 1 <= bullets.rect.x <= rect_boss.topright[0] + 2 and\
    #                 rect_boss.bottom + 2 >= bullets.rect.y >= rect_boss.top - 2:
    #             bullets.kill()
    #             return 1
    #     return 0


def coin_collect(coin, spaceship):
    #---
    #with the limits of the rect i can know if they collide with each other
    # |||
    coin.draw()
    #pygame.draw.rect(screen, (0,255,255), coin.rect_coin)
    #pygame.draw.rect(screen, (255,0,0), spaceship.rect_spacehip_Collide)
    if coin.rect_coin.topleft[0] <= spaceship.rect.centerx <= coin.rect_coin.topright[0] and \
        coin.rect_coin.bottom - spaceship.rect.top == 0:
        coin.collect_or_not()
        return 1

    elif coin.rect_coin.topleft[0] <= spaceship.rect.midright[0] <= coin.rect_coin.topright[0] and \
         coin.rect_coin.topleft[1] <= spaceship.rect.midright[1] <= coin.rect_coin.bottomleft[1]:
        coin.collect_or_not()
        return 1

    elif coin.rect_coin.topleft[0]  <= spaceship.rect.midleft[0] <= coin.rect_coin.topright[0] and\
        coin.rect_coin.topright[1] <= spaceship.rect.midleft[1] <= coin.rect_coin.bottomright[1]:
        coin.collect_or_not()
        return 1

    elif coin.rect_coin.topleft[0] <= spaceship.rect.centerx <= coin.rect_coin.topright[0] and \
         coin.rect_coin.top - spaceship.rect.bottom == 0:
        coin.collect_or_not()
        return 1

    else:
        return 0


def kill_enemy():
    #pygame.draw.circle(screen, (200,0,0), (20,20), 10) (screen, pos on the screen, radios)
    #first of all the first for move on all the sprite in each enemy in the group of enemy and moving each enemy
    # the second for run over all the bullet sprite in bullet group and check if there is collide between enemy_sprite
    # and enemy_group if there is a collide between emmey sprite and bullet spirit
    # delete both of them
    # than add to the level and the score
    global level, enemy_group, bullet_group, score
    for enemy_spirit in enemy_group:
        enemy_spirit.moving_enemy_by_level(level)
        for bullet_spirit in bullet_group:
            # if bullet_spirit.rect.x > 400:
            #     bullet_spirit.rect.x = 0
            # elif  bullet_spirit.rect.x < 0:
            #     bullet_spirit.rect.x = 400
            if bullet_spirit.rect.midleft[0] <= 0:
                bullet_spirit.rect.centerx = 4
                bullet_spirit.diriction = 'right'
            if bullet_spirit.rect.midright[0] >= 799:
                bullet_spirit.diriction = 'left'
            collide_bullet = bullet_spirit.rect.colliderect(enemy_spirit.get_rect())
            if collide_bullet == 1:
                bullet_spirit.kill()
                enemy_spirit.kill()
                score += 1
                level += 0.1
                # print(level)


def show_score(score):
    score_text = pygame.font.Font(None, 50)
    score_surface = score_text.render("score: " + str(int(score)), True, (0,0,255))
    score_rect = score_surface.get_rect(center=(400, 20))
    screen.blit(score_surface, score_rect)

def show_game_over_screen(score, win_the_game = False):
    score_text = pygame.font.Font(None, 70)
    score_surface = score_text.render("your score is: " + str(int(score)), True, (0,0,255))
    score_rect = score_surface.get_rect(center=(400, 280))
    screen.blit(score_surface, score_rect)
    if win_the_game:
        game_win_text = pygame.font.Font(None, 70)
        game_win_surface = game_win_text.render("you win", True, (255, 0, 0))
        game_win_rect = game_win_surface.get_rect(center=(400, 340))
        screen.blit(game_win_surface, game_win_rect)
    else:
        game_over_text = pygame.font.Font(None, 70)
        game_over_surface = game_over_text.render("game over ", True, (255, 0, 0))
        game_over_rect = game_over_surface.get_rect(center=(400, 340))
        screen.blit(game_over_surface, game_over_rect)

    game_over_restart = pygame.font.Font(None, 70)
    game_over_restart_surface = game_over_restart.render("press enter to restart ", True, (0, 0, 0))
    game_over_restart_rect = game_over_restart_surface.get_rect(center=(400, 400))
    screen.blit(game_over_restart_surface, game_over_restart_rect)


def collide_spaceship(spaceship, enemy_group, bullet_group, boss_enemy):
    global lives
    #enemy that hit the spaceship
    for enemy in enemy_group:
        if enemy.rect.topleft[0] <= spaceship.rect.centerx <= enemy.rect.topright[0] and \
            enemy.rect.bottom - spaceship.rect.top == 0:
            if lives > 0:
                enemy.kill()
                lives -= 1
                return True
            else:
                return False
        elif enemy.rect.topleft[0] <= spaceship.rect.midright[0] <= enemy.rect.topright[0] and \
            enemy.rect.topleft[1] <= spaceship.rect.midright[1] <= enemy.rect.bottomleft[1]:
            if lives > 0:
                enemy.kill()
                lives -= 1
                return True
            else:
                return False
        elif enemy.rect.topleft[0] <= spaceship.rect.midleft[0] <= enemy.rect.topright[0] and \
            enemy.rect.topright[1] <= spaceship.rect.midleft[1] <= enemy.rect.bottomright[1]:
            if lives > 0:
                enemy.kill()
                lives -= 1
                return True
            else:
                return False
        elif enemy.rect.topleft[0] <= spaceship.rect.centerx <= enemy.rect.topright[0] and \
            enemy.rect.bottom - spaceship.rect.top == 0:
            if lives > 0:
                enemy.kill()
                lives -= 1
                return True
            else:
                return False

    #bullets that hit the spaceship
    for bullet in bullet_group:
        end_game = bullet.rect.colliderect(spaceship.rect)
        if end_game == 1:
            if lives > 0:
                bullet.kill()
                lives -= 1
                return True
            else:
                return False

    # boss enemy kil the spaceship
    if boss_enemy.rect.topleft[0] <= spaceship.rect.centerx <= boss_enemy.rect.topright[0] and \
            boss_enemy.rect.bottom - spaceship.rect.top == 0:
            return False
    elif boss_enemy.rect.topleft[0] <= spaceship.rect.midright[0] <= boss_enemy.rect.topright[0] and \
            boss_enemy.rect.topleft[1] <= spaceship.rect.midright[1] <= boss_enemy.rect.bottomleft[1]:
            return False
    elif boss_enemy.rect.topleft[0] <= spaceship.rect.midleft[0] <= boss_enemy.rect.topright[0] and \
            boss_enemy.rect.topright[1] <= spaceship.rect.midleft[1] <= boss_enemy.rect.bottomright[1]:
            return False
    elif boss_enemy.rect.topleft[0] <= spaceship.rect.centerx <= boss_enemy.rect.topright[0] and \
            boss_enemy.rect.bottom - spaceship.rect.top == 0:
            return False

    # limtis for the spaceship
    if spaceship.rect.midright[0] <= 0:
        return False
    if spaceship.rect.midleft[0] >= 800:
        return False
    if spaceship.rect.bottom <= -0:
        return False
    if spaceship.rect.top >= 800:
        return False

    return True


def draw_super_coin(super_coin):
    global take_super_coin, time_until_super_coin_disappear
    if take_super_coin == "no":
        super_coin.draw()
        if coin_collect(super_coin, spaceship):
            take_super_coin = "yes"


def draw_lives(lives):
    lives_text = pygame.font.Font(None, 40)
    lives_surface = lives_text.render(str(int(lives) + 1) + " lives", True, (0, 0, 255))
    lives_rect = lives_surface.get_rect(midleft=(50, 20))
    screen.blit(lives_surface, lives_rect)




pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 2000)
x_pos = 0
y_pos = 300
FLOOR_SURFACE = pygame.image.load('assets/base.png').convert_alpha() # we nneed to make function
first_time = -1
bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
enemy_list_rect = []
index_of_enemy = -1
spaceship  = SPACE_SHIP()
k_up = False # if the key up is press
k_down = False # if the key down is press
k_left = False # if the key left is press
k_right = False # if the key right is press
level = 1 # every 10 hits the leve go up by 1.
Hit_or_not = 0
BOSS_ENEMY = ENEMY(pygame.transform.scale2x(pygame.transform.flip(pygame.image.load('assets/bluebird-midflap.png').convert_alpha(),True,False)), True)
hits_until_elimnation_boss = 30
coin = COIN()
create_new_boss = pygame.USEREVENT + 1
pygame.time.set_timer(create_new_boss, 20000) # need to change more  sec
show_boss = True
FPS = 100
score = 0

game_on = True
run = True
create_new_supercoin = pygame.USEREVENT + 2
pygame.time.set_timer(create_new_supercoin, 20000)
take_super_coin = "yes"
super_coin = COIN(SuperPower=True)

time_until_super_coin_disappear = pygame.USEREVENT + 3
pygame.time.set_timer(time_until_super_coin_disappear, 10000)
count_until_the_first_super_coin = 0
lives = 0


while run: # the game loop
    draw_background()
    for event in pygame.event.get(): # every thing i do in the window of the game
        if event.type == pygame.QUIT: # specific event when i want to close the game
            pygame.quit() # close the window of the game
            sys.exit()
        if event.type == SPAWNPIPE:
            enemy = ENEMY()
            enemy_group.add(enemy)
        if event.type == time_until_super_coin_disappear and game_on:
            count_until_the_first_super_coin += 1
            if count_until_the_first_super_coin % 2 != 0:
                take_super_coin = "yes" # to vanish him after 10 sec.
        if event.type == create_new_supercoin and game_on:
            super_coin = COIN(SuperPower=True)
            take_super_coin = "no"
        if event.type == create_new_boss and game_on:
            show_boss = True
            if hits_until_elimnation_boss == 0:
                hits_until_elimnation_boss = 30
                BOSS_ENEMY = ENEMY(pygame.transform.scale2x(
                    pygame.transform.flip(pygame.image.load('assets/bluebird-midflap.png').convert_alpha(), True, False)), True)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if spaceship.get_vector_move_direction_x() == 1:
                    #move right
                    bullet = BULLET(10, 10, spaceship.rect_spaceship.x, spaceship.rect_spaceship.y, (0, 0, 255), 'right')
                    bullet_group.add(bullet)

                if spaceship.get_vector_move_direction_x() == -1:
                    # move left
                    bullet = BULLET(10, 10, spaceship.rect_spaceship.x, spaceship.rect_spaceship.y, (255, 0, 0), 'left')
                    bullet_group.add(bullet)


            if event.key == pygame.K_UP: k_up = True
            if event.key == pygame.K_DOWN: k_down = True
            if event.key == pygame.K_RIGHT:  k_right = True
            if event.key == pygame.K_LEFT:  k_left = True




        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP: k_up = False
            if event.key == pygame.K_DOWN: k_down = False
            if event.key == pygame.K_RIGHT: k_right = False
            if event.key == pygame.K_LEFT: k_left = False
            spaceship.vector_move = Vector2(0,0)

        if event.type == pygame.KEYDOWN and game_on == False:
            if event.key == pygame.K_RETURN :
                BOSS_ENEMY = ENEMY(pygame.transform.scale2x(
                    pygame.transform.flip(pygame.image.load('assets/bluebird-midflap.png').convert_alpha(), True,
                                          False)), True)
                enemy_group.empty()
                bullet_group.empty()
                coin.position = (random.randint(10, 780) , random.randint(20, 780))
                spaceship.rect_spaceship = Vector2(400,400)
                spaceship.vector_move = Vector2(0, 0)
                score = 0
                level = 1
                hits_until_elimnation_boss = 30
                game_on = True
                lives = 0




    if game_on and level < 30:
        if k_up:
            spaceship.move_spaceship("up")
        if k_down:
            spaceship.move_spaceship("down")
        if k_right:
            spaceship.move_spaceship("right")
        if k_left:
            spaceship.move_spaceship("left")

        enemy_group.draw(screen)
        enemy_group.update()
        bullet_group.draw(screen)
        bullet_group.update()
        spaceship.update()
        spaceship.draw()
        spaceship.bounce_spacehip()
        if coin_collect(coin, spaceship):
            score += 1
        kill_enemy()
        SHOW_BOSS(level, bullet_group )
        show_score(score)
        game_on = collide_spaceship(spaceship, enemy_group, bullet_group , BOSS_ENEMY)
        Moving_enemy(enemy_group)
        draw_super_coin(super_coin)
        draw_lives(lives)

    elif not game_on and level < 30:
        show_game_over_screen(score)
    if level >= 30:
        game_on = False
        show_game_over_screen(score, win_the_game = True)


    # print(FPS)
    # print('the level is: '+str(int(level)))
    if FPS < 144:
        FPS += 0.05
    clock.tick(FPS)
    pygame.display.update() # update the surface