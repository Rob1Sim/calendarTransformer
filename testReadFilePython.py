from datetime import datetime;

def load_calendar():
    #Ouverture du premier calendrier récupérer sur le web
    try:
        with open('var/calendar/DU2XWMWQ163866.ics', 'r+') as calendar:
            firstCalendar = calendar.readlines()
    except FileNotFoundError:
        print("Le calendrier est introuvable")
    
    actualDate= datetime.now().strftime('%d-%m-%Y-%H-%M-%S')
    
    try:
        
        with open('var/calendar/calendar'+actualDate+'.ics', 'w') as newCalendar:
            for line in firstCalendar:
                if line == "SUMMARY:MR" or line == "SUMMARY:MS":
                    print(line)
                
    except FileNotFoundError:
        print("Echec lors de l'ouverture")
    

if __name__ == '__main__':
    load_calendar()
