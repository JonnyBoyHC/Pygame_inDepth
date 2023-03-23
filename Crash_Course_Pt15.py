'''
Creating Snow Particles
'''
import pygame
import random
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

window_size = [400, 400]
window =pygame.display.set_mode(window_size)

pygame.display.set_caption('Snow Particles Display')

snow_Particles = []

for i in range(200):
  x = random.randrange(0, 400)
  y = random.randrange(0, 400)

  snow_Particles.append([x, y])

clock = pygame.time.Clock()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()

  window.fill(black)

  for i in range(len(snow_Particles)):
    pygame.draw.circle(window, white, snow_Particles[i], 2)
    snow_Particles[i][1] += 1
    if snow_Particles[i][1] > 400:
      y = random.randrange(-50, -10)
      snow_Particles[i][1] = y
      x = random.randrange(0, 400)
      snow_Particles[i][0] = x

  pygame.display.flip()
  clock.tick(20)
