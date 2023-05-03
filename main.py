from twilio.rest import Client
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Twilio account SID and auth token
account_sid = 'AC9855d1fd6614f8340b93c42660d6da93'
auth_token = 'd51d9032b57752ff337d875920abd903'

# Twilio WhatsApp number
whatsapp_number = 'whatsapp:+14155238886'

# create a Twilio client object
client = Client(account_sid, auth_token)

# route to receive incoming WhatsApp messages
@app.route('/whatsapp', methods=['POST'])
def whatsapp_reply():
    # get the incoming message details
    msg_from = request.form['From']
    msg_body = request.form['Body']

    # create a messaging response object
    resp = MessagingResponse()

    # create a reply message
    reply_msg = "Hello! You said: " + msg_body

    # send the reply message
    message = client.messages.create(
        body=reply_msg,
        from_=whatsapp_number,
        to=msg_from
    )

    # add the reply message to the messaging response
    resp.message(reply_msg)

    return str(resp)

if __name__ == '__main__':
    app.run()