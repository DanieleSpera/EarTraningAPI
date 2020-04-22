from flask import Flask, send_file

app = Flask(__name__)

from tools.sound_file_generator import sound_generator
from tools.interval import Interval

@app.route("/")
def index ():
   return "MusicApp is active"

@app.route("/audiofile/<note>")
def get_note_sound(note):
   generator = sound_generator() 
   sound_url = generator.get_sound_url(note)
   return send_file(sound_url)

@app.route("/intervals/<root>/<interval>/<category>")
def get_interval_sound(root,interval,category):
   """Get the interval parameters and returns an audio file
   in -> string Root Note, string Interval, string category "Melodic" or "Harmonic"
   out -> void """
   generator = Interval()
   interval_url = generator.get_interval_audio_url(root,interval,category)
   return send_file(interval_url)


if __name__ =="__main__":
   app.run()