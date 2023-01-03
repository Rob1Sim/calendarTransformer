from datetime import datetime
from genericpath import isfile;
from os import remove,listdir,path;
from time import sleep

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
    
    #Génère un nom de fochier unique
    firstCalendar = load_calendar();
    actualDate = datetime.timestamp(datetime.now())
    newFileName = 'calendar'+str(actualDate)+'.ics'
    
    try:
        
        with open('var/calendar/new/'+newFileName, 'a') as newCalendar:
            lastLineSummarry = False
            lastLineDesc = False

            for line in firstCalendar:
                
                if lastLineSummarry :
                    line = ""
                    lastLineSummarry = False

                if "SEQUENCE:" in line:
                    lastLineDesc = False
                
                if lastLineDesc:
                    line = ""

                    
                
                
                if "SUMMARY:MR" in line or "SUMMARY:MS" in line:
                    ligne = ""
                    #Quitte la boucle lorsque on arrive a la fin du nom de la matière
                    for lettre in range(len(line)):

                        if line[lettre] == ";":
                            break
                        if lettre not in [i for i in range(8,14)]:
                            ligne += line[lettre]
                    line = ligne + "\n"
                    lastLineSummarry = True
                
                
                if "DESCRIPTION:" in line:
                    line = "DESCRIPTION:\n"
                    lastLineDesc = True

                
                

                    
                
                    #On réécrit les lignes changés
                newCalendar.write(line)

    except FileNotFoundError:
        print("Echec lors de l'ouverture")

    """
    Cherche et supprime les version obselète du calendrier
    """
def delete_obselete_calendar():
    dir_path = "var/calendar/new/"
    listOfTimeStamp = {}

    for _path in listdir(dir_path):
        if path.isfile(path.join(dir_path,_path)):
            listOfTimeStamp[datetime.fromtimestamp(path.getmtime
                            (path.join(dir_path, _path)))] = _path
    #On trie les clé (donc les date de modif) sans perdre les valeurs
    listOfTimeStamp = sorted(listOfTimeStamp.items(), key=lambda x: x[1])
    print(listOfTimeStamp.pop())
    
    
    for file in listOfTimeStamp:
            try:
                remove(path.join(dir_path, file[1]))
            except Exception as e:
                print(str(e))
    
    

def main():
    write_calendar()
    delete_obselete_calendar()

if __name__ == '__main__':
    main();
