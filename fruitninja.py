import pygame
from pygame.locals import *
import sys
import random
from pygame import mixer

pygame.init()
clock = pygame.time.Clock()

lives = 3
score = 0
x = 480
y = 10

screen = pygame.display.set_mode((620, 320))
pygame.display.set_caption('FRUIT NINJA')
background = pygame.image.load('background3.png')



pomegranate = pygame.image.load('pomegranate.png')
pomegranate_rect = pomegranate.get_rect(topleft=[100, 200])

orange = pygame.image.load('orange.png')
orange_rect = orange.get_rect(topright=[200, 100])

melon = pygame.image.load('melon.png')
melon_rect = melon.get_rect(topleft=[300, 90])

guava = pygame.image.load('guava.png')
guava_rect = guava.get_rect(topleft=[400, 300])

bomb = pygame.image.load('bomb.png')
bomb_rect = bomb.get_rect(topright=[400, 160])

white_lives = pygame.image.load('white_lives.png')
white_lives_rect = white_lives.get_rect(topright=[480, 10])

red_lives = pygame.image.load('red_lives.png')
red_lives_rect = red_lives.get_rect(topright=[480, 10])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            if pomegranate_rect.collidepoint(pygame.mouse.get_pos()):
                pomegranate_Sound = mixer.Sound('slice.wav')
                pomegranate_Sound.play()
                pomegranate = pygame.image.load('half_pomegranate.png')
                score += 10
            if orange_rect.collidepoint(pygame.mouse.get_pos()):
                orange = pygame.image.load('half_orange.png')
                orange_Sound = mixer.Sound('slice.wav')
                orange_Sound.play()
                score += 10

            if melon_rect.collidepoint(pygame.mouse.get_pos()):
                melon = pygame.image.load('half_melon.png')
                melon_Sound = mixer.Sound('slice.wav')
                melon_Sound.play()
                score += 10

            if guava_rect.collidepoint(pygame.mouse.get_pos()):
                guava = pygame.image.load('half_guava.png')
                guava_Sound = mixer.Sound('slice.wav')
                guava_Sound.play()
                score += 10

            if bomb_rect.collidepoint(pygame.mouse.get_pos()):
                bomb_Sound = mixer.Sound('explosion.wav')
                bomb_Sound.play()
                bomb = pygame.image.load('explosion.png')
                lives -= 1

    screen.fill((255, 255, 255))
    screen.blit(background, [0, 0])

    font_style = pygame.font.SysFont("bahnschrift", 25)
    text = font_style.render("SCORE :" + str(score), True, (255, 255, 255))
    screen.blit(text, (0, 0))

    if lives != 0:

        if pomegranate_rect.y != 320:
            screen.blit(pomegranate, pomegranate_rect)
            pomegranate_rect.bottom += 5
        else:
            # pomegranate_rect.x = random.randint(100, 400)
            pomegranate = pygame.image.load('pomegranate.png')
            pomegranate_rect.x, pomegranate_rect.y = random.randint(200, 300), 90

        if orange_rect.y != 320:
            screen.blit(orange, orange_rect)
            orange_rect.bottom += 5
        else:
            # orange_rect.x = random.randint(100, 300)
            orange = pygame.image.load('orange.png')
            orange_rect.x, orange_rect.y = random.randint(100, 500), 40

        if melon_rect.y != 320:
            screen.blit(melon, melon_rect)
            melon_rect.bottom += 5
        else:
            # melon_rect.x = random.randint(80, 300)
            melon = pygame.image.load('melon.png')
            melon_rect.x, melon_rect.y = random.randint(80, 600), 80

        if guava_rect.y != 320:
            screen.blit(guava, guava_rect)
            guava_rect.bottom += 5
        else:
            # guava_rect.x = random.randint(100, 200)
            guava = pygame.image.load('guava.png')
            guava_rect.x, guava_rect.y = random.randint(10, 200), 60

        if bomb_rect.y != 320:
            screen.blit(bomb, bomb_rect)
            bomb_rect.bottom += 5
        else:
            # bomb_rect.x = random.randint(60,80)
            bomb = pygame.image.load('bomb.png')
            bomb_rect.x, bomb_rect.y = random.randint(60, 80), 60

    for i in range(lives):
        white_lives_rect.x = int(x + 50 * i)
        white_lives_rect.y = y
        screen.blit(white_lives, white_lives_rect)
        i += 1

    for j in range(3 - lives):
        red_lives_rect.x = int(x + 50 * i)
        red_lives_rect.y = y
        screen.blit(red_lives, red_lives_rect)
        i += 1

    if lives == 0:
        screen.fill((255, 255, 255))
        screen.blit(background, [0, 0])
        background = pygame.image.load('game_over1.png')
        mixer.music.load('gameover.wav')
        mixer.music.play()
        pygame.display.update()

    pygame.display.update()
    pygame.display.flip()
    clock.tick(25)