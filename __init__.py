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

@app.route("/intervals/<root>/<interval>")
def get_interval_sound(root,interval):
   generator = Interval()
   interval_url = generator.get_interval_audio_url(root,interval)
   return send_file(interval_url)


if __name__ =="__main__":
   app.run()
