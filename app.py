from flask import Flask, render_template, redirect
import random
import pygame
import os

# Set '__location__' variable to directory of script
__location__ = os.path.realpath(
    os.path.join(
        os.getcwd(),
        os.path.dirname(
            __file__
        )
    )
)

# Set location variables to the script location + fileName
fartFile1 = __location__ + '/audio/fart1.wav'
fartFile2 = __location__ + '/audio/fart2.wav'
fartFile3 = __location__ + '/audio/fart3.wav'

staticPath = "/" + __location__ + '/static'

# Create app
app = Flask(__name__, static_url_path=staticPath)


# Initialize pygame mixer
pygame.mixer.init()

# Define route for index page
@app.route('/')
def index():
    return render_template('index.html')

# Define route for playing the fart sound
@app.route('/fart')
def fart():
    # Load and play the fart sound
    #fart_sounds = [fartFile1, fartFile2, fartFile3]
    fart_sounds = [fartFile1, fartFile2, fartFile3]
    random_fart_sound = random.choice(fart_sounds)
    fart_sound = pygame.mixer.Sound(random_fart_sound)
    fart_sound.play()
    # Redirect back to the root directory
    return redirect("/")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html'), 404