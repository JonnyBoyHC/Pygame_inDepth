'''
Keyboard Input Listening
'''
import pygame
pygame.init()
window = pygame.display.set_mode((850, 850))

done = False
is_blue = True

x = 30
y = 30

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
      is_blue = not is_blue

  pressed = pygame.key.get_pressed()
  if pressed[pygame.K_UP]: y -= 3
  if pressed[pygame.K_DOWN]: y += 3
  if pressed[pygame.K_LEFT]: x -= 3
  if pressed[pygame.K_RIGHT]: x += 3

  if is_blue:
    color = (0, 128, 255)
  else:
    color = (255, 100, 0)

  pygame.draw.rect(window, color, pygame.Rect(x, y, 60, 60))

  pygame.display.flip()




# playing = True

# while playing:
#   event = pygame.event.wait()
#   if event. type == pygame. QUIT:
#     break
#   if event. type in (pygame. KEYDOWN, pygame. KEYUP):
#     key_name = pygame. key. name (event. key)
#     key_name = key_name. upper()
#     if event. type == pygame.KEYDOWN:
#       print (u"{} Key Pressed".format(key_name))
#     elif event. type == pygame.KEYUP:
#       print (u"{} Key Released".format(key_name))

pygame.quit()