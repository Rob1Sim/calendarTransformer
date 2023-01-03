from flask import Flask, render_template, jsonify, send_file
from os import listdir
import requests
import readAndWriteCalender

app = Flask(__name__)


@app.route('/api/calendar/')
def return_calendar():
    fetch_calendar()
    basePath = "var/calendar/new/"
    file = load_calendar(basePath)
    try:
        return send_file(basePath+file)
    except Exception as e:
        return str(e)

    """
    Récupère un nouveau calendrier générer
    """
def load_calendar(basePath):
    readAndWriteCalender.main()
    return listdir(basePath)[0]
    

    """
    Récupère la dernière version du calendrier de l'URCA
    """
def fetch_calendar():
    url = "https://caldav.univ-reims.fr/URCA/cache/DU2XWMWQ163866.ics"
    calendar = requests.get(url,allow_redirects=True)
    open('var/calendar/DU2XWMWQ163866.ics','wb').write(calendar.content)
    print("yeah")
