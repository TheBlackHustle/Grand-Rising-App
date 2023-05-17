import re                     # Imports datetime library
import pymongo
from pymongo import MongoClient
import requests
from requests.auth import HTTPBasicAuth
import base64
import os
#import openai
import time
from statistics import mean
import sqlite3
from datetime import date
import datetime
from pytz import timezone
from google.colab import drive
import json

#This is the openAI key 
os.environ["OPENAI_API_KEY"] = "----"

openweather_key = '274ff023d5e912e80113cfee65a2170b'
city = 'Plainsboro'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={openweather_key}&units=imperial'


'''def generate_text(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text'''

def generate_prompt():
    today = date.today().strftime("%B %d, %Y")  # get today's date in the format "Month Day, Year"
    try:
        today = date.today().strftime("%B %d, %Y")  # get today's date in the format "Month Day, Year"
    except Exception as e:
        print('Error caught as', e)
        #today = "today"  # use a default value if there is an error
def getTime():
   # Get current time in local timezone
    local_time = datetime.datetime.now()
    est = timezone('US/Eastern')
    est_time = local_time.astimezone(est)

    # Return date and time as a formatted string
    print('The current time in EST is', est_time.strftime("%B %d, %Y %I:%M %p"))


def get_weather():
  response = requests.get(url)
  weather_data = response.json()
  temperature = weather_data['main']['temp']
  
  print('The current temperature for', city, 'is', temperature)


def getWorkout():
  drive.mount('/content/drive')


def lambda_handler(event, context):
     print('Grand Rising Daddy Dev...')
     current_time = getTime()
     get_weather()
      #e = event

     ses = boto3.client('ses')

     body = insertFunction()

     ses.send_email(
	    Source = 'blank',
	    Destination = {
		    'ToAddresses': [
			    'blank'
		    ]
	    },
	    Message = {
		    'Subject': {
			    'Data': 'SES Demo',
			    'Charset': 'UTF-8'
		    },
		    'Body': {
			    'Text':{
				    'Data':body[0]['Firstname'] + "," + " Todays message...." + "\n" + "\n" +
                    ":)" "\n"
				    "\n" + body[10]['GitLink'] + "\n" + body[11]['StackOverflowLink'] + "\n" + body[12]['GoogleScholarLink'] + "\n" + body[13]['TwitterLink'] + 
				    "\n" + "\n " + "Thank you," + "\n" + "\n" + body[14]['SendersSignature'],
				    'Charset': 'UTF-8'
			    }
		    }
	    }
    )
    
     return {
        'statusCode': 200,
        'body': json.dumps('Successfully sent email from Lambda using Amazon SES')
