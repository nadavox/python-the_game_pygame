import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.new_block = False

        self.head_up = pygame.image.load('assets/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('assets/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('assets/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('assets/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('assets/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('assets/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('assets/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('assets/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('assets/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('assets/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('assets/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('assets/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('assets/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('assets/body_bl.png').convert_alpha()
        self.crunch_sound = pygame.mixer.Sound('assets/crunch.wav')
    def draw_snake(self):
            self.update_head_graphics()
            self.update_tail_graphics()
            for index, block in enumerate(self.body):
                x_pos = int(block.x * cell_size)
                y_pos = int(block.y * cell_size)
                block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

                if index == 0:
                    screen.blit(self.head ,block_rect)
                elif index == len(self.body) - 1:
                    screen.blit(self.tail, block_rect)
                else:
                    previous_block = self.body[index + 1] -block
                    next_block  = self.body[index - 1] - block
                    if previous_block.x == next_block.x:
                        screen.blit(self.body_vertical, block_rect)
                    elif previous_block.y == next_block.y:
                        screen.blit(self.body_horizontal, block_rect)
                    else:
                        if previous_block.x == -1 and next_block.y ==-1 or previous_block.y == -1 and next_block.x ==-1:
                            screen.blit(self.body_tl, block_rect)
                        if previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1  and next_block.x == -1:
                            screen.blit(self.body_bl, block_rect)
                        if  previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                            screen.blit(self.body_tr, block_rect)
                        if previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                            screen.blit(self.body_br, block_rect)


                # else:
                #     pygame.draw.rect(screen, (150,100,100), block_rect)

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0): self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1): self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1): self.tail = self.tail_down


    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1,0): self.head = self.head_right
        elif head_relation == Vector2(0, 1): self.head = self.head_up
        elif head_relation == Vector2(0, -1): self.head = self.head_down


    def play_crunch_sound(self):
        self.crunch_sound.play()


    def move_snake(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)

class Fruit:
    def __init__(self):
        self.randomize()

    def draw_a_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size), cell_size, cell_size)
        #pygame.draw.rect(screen, (126,166,114), fruit_rect)
        screen.blit(apple, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = Fruit()

    def Update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
    def draw_element(self):
        self.draw_grass()
        self.fruit.draw_a_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()

        for block in self.snake.body[1:0]:
            if block == self.fruit.pos:
                self.fruit.randomize()


    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not  0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if self.snake.body[0] == block:
                self.game_over()

    def game_over(self):
        self.snake.reset()

    def draw_grass(self):
        grass_color = (107,200,0)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 ==0:
                        grass_rect = pygame.Rect(col * cell_size , row * cell_size , cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)


    def draw_score(self):
        score_text = "  " + str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (0,0,0))
        score_x = int(cell_size* cell_number -60)
        score_y = int(30)
        score_rect = score_surface.get_rect(center = (score_x , score_y))
        apple_rect = apple.get_rect(midright = (score_rect.centerx -5, score_rect.centery))
        bg_rect2 = pygame.Rect(apple_rect.left - 1, apple_rect.top , apple_rect.width + score_rect.width + 5,
                              apple_rect.height )
        screen.blit(score_surface, score_rect)
        screen.blit(apple, apple_rect)
        pygame.draw.rect(screen, (0, 0, 0), bg_rect2, 2)

pygame.init()
cell_size = 40
cell_number = 20
Framerate = 55
BGcolor = (130,140,40)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)



screen = pygame.display.set_mode((cell_number * cell_size ,cell_number * cell_size))
clock = pygame.time.Clock()

apple = pygame.image.load('assets/bluebird-midflap.png').convert_alpha()
Snake = SNAKE()
fruit = Fruit()
game_font = pygame.font.Font('assets/stay home.otf', 25)
main_gmae = MAIN()

while True:
    for event in  pygame.event.get(): #loop that happens every event in the game like push keyboard, exit, mouse.
        if event.type == pygame.QUIT: # if we click on the exit bottom it close the game
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_gmae.Update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_gmae.snake.direction.y != 1:
                    main_gmae.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                if main_gmae.snake.direction.y != -1:
                    main_gmae.snake.direction = Vector2(0,1)
            if event.key == pygame.K_RIGHT:
                if main_gmae.snake.direction.x != -1:
                    main_gmae.snake.direction = Vector2(1,0)
            if event.key == pygame.K_LEFT:
                if main_gmae.snake.direction.x != 1:
                    main_gmae.snake.direction = Vector2(-1,0)
    screen.fill(BGcolor)
    main_gmae.draw_element()
    pygame.display.update() #update all the things i do in the game
    clock.tick(Framerate) # limit my framerate