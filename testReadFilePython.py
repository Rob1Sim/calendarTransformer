def load_calendar():
    #Ouverture du premier calendrier récupérer sur le web
    try:
        with open('var/calendar/DU2XWMWQ163866.ics', 'r+') as calendar:
            firstCalendar = calendar.readlines()
    except FileNotFoundError:
        print("Le calendrier est introuvable")
    

if __name__ == '__main__':
    load_calendar()
