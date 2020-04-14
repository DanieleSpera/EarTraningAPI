""" Interval Generation Module """

import numpy as np

from tools.sound_file_generator import sound_generator 

class interval_generator:

    def __init__(self,root,interval):

        self.settings = {'audio_dir' : '/var/www/MusicApp/app/audio_files/'}
        self.root = root.replace("sharp", "#")

        self.interval = interval

        self.notes_list = [
                #     Notes         Freq
                    [["C"      ] , 16.35 ],
                    [["C#","Db"] , 17.32 ],
                    [["D"      ] , 18.35 ],
                    [["D#","Eb"] , 19.45 ],
                    [["E"      ] , 20.60 ],
                    [["F"      ] , 21.83 ],
                    [["F#","Gb"] , 23.12 ],
                    [["G"      ] , 24.50 ],
                    [["G#","Ab"] , 25.96 ],
                    [["A"      ] , 27.50 ],
                    [["A#","Bb"] , 29.14 ],
                    [["B"      ] , 30.87 ] 
        ]

        self.intervals = [
                #         Name  half step distance
                        [["P1", "d2"] , 0 ],
                        [["m2", "A1"] , 1 ],
                        [["M2", "d3"] , 2 ],
                        [["m3", "A2"] , 3 ],
                        [["M3", "d4"] , 4 ],
                        [["P4", "A3"] , 5 ],
                        [["A4", "d5"] , 6 ],
                        [["P5", "d6"] , 7 ],
                        [["m6", "A5"] , 8 ],
                        [["M6", "d7"] , 9 ],
                        [["m7", "A6"] , 10],
                        [["M7", "d8"] , 11],
                        [["P8", "A7"] , 12]         
        ]
    def return_intervals (self):

        root = self.root
        interval = self.interval

        note1_name = root[:-1]
        note1_octave = root[-1]
        note1_item = list(filter( lambda note : note1_name in note[0] , self.notes_list))[0]
        note1_position = self.notes_list.index(note1_item)
        note1_frequency = self.get_frequency_note(note1_item[1], int(note1_octave))
        
        interval_item = list(filter( lambda interval_itm : interval in interval_itm[0] , self.intervals))[0]
        distance = interval_item[1]

        total_distance = note1_position + distance
        oct_difference = total_distance // (len(self.intervals)-1)

        note2_index = total_distance - ((len(self.intervals)-1) * oct_difference)
        note2_octave = int(note1_octave) + oct_difference

        note2_item = self.notes_list[note2_index]
        note2_frequency = self.get_frequency_note(note2_item[1], int(note2_octave))

        test1 = "note1_name: %s note1_octave %s note1_item %s note1_position %s  note1_frequency %s" % (note1_name,note1_octave,note1_item,note1_position,note1_frequency)
        test2 = "interval_item: %s distance %s total_distance %s number_steps %s" % (interval_item,distance, total_distance,len(self.intervals))
        test3 = "note2_index: %s note2_octave %s   " % (note2_index,note2_octave)
        test4 = "note2_item %s note2_frequency %s  " % (note2_item,note2_frequency)

        
        s_generator = sound_generator()
        sound_wav_1 = s_generator.generate_note(note1_frequency)
        sound_wav_2 = s_generator.generate_note(note2_frequency)

        interval_wave = np.concatenate((sound_wav_1, sound_wav_2), axis=None)
        
        file_name =  root+"-"+interval
        s_generator.generate_file( interval_wave, file_name )

        return self.settings.get('audio_dir')+file_name+'.mp3'
        #return test1 + "|||" + test2 + "|||" + test3 + test4


    def get_frequency_note(self,base_frequency,octave):
        frequency = base_frequency
        for freq in range(octave):
            frequency = frequency * 2
        return frequency
