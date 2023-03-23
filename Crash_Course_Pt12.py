'''
Moving Object around a Confined Window
'''
import pygame
pygame.init()
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Moving Object')

# Object's Position
x = 200
y = 250

# Object's Dimension
width = 30
height = 40

v = 7

playing = True

while playing:
  pygame.time.delay(10)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      playing = False

  keys = pygame.key.get_pressed()

  if keys[pygame.K_LEFT] and x > 0:
    x -= v
  if keys[pygame.K_RIGHT] and x < 500 - width:
    x += v
  if keys[pygame.K_UP] and y > 0:
    y -= v
  if keys[pygame.K_DOWN] and y < 500 - height:
    y += v


  window.fill((0, 0, 0))

  pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))

  pygame.display.update()

pygame.quit()