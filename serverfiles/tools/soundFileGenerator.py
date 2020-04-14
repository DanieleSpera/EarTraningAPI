import os
import sys
import numpy as np
from scipy.io import wavfile

class sound_generator():

   def __init__(self):
      self.settings = {'audio_dir':'/var/www/MusicApp/app/audio_files'}

   def get_sound_url(self):
      return "hello Bagel!"
