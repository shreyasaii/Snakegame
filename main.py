import pygame
import random

# Initialize Pygame
pygame.init()
pygame.mixer.init()  # Initialize Pygame mixer

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Display settings
dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Aparna')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

# Font settings
font_path = "PressStart2P.ttf"
font_style_large = pygame.font.Font(font_path, 35)
font_style_medium = pygame.font.Font(font_path, 20)
font_style_small = pygame.font.Font(font_path, 20)
score_font = pygame.font.Font(font_path, 20)

# Load background images
start_bg = pygame.image.load('1.jpg')
start_bg = pygame.transform.scale(start_bg, (dis_width, dis_height))

game_bg = pygame.image.load('2.jpg')
game_bg = pygame.transform.scale(game_bg, (dis_width, dis_height))

# Load background music
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)  # Play music continuously

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color, y_displacement=0, font=font_style_large):
    mesg = font.render(msg, True, color)
    mesg_rect = mesg.get_rect(center=(dis_width / 2, dis_height / 2 + y_displacement))
    dis.blit(mesg, mesg_rect)

def gameLoop():
    global snake_speed  # Use global to modify snake_speed
    
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.blit(game_bg, (0, 0))
            your_score(Length_of_snake - 1, y_displacement=-50, font=font_style_small, center=True)
            message("Try Again!", red)
            message("Press Q-Quit or C-Play Again", red, 50, font=font_style_medium)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.blit(game_bg, (0, 0))
        pygame.draw.circle(dis, green, (int(foodx) + snake_block // 2, int(foody) + snake_block // 2), snake_block // 2)
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        your_score(Length_of_snake - 1)

        # Increase snake speed after score reaches 10
        if Length_of_snake > 10:
            snake_speed = 20  # Adjust speed as needed

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

def your_score(score, y_displacement=0, font=score_font, center=False):
    value = font.render("Your Score: " + str(score), True, white)
    if center:
        value_rect = value.get_rect(center=(dis_width / 2, dis_height / 2 + y_displacement))
    else:
        value_rect = value.get_rect(topleft=(0, y_displacement))
    dis.blit(value, value_rect)

def start_game():
    start = True
    while start:
        dis.blit(start_bg, (0, 0))
        message("Start Game", white)
        message("Press Enter to play!", white, 50, font=font_style_medium)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start = False

start_game()
gameLoop()
