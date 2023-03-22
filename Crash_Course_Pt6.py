'''
Image insertion
'''
import pygame

pygame.init()
window = pygame.display.set_mode((450, 450))

image = pygame.image.load('images/pink_cosmos_flowers.jpg')


playing = True

while playing:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      playing = False

  window.fill((255, 255, 255))
  window.blit(image, (0, 0))

  pygame.display.update()



pygame.quit()