import os
import pymongo
from pymongo import MongoClient
import json
from flask import Flask
from flask import Flask, request, make_response
from resources.Send_email.send_mail import EmailSender
from resources.template_reader import TemplateReader
from resources.handlers.mongodb import Log


app = Flask(__name__)


# geting and sending response to dialogflow
@app.route('/', methods=['GET', 'POST'])

def hello_world():
	return 'Hello World!'

def webhook():
    req = request.get_json(silent=True, force=True)
    res = processRequest(req)
    
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def configureDatabase():
    """Configures the database"""
    client = pymongo.MongoClient("mongodb+srv://myekini:Muhammadyk1@cluster0.qinyqn8.mongodb.net/?retryWrites=true&w=majority")
    return client.get_database('supportbot')


# processing the request from dialogflow
def processRequest(req):
    log = Log()
    sessionID = req.get('responseId')
    result = req.get("queryResult")
    user_says = result.get("queryText")
    parameters = result.get("parameters")
    response = result.get('fulfillmentText')
    wallet_address= parameters.get("wallet_address")
    nft_type = parameters.get("nft_type")
    r_email = parameters.get("email")
    intent = result.get("intent").get('displayName')
    db = configureDatabase()
    
    # process email automation with user information
    if intent == "Balance intent":
        email = EmailSender()
        template = TemplateReader()
        email_message = template.read_course_template(nft_type)
        email.send_email_to_student(r_email, email_message)
    
        #save converstion into database
        log.saveConversations(sessionID, intent, user_says, response, db)




if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0')