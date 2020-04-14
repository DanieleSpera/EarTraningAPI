import app_settings

class Note():

    def __init__(self):

        #app settings
        self.notes_list = app_settings.note_freq_dict

        #class settings
        self.labels = []
        self.base_frequency = 0
        self.octave = 4
        self.frequency = 0
        self.scale_position = 0
        
    @property
    def octave(self):
        return self.__octave
    
    @octave.setter
    def octave(self,oct):
        self.__octave = oct
        self.frequency = self.get_frequency_note(oct)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,note_name):
        self.__name = note_name
        note_item = list(filter(lambda note: note_name in note[0], self.notes_list))[0]
        self.labels = note_item[0]
        self.base_frequency = note_item[1]
        self.frequency = self.get_frequency_note(self.octave)
        self.scale_position = self.notes_list.index(note_item)


    def get_frequency_note(self,octave):
        """Calculates the frequecy base on the given octaves"""
        frequency = self.base_frequency
        for i in range(int(octave)):
            frequency = frequency * 2
        return frequency

    def log_note_property(self):
        print("-> NOTE: Name: %s labels %s base_frequency %s octave %s  frequency %s scale_position %s" % (self.name,self.labels,self.base_frequency,self.octave,self.frequency,self.scale_position))