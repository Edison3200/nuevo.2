from flask import render_template
from src import app
from os import path

INSTALACION_PATH = path.abspath('instalacion.txt')

@app.route('/')
def index():
    if(path.exists(INSTALACION_PATH)):
        return render_template('instalacion.html')
    
    return render_template('index.html')