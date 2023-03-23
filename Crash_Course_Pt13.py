'''
Creating Interactive Buttons
'''
import pygame
pygame.init()
window = pygame.display.set_mode((720, 720))
pygame.display.set_caption('Interactive Button Creation')

color_button_light



while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      playing = False

  keys = pygame.key.get_pressed()




  window.fill((0, 0, 0))


  pygame.display.update()

pygame.quit()