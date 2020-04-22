""" Interval Generation Module """

import os
from enum import Enum 
import numpy as np

import app_settings
from tools.note import Note
from tools.sound_file_generator import sound_generator


class Interval:

    def __init__(self):

        #app settings
        self.audio_dir = app_settings.audio_dir + "Intervals/"
        self.notes_list = app_settings.note_freq_dict
        self.intervals = app_settings.intervals

        #class settings
        self.note_1 = None
        self.note_2 = None
        self.selected_root = ""
        self.selected_interval = ""
        self.s_generator = sound_generator()
        self.category = Interval_Category.Melodic
        
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

    #---------> API INPUT / ENTRY POINT
    def get_interval_audio_url(self,root,selected_interval,category):

        self.selected_root = root.replace("sharp","#")
        self.selected_interval = selected_interval
        self.category = Interval_Category(category)

        file_name = self.selected_root+"-"+ self.selected_interval

        folder_file = self.audio_dir + self.category.value+"/"
        path_note = folder_file + file_name+'.mp3'

        if(not os.path.exists(path_note)):
            self.generate_interval(self.selected_root,self.selected_interval)
            soundwave = self.generate_interval_soundwave()
            self.s_generator.generate_file(soundwave, folder_file, file_name)

        return path_note

    def generate_interval(self, root, selected_interval):
        """Get the second note given the first
        in -> String root note , String Interval
        out -> void """

        self.note_1 = Note()
        self.note_1.name = root[:-1] #note name
        self.note_1.octave = int(root[-1])#note octave
        
        self.note_1.log_note_property()

        self.note_2 = self.get_second_note_from_root(self.note_1, selected_interval)

        self.note_2.log_note_property()

    def generate_interval_soundwave(self):
        print('generate_interval_soundwave')
        if None  in (self.note_1, self.note_1):
            raise Exception('Interval Notes are not defined')
        
        sound_wav_1 = self.s_generator.generate_note(self.note_1.frequency)
        sound_wav_2 = self.s_generator.generate_note(self.note_2.frequency)

        if self.category == Interval_Category.Melodic:
            print('Melodic')
            interval_wave = np.concatenate((sound_wav_1, sound_wav_2), axis=None)
        elif self.category == Interval_Category.Harmonic:
            print('Harmonic')
            interval_wave = sound_wav_1 + sound_wav_2

        return interval_wave


class Interval_Category(Enum):
    Melodic = "Melodic"
    Harmonic = "Harmonic"