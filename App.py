from flask import Flask, render_template


app = Flask(__name__)

@app.route("/",methods=['GET'])
def home():
    return  render_template('welcome.html')

@app.route("/send",methods=['POST'])
def send():
    return   "Send"


@app.route("/receive",methods=['POST'])
def receive():
    return  "Receive"
