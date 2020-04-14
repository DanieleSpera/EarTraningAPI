#Server Variables
#audio_dir = '/var/www/MusicApp/app/audio_files/'


#Local Variables
audio_dir = "/Users/danielespera/Downloads/PythonProjects/ChordProject/audio_files/"

sample_rate = 44100

note_freq_dict = [
#     Notes       Base Freq
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

intervals = [
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
