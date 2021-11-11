#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import render_template
import os,subprocess
import time
app = Flask(__name__)




@app.route("/", methods=['POST', 'GET'])
def index():
    gg =''
    info =''
    newmod=''
    if request.method == "POST":
        f = request.files['audio_data']
        with open('audio.wav', 'wb') as audio:
            f.save(audio)
        print('file uploaded successfully')
        if os.path.isfile('./new.wav'):
            subprocess.run('rm ./new.wav',shell=True, check=True,executable='/bin/bash')

        render_template('index.html', request="POST")


        info='' #để text nhận dạng ở đây

        return info 
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='5050',debug = True,ssl_context=('adhoc'))
