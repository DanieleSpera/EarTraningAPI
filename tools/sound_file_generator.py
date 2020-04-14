import os
import sys
import numpy as np
from scipy.io import wavfile

import app_settings

class sound_generator():

   def __init__(self):

      #app settings
      self.audio_dir = app_settings.audio_dir
      self.sample_rate = app_settings.sample_rate

      #class settings
      self.selected_root = ""
      self.path_note = self.audio_dir + self.selected_root +'.mp3'
      self.note_dict = {
         'C' :32,
         'C#':34,
         'D' :36,
         'D#':38,
         'E' :41,
         'F' :43,
         'F#':46,
         'G' :49,
         'G#':52,
         'A' :55,
         'A#':58,
         'B' :61,
      }

   def get_sound_url(self,note):

      self.selected_root = note.replace("sharp","#")
      path_note = self.path_note = self.audio_dir +self.selected_root+'.mp3'

      if(not os.path.exists(path_note)):
         soundwave = self.generate_note(self.note_dict.get(self.selected_root))
         self.generate_file(soundwave,self.selected_root)
         os.remove(self.audio_dir+self.selected_root+'.wav')
      return (path_note)

   def generate_note(self,frequency):
      #wave settings
      sample_rate = self.sample_rate
      length = 1

      t = np.linspace(0, length, sample_rate * length)
      y = np.sin(frequency * 2 * np.pi * t)

      return y

   def get_frequency_note(self,base_frequency,octave):
      frequency = base_frequency
      for freq in range(octave):
         frequency = frequency * 2
      return frequency

   def generate_file(self,soundwave,name):
      wav_path = self.audio_dir +name+'.wav'

      wavfile.write(wav_path, self.sample_rate,soundwave)

      mp3_path = self.audio_dir +name+'.mp3'

      rate,data = wavfile.read(wav_path)
      shifted = data * (2 **31-1)
      ints = shifted.astype(np.int32)

      command =  "ffmpeg -i "+wav_path+" -vn -ar 44100  -ac 2 -b:a 192k "+mp3_path

      os.system(command)      