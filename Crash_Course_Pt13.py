'''
Creating Interactive Buttons
'''
import pygame
pygame.init()
window = pygame.display.set_mode((720, 720))
pygame.display.set_caption('Interactive Button Creation')

# Set button's color
color = (255, 255, 255)
color_button_light = (170, 170, 170)
color_button_dark = (100, 100, 100)

# Get the width and height of the window
width = window.get_width()
height = window.get_height()

# Set button's font
button_font = pygame.font.SysFont('Corbel', 35)
text = button_font.render('Bye Bye', True, color)


while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()

  # Listening for mouse click within the box area
  if event.type == pygame.MOUSEBUTTONDOWN:
    if width/2 <= mouse[0] <= width/2 + 140 and height/2 <= mouse[1] <= height/2 + 140:
      pygame.quit()

  window.fill((60, 25, 60))
  mouse = pygame.mouse.get_pos()

  # While mouse hovering over the button and change color
  if width/2 <= mouse[0] <= width/2 + 140 and height/2 <= mouse[1] <= height/2 + 140:
    pygame.draw.rect(window, color_button_light, [width/2, height/2, 140, 140])
  else:
    pygame.draw.rect(window, color_button_dark, [width/2, height/2, 140, 140])

  window.blit(text, (width/2, height/2))

  pygame.display.update()
