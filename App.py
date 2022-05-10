import json
from flask import Flask, jsonify, render_template
import jsons

import pika
from entities.Notification import Notification


from services.MessengerService import MessengerService


app = Flask(__name__)
app.debug = True
app.secret_key = 'development key'

if __name__ == "__main__":
    app.run(debug=True)


@app.route("/", methods=['GET'])
def home():
    return render_template('welcome.html')


@app.route("/send", methods=['POST'])
def send():

    messenger = MessengerService()
    messenger.sendMessage()

    return "sent message"


@app.route("/receive", methods=['POST'])
def receive():
    messenger = MessengerService()
    st  = messenger.receiveMessage()
    return jsonify({'data': st})

 
