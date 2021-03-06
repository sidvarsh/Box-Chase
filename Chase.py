import random
import pygame

WIDTH = 500
HEIGHT = 500

alien = Actor('alien')
alien.pos = (400, 50)
box = Rect((20, 20), (100, 100))
score = 0

def draw():
    screen.clear()
    screen.draw.filled_rect(box, 'red')
    alien.draw()

def update():
    global score
    if keyboard.right:
        alien.x = alien.x + 2
    elif keyboard.left:
        alien.x = alien.x - 2
    elif keyboard.up:
        alien.y = alien.y - 2
    elif keyboard.down:
        alien.y = alien.y + 2
    if alien.colliderect(box):
        box.x = random.randint(0, WIDTH)
        box.y = random.randint(0, HEIGHT)
        score = score + 1
        print("Score:",score)

    if keyboard.f:
        pygame.display.set_mode((WIDTH,HEIGHT), pygame.FULLSCREEN)
    if keyboard.escape:
        exit()
