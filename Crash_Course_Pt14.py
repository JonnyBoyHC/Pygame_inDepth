'''
Adding Boundaries to an Object
'''
import pygame
import random
pygame.init()

width = 700
height = 550

window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Adding Boundaries to an Object')

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

ball_x = width/2 - 12
ball_y = height/2 - 12
ball_xMove = 0.1 * random.choice((1, -1))
ball_yMove = 0.1

ball_pixel = 25

while True:
  window.fill(red)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()

  if ball_x <= 0 or ball_x + ball_pixel >= width:
    ball_xMove *= -1
  if ball_y <= 0 or ball_y + ball_pixel >= height:
    ball_yMove *= -1

  ball_x += ball_xMove
  ball_y += ball_yMove

  ballImg = pygame.draw.circle(window, (0, 0, 255), (ball_x, ball_y), 15)

  pygame.display.update()
