from flask import Flask, render_template, request, jsonify, send_from_directory
from gtts import gTTS
import os

app = Flask(__name__)

# Directory to store generated audio files
AUDIO_DIR = "static/audio"
if not os.path.exists(AUDIO_DIR):
    os.makedirs(AUDIO_DIR)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get")
def get_bot_response():
    message = request.args.get('msg')
    
    # Use gTTS to generate the speech audio file
    tts = gTTS(text=message, lang='en', slow=False)
    audio_file = os.path.join(AUDIO_DIR, "output_audio.mp3")
    tts.save(audio_file)
    
    # Return the path to the generated audio file
    return jsonify(audio_url=f"/{audio_file}")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
