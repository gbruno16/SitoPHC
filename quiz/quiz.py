import requests
from bs4 import BeautifulSoup
from scipy import rand
from random import randrange
import json
#scp -r Quiz bruno@poisson.phc.dm.unipi.it:~/public_html/Quiz 
URL="https://unimap.unipi.it/registri/dettregistriNEW.php?re=3325977::::&ri=4183"
materia="Prob_2122"
page = requests.get(URL)
domande={}
soup = BeautifulSoup(page.content, "html.parser")
list_raw = soup.find_all("li")
i=0
for lezione in list_raw:
    testo=lezione.text
    if testo.find("lezione") != -1:
        data, body=testo.split(" lezione: ")
        argomenti=body.split(".")[:-1]
        #print(argomenti)
        #domande+=argomenti
        for argomento in argomenti:
            domande["d"+str(i)]={"domanda":argomento, "data":data, "autore":"Registro"}
            i+=1
    elif testo.find("esercitazione") != -1:
        data, body=testo.split(" esercitazione: ")
        argomenti=body.split(".")[:-1]
        #print(argomenti)
        #domande+=argomenti
        for argomento in argomenti:
            domande["d"+str(i)]={"domanda":argomento, "data":data, "autore":"Registro"}
            i+=1

    

print(domande)

a_file = open("./data/"+materia+".json", "w")
a_file = json.dump(domande, a_file)

# Open a file with access mode 'a'
with open("data/list.txt", "a") as file_object:
    # Append 'hello' at the end of file
    file_object.write(","+materia)
