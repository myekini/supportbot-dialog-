import json
import requests
from flask import Flask
from Send_email.send_mail import EmailSender
from flask_cors import cross_origin

app = Flask(__name__)


# geting and sending response to dialogflow
@app.route('/webhook', methods=['POST'])
@cross_origin()
def webhook():

    req = requests.get_json(silent=True, force=True)
    res = processRequest(req)
    res = json.dumps(res, indent=4)
    
    return res

# processing the request from dialogflow
def processRequest(req):
   
    sessionID = req.get('responseId')
    result = req.get("queryResult")
    user_says = result.get("queryText")
    parameters = result.get("parameters")
    wallet_address= parameters.get("wallet_address")
    nft_type = parameters.get("nft_type")
    

if __name__ == '__main__':
   app.run()