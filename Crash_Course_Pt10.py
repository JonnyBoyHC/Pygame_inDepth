'''
How to Make an Object Jump
'''
import pygame
pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Jumping Tutorial')

# Object's Position
x = 200
y = 200

# Object's Dimension
width = 30
height = 40

# Setting mass and velocity
m = 1
v = 5

# Object is Static
jumping = False

playing = True

while playing:
  window.fill((255, 255, 255))

  pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      playing = False

  keys = pygame.key.get_pressed()

  if jumping == False:
    if keys[pygame.K_SPACE]:
      jumping  = True

  if jumping:
    F = (1/2)*m*(v**2)
    y -= F

    v -= 1

    if v < 0:
      m = -1
    if v == -6:
      jumping = False
      m = 1
      v = 5

  pygame.time.delay(10)

  pygame.display.update()

pygame.quit()