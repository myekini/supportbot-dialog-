import os
import json
from flask import Flask
from flask import Flask, request, make_response
from Send_email.send_mail import EmailSender

app = Flask(__name__)


# geting and sending response to dialogflow
@app.route('/', methods=['GET', 'POST'])

def webhook():
    req = request.get_json(silent=True, force=True)
    res = processRequest(req)
    print(res.sessionID)
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


# processing the request from dialogflow
def processRequest(req):
   
    sessionID = req.get('responseId')
    result = req.get("queryResult")
    user_says = result.get("queryText")
    parameters = result.get("parameters")
    wallet_address= parameters.get("wallet_address")
    nft_type = parameters.get("nft_type")
    

   
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0')