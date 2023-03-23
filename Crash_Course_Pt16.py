'''
Bubble Sort Visualizer
'''
import pygame
pygame.init()
window = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Bubble Sort Visualizer')

x = 40
y = 40

width = 20
height = [200, 50, 130, 90, 230, 62, 112, 88, 33, 83, 70, 158, 181, 20]

def show(height):
  for i in range(len(height)):
    pygame.draw.rect(window, (255, 255, 255), ( x + 30 * i, y, width, height[i]))


while True:
  execute = False
  pygame.time.delay(10)
  keys = pygame.key.get_pressed()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()

  if keys[pygame.K_SPACE]:
    execute = True

  if execute == False:
    window.fill((0, 0, 0))
    show(height)
    pygame.display.flip()
  else:
    for i in range(len(height) - 1):
      for j in range(len(height) - i - 1):
        if height[j] > height[j + 1]:
          height[j], height[j + 1] = height[j + 1], height[j]

        window.fill((0, 0, 0))
        show(height)
        pygame.time.delay(50)
        pygame.display.update()


