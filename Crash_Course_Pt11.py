'''
Playing Audio File
'''
from pygame import mixer

mixer.init()
mixer.music.load('musics/Future-Technology.mp3')
mixer.music.set_volume(0.8)
mixer.music.play()

while True:
  print("Press 'p' to pause the Audio")
  print("Press 'r' to resume the Audio")
  print("Press 'e' to exit the program")

  entry = input("")

  if entry == 'p':
    mixer.music.pause()
  elif entry == 'r':
    mixer.music.unpause()
  elif entry == 'e':
    mixer.music.stop()
    break