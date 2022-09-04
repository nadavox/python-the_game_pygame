import pygame
import random
import sys


def draw_floor():
    screen.blit(FLOOR_SURFACE, (flor_x_pos, 900))
    screen.blit(FLOOR_SURFACE, (flor_x_pos + 576, 900))


def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_new_pipe = pipe_surface.get_rect(midtop=(600, random_pipe_pos))
    top_new_pipe = pipe_surface.get_rect(midbottom=(600, random_pipe_pos - 300))
    return bottom_new_pipe, top_new_pipe


def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 3
    return pipes


def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 1024:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False,
                                              True)  # flip the surface when (x direction, y direction)
            screen.blit(flip_pipe, pipe)


def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            death_sound.play()
            return False

    if bird_rect.top <= -100 or bird_rect.bottom >= 900:
        death_sound.play()
        return False

    return True


def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -bird_movement * 4, 1)
    return new_bird


def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center=(100, bird_rect.centery))
    return new_bird, new_bird_rect


def score_display(game_mode):
    if game_mode == "main_game":
        score_surface = game_font.render(str(int(score)), True, (0, 0, 255))
        score_rect = score_surface.get_rect(center=(288, 100))  # make rectangle so it easy to move it
        if score >= 0:
            screen.blit(score_surface, score_rect)
    else:
        score_surface = game_font.render("Your score: " + str(int(score)), True, (0, 0, 255))
        score_rect = score_surface.get_rect(center=(288, 870))  # make rectangle so it easy to move it
        if score >= 0:
            screen.blit(score_surface, score_rect)
        High_score()


def High_score():
    High_score_surface = highscore_font.render("high score: " + str(int(high_score)), True, (0, 0, 255))
    highscore_rect = High_score_surface.get_rect(center=(300, 50))
    screen.blit(High_score_surface, highscore_rect)


def Update_Score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score


def Draw_menu(game_over):
    if not game_over:
        menue_surface = pygame.transform.scale2x(pygame.image.load('assets/message.png'))
        manue_rect = menue_surface.get_rect(center=(300, 512))
        screen.blit(menue_surface, manue_rect)
    else:
        Show_surface_game_over()


def Show_Game_Over(pipe_list):  # tell me if the game is over
    if not check_collision(pipe_list):
        return True  # it means game over
    else:
        return False


def Show_surface_game_over():
    To_restart = To_restart_font.render("press space to play", True, (255, 255, 255))
    To_restart_rect = To_restart.get_rect(center=(300, 500))
    game_over_surface = pygame.transform.scale2x(pygame.image.load('assets/gameover.png').convert_alpha())
    game_over_surface_rect = game_over_surface.get_rect(center=(300, 300))
    screen.blit(game_over_surface, game_over_surface_rect)
    screen.blit(To_restart, To_restart_rect)


# pygame.mixer.pre_init(frequency = 44100, size = 16, channels = 1, buffer = 512) #intiat mixer to play music in time
pygame.init()
screen = pygame.display.set_mode((576, 1024))  # made the screen of the game
clock = pygame.time.Clock()  # varible to choose how many frames per second my game will run
game_font = pygame.font.Font('assets/04B_19.TTF', 50)
highscore_font = pygame.font.Font('assets/04B_19.TTF', 40)
To_restart_font = pygame.font.Font('assets/04B_19.TTF', 50)

# gmae variables
gravity = 0.25
bird_movement = 0
game_active = False
score = -1.05
high_score = 0
score_sound_countdown = 300
game_over = False

bg_surface = pygame.image.load(
    'assets/background-day.png').convert()  # varible for background_surface, convert is to help the game to run more easliy
bg_surface = pygame.transform.scale2x(bg_surface)  # to increase the back ground multiple 2

FLOOR_SURFACE = pygame.image.load('assets/base.png').convert()
FLOOR_SURFACE = pygame.transform.scale2x(FLOOR_SURFACE)
flor_x_pos = 0

bird_downflap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-downflap.png').convert_alpha())
bird_midflap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-midflap.png').convert_alpha())
bird_upflap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-upflap.png').convert_alpha())
bird_frames = [bird_downflap, bird_midflap, bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center=(100, 512))

BIRDFLAP = pygame.USEREVENT + 1  # IT HAS TO BE +1 TO CREATE ANOTHER EVENT.
pygame.time.set_timer(BIRDFLAP, 200)

# bird_surface = pygame.image.load('assets/bluebird-midflap.png').convert_alpha() #image of the bird
# bird_surface = pygame.transform.scale2x(bird_surface) # make it twice in the size
# bird_rect = bird_surface.get_rect(center = (100 , 512)) # put rectangle around the surface

pipe_surface = pygame.image.load('assets/pipe-green.png')
pipe_surface = pygame.transform.scale2x(pipe_surface)  # make it twice in the size
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)  # event that occur every 1.2 sec
pipe_height = [400, 600, 800]

flap_sound = pygame.mixer.Sound('assets/sfx_wing.wav')
death_sound = pygame.mixer.Sound('assets/sfx_hit.wav')
score_sound = pygame.mixer.Sound('assets/sfx_point.wav')

while True:  # the game loop
    for event in pygame.event.get():  # every thing i do in the window of the game
        if event.type == pygame.QUIT:  # specific event when i want to close the game
            pygame.quit()  # close the window of the game
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 9
                flap_sound.play()
            if event.key == pygame.K_SPACE and game_active == False and game_over == False:
                game_active = True
                game_over = False
                pipe_list.clear()
                bird_rect.center = (100, 512)
                bird_movement = 0
                high_score = Update_Score(score, high_score)
                score = -1
                score_sound_countdown = 300
            if event.key == pygame.K_SPACE and game_active == False:
                game_over = False
                Draw_menu(game_over)

        if event.type == BIRDFLAP:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0

            bird_surface, bird_rect = bird_animation()

        if event.type == SPAWNPIPE:
            pipe_list.extend(
                create_pipe())  # make a new pipe and insert to a list of pipe bt a function call create pipe)

    screen.blit(bg_surface, (0, 0))  # put one surface on another surface by (x,y)
    High_score()
    if game_active:  # if the game is runing with score
        # bird
        bird_movement += gravity
        rotated_bird = rotate_bird(bird_surface)
        bird_rect.centery += bird_movement
        screen.blit(rotated_bird, bird_rect)
        game_active = check_collision(pipe_list)
        game_over = Show_Game_Over(pipe_list)

        # pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

        # score
        score += 0.0055
        high_score = Update_Score(score, high_score)
        score_display("main_game")
        score_sound_countdown -= 1
        if score_sound_countdown <= 0:
            score_sound.play()
            score_sound_countdown = 230
    else:
        Draw_menu(game_over)
        score_display("game_over")

    # floor
    flor_x_pos -= 1
    draw_floor()  ## a function that draw another floor on the right to make the movement infinity
    if flor_x_pos <= -576:
        flor_x_pos = 0
    screen.blit(FLOOR_SURFACE, (flor_x_pos, 900))
    pygame.display.update()  # draw and update on the canvas whatever I wrote in the loop
    clock.tick(144)  # limit my frames per second
pygame.quit()
