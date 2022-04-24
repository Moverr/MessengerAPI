from flask import Flask, render_template
 

from services.MessengerService import MessengerService

messenger  = MessengerService() 
 
app = Flask(__name__)
app.debug = True
app.secret_key = 'development key'

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/",methods=['GET'])
def home():
    return  render_template('welcome.html')

@app.route("/send",methods=['POST'])
def send():
    messenger.sendMessage
    print("lsoooelose")
    return   "Send"


@app.route("/receive",methods=['POST'])
def receive():
    messenger.receiveMessage
    return  "Received"

# api.add_resource(home(),)