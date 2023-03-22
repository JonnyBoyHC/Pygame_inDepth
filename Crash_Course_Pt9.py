'''
Draw a few different shapes
'''
import pygame
pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 128, 0)
black = (0, 0, 0)
red = (255, 0, 0)

window = pygame.display.set_mode((450, 450))
pygame.display.set_caption('Drawing Shapes')
window.fill(white)
pygame.draw.polygon(window, blue, [(146, 0), (291, 106), (236, 277), (56, 277), (0, 106)])
pygame.draw.line(window, green, (65, 350), (120, 350), 4)
pygame.draw.circle(window, black, (300, 50), 20, 0)
pygame.draw.ellipse(window, red, (300, 250, 40, 80), 1)
pygame.draw.rect(window, green, (150, 300, 100, 50))



while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()

    pygame.display.update()

pygame.quit()