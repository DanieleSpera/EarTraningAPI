""" Interval Generation Module """

import os
import numpy as np

import app_settings
from tools.note import Note
from tools.sound_file_generator import sound_generator


class Interval:

    def __init__(self):

        #app settings
        self.audio_dir = app_settings.audio_dir
        self.notes_list = app_settings.note_freq_dict
        self.intervals = app_settings.intervals

        #class settings
        self.note_1 = None
        self.note_2 = None
        self.selected_root = ""
        self.selected_interval = ""
        self.s_generator = sound_generator()
        
    def get_second_note_from_root(self, note_1, selected_interval):
        """Get the second note given the first
        in -> first note item [name, base frequency], note octave int, interval string
        out -> note item [name, base_freq]"""

        #Get Interval Distance
        interval_item = list(filter (lambda interval_itm: selected_interval in interval_itm[0] , self.intervals))[0]
        distance = interval_item[1]

        total_distance = note_1.scale_position + distance
        oct_difference = total_distance // (len(self.intervals)-1)

        note2_position = total_distance - ((len(self.intervals)-1) * oct_difference)
        note2_octave = note_1.octave + oct_difference

        note2_name = self.notes_list[note2_position][0][0]

        note_2 = Note()
        note_2.name = note2_name
        note_2.octave = note2_octave
        
        return note_2

    def get_interval_audio_url(self,root,selected_interval):

        self.selected_root = root.replace("sharp","#")
        self.selected_interval = selected_interval

        file_name = self.selected_root+"-"+self.selected_interval

        path_note = self.audio_dir +file_name+'.mp3'

        if(not os.path.exists(path_note)):
            soundwave = self.generate_interval_audio(self.selected_root,self.selected_interval)
            self.s_generator.generate_file(soundwave, file_name)
            os.remove(self.audio_dir+file_name+'.wav')

        return path_note

    def generate_interval_audio(self, root, selected_interval):

        self.note_1 = Note()
        self.note_1.name = root[:-1] #note name
        self.note_1.octave = int(root[-1])#note octave
        
        self.note_1.log_note_property()

        self.note_2 = self.get_second_note_from_root(self.note_1, selected_interval)

        self.note_2.log_note_property()

        interval_soundwave = self.generate_interval_soundwave()

        return interval_soundwave
        
    def generate_interval_soundwave(self):
        
        if None  in (self.note_1, self.note_1):
            raise Exception('Interval Notes are not defined')
        
        sound_wav_1 = self.s_generator.generate_note(self.note_1.frequency)
        sound_wav_2 = self.s_generator.generate_note(self.note_2.frequency)

        interval_wave = np.concatenate((sound_wav_1, sound_wav_2), axis=None)

        return interval_wave