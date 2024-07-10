# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 18:23:01 2024

@author: LAKSHMI
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detect():
    ''' This function gets emotions
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    formatted_text = ""
    response = emotion_detector(text_to_analyze)
    for key1, value1 in response.items():
        if key1 == 'dominant_emotion':
            formatted_text += f"The dominant emotion is {value1}"
        else:
            formatted_text += f"'{key1}': {value1}, "
    if response['dominant_emotion'] is None:
        formatted_text1 = "Invalid input ! Try again."
    else:
        formatted_text1= formatted_text
    return formatted_text1

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
