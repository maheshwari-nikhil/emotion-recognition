from flask import Flask, flash, redirect, render_template, request, session, abort
import emotion_classifier

classifier = emotion_classifier.EmotionClassifier()
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/record", methods=['GET'])
def record():
	classifier.record_audio()
	predicted_emotion_array = classifier.classify_audio()
	return render_template('result.html', names = predicted_emotion_array[0]);

if __name__ == "__main__":
    app.run()