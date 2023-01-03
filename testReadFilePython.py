from datetime import datetime;

"""
    Récupère le calendrier enregistrer 
    
"""
def load_calendar():
    
    
    
    #Ouverture du premier calendrier récupérer sur le web
    try:
        with open('var/calendar/DU2XWMWQ163866.ics', 'r+') as calendar:
            firstCalendar = calendar.readlines()
    except FileNotFoundError:
        print("Le calendrier est introuvable")
    
    return firstCalendar;
    

"""
    Ecris un nouveau calendrier en formatant l'ancien
    """
def write_calendar():
    
    firstCalendar = load_calendar();
    actualDate = datetime.now().strftime('%d-%m-%Y-%H-%M-%S')
    newFileName = 'calendar'+actualDate+'.ics'
    try:

        with open('var/calendar/'+newFileName, 'w') as newCalendar:
            for line in firstCalendar:
                line = line.replace("\n", "")
                if "SUMMARY:MR" in line or "SUMMARY:MS" in line:
                    ligne = ""
                    #Quitte la boucle lorsque on arrive a la fin du nom de la matière
                    for lettre in range(len(line)):

                        if line[lettre] == ";":
                            break
                        if lettre not in [i for i in range(8,14)]:
                            ligne += line[lettre]
                    print(ligne)


    except FileNotFoundError:
        print("Echec lors de l'ouverture")



if __name__ == '__main__':
    write_calendar()
