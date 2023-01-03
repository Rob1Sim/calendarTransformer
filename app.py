from flask import Flask, render_template, jsonify, send_file
from os import listdir
import readAndWriteCalender

app = Flask(__name__)


@app.route('/api/calendar/')
def return_calendar():
    basePath = "var/calendar/new/"
    file = load_calendar(basePath)
    try:
        return send_file(basePath+file)
    except Exception as e:
        return str(e)


def load_calendar(basePath):
    readAndWriteCalender.main()
    
    
    
    return listdir(basePath)[0]
    
