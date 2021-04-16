
import os
#you need to install twilio module by pip3 install twilio
from twilio.rest import Client
from time import sleep
import json

with open('cred.json','r') as f:
  data = (json.load(f))
  sid = data["account_sid"]
  token = data["auth_token"]

client = Client(sid, token)
#you can get your twilio number by going to www.twilio.com/console
def send(client):
	message = client.messages \
    	.create(
         	body='This is the ship that made the Kessel Run in fourteen parsecs?',
         	from_='put your twilio number',
         	to='Put hte number of the receiver'
         	
     	)

	print("Message sent to put the number of receiver")

send(client)