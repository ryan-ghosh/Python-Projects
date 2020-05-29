from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
import smtplib
from gtts import gTTS
from time import ctime

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def recordAudio(ask=False):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if ask:
            omai_speak(ask)
        audio = r.listen(source)
        voiceData = ""
        try:
            voiceData = r.recognize_google(audio)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            omai_speak("Sorry, my speech service is down")
        return voiceData

def omai_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1,10000000)
    audioFile = 'audio-' + str(r) + '.mp3'
    tts.save(audioFile)
    playsound.playsound(audioFile)
    print(audio_string)
    os.remove(audioFile)


def respond(voice_data):
    icebreakers = ["how was your day today?", "what did you do today?", "Do you have a date tonight?", "How were your friends today?"]
    if 'hello' in voice_data or 'hi' in voice_data or "you there?" in voice_data:
        omai_speak("Hello!")
    if "thank you" in voice_data:
        answers = ["Your welcome", "No problem", "My pleasure", "Just doing my job"]
        x = random.randint(0, len(answers))
        omai_speak(answers[x])
    if 'what is your name' in voice_data:
        omai_speak('My name is Omai')
    if "favorite color" in voice_data:
        omai_speak("My favorite color is gold")
    if "start conversation" in voice_data:
        x = random.randint(0, len(icebreakers))
        omai_speak(icebreakers[x])
        convo = recordAudio()
        omai_speak("That's good. Did you finish everything on your schedule today?")
    if 'what time is it' in voice_data:
        currentDT = datetime.datetime.now()
        omai_speak("it is" + str(currentDT.strftime("%H:%M:%S")))
    if 'what is the date' in voice_data:
        currentDT = datetime.datetime.now()
        omai_speak("it is" + str(currentDT.strftime("%a, %b %d, %Y")))
    if "install a package" in voice_data:
        command = recordAudio("what do you wish to install?")
        omai_speak("Yes sir.")
        os.system("pip install " + command.replace(" ", ""))
        omai_speak("Done")
    if "run program" in voice_data:
        program = recordAudio("which program?")
        os.system("python {}.py".format(program.replace(" ", "_")))
        omai_speak("Done, check terminal for output")
    if 'search' in voice_data:
        search = recordAudio("What do you wish to know?")
        search = search.replace(' ', '+')
        url = 'https:"//google.com/search?q=' + search
        webbrowser.get().open(url)
        omai_speak("Here is what I found for " + search.replace('+', " "))
    if 'find location' in voice_data:
        location = recordAudio("What is the location?")
        url = 'https:"//google.nl/maps/place/' + location.replace(' ', '+') + '/&amp;'
        webbrowser.get().open(url)
        omai_speak("Here is the location of " + location)
    if 'weather' in voice_data:
        url = 'https://www.google.com/search?q=weather'
        omai_speak("This is the weather today")
        webbrowser.get().open(url)
    if "hype me up" in voice_data or "the scene" in voice_data:
        omai_speak("Yes sir")
        url = "https://www.youtube.com/watch?v=PQleT6BtCbE"
        webbrowser.get().open(url)
    if 'Henry' in voice_data:
        omai_speak("Ok buddy")
    if "send email" in voice_data:
        recipient = recordAudio("Who is the recipient?") 
        address = recordAudio("What is the email address?")   # speak email address
        address.replace(" ", "")
        content = recordAudio("What should I say?")
        ## init gmail smtp
        mail = smtplib.SMTP("smtp@gmail.com", 587)

        ## identify to server
        mail.ehlo()

        ## encrypt
        mail.starttls()

        ## login
        mail.login("ryan.ghosh21", "akre6829")

        ## send mail
        mail.sendmail(recipient, "{}@gmail.com".format(address), content)
        ## close conneciton
        mail.close()
        omai_speak("email sent")
    if 'satisfied' in voice_data:
        omai_speak("Til next time")
        exit()

def authenticate_google():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    return service

def get_events(n, service):
    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print(f'Getting the upcoming {n} events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=n, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])


service = authenticate_google()
get_events(2,service)
time.sleep(1)
omai_speak("Hello, my name is Omai, your personal assistant. How can I help you?")
while 1:
    voiceData = recordAudio()
    respond(voiceData)