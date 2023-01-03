from flask import Flask, render_template, jsonify, send_file
import readAndWriteCalender

app = Flask(__name__)


@app.route('/api/calendar/')
def return_calendar():
    load_calendar()
    try:
        return send_file('var/calendar/DU2XWMWQ163866.ics')
    except Exception as e:
        return str(e)



def load_calendar():
    readAndWriteCalender.main()
    calendar = open('var/calendar/DU2XWMWQ163866.ics','r+')
    print(calendar.readlines())
    calendar.close()
    