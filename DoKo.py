
import random
import time 
from collections import Counter

funnyzahl = int(random.random()*1000000)
random.seed(funnyzahl)

spieler = ["Mäthy","Alex","Leo","Leopold","Maxi","Takeshi","Kilian","Marlene","Paul","Paula","Pascal","Pauline","Thilo"]

#heute Raus: Lisa und Thilo 

#spielplan auslosen 
#kontrollieren, wie optimal 
#speichern oder verwerfen 


spieler = ["Mäthy","Alex","Leo","Leopold","Maxi","Takeshi","Kilian","Marlene","Paul","Paula","Pascal","Pauline","Thilo"]

#abbruchbedinungen

#maximale Laufzeit der Programms
laufzeit = 60*5
#mind Anzahl an Mitspielern für jeden Spieler 
mind_anzahl_mitspieler = 9
#Anzahl an generierten Spielplänen (der aktuellen Stufe) ohne das eine besser Stufe erreicht wurde
max_spielplaene = 10**9



start_time = time.time()
spielplan = []
i_spielplan = 0

max_lowest_mitspieler = 0

def flatten(liste):
    return [item for sublist in liste for item in sublist]


while (time.time()-start_time) < laufzeit and i_spielplan < max_spielplaene and max_lowest_mitspieler<mind_anzahl_mitspieler:
    
    #Generation des Spielplans 
    spielplan_t = [[],[],[],[]]  
    for i in range(4):
        #durchläuft die Runden (i.Runde)
        #tische = [[]*int(len(spieler)/4)][:] # fick Python der denkt ich will 4 mal hintereinander die selber Liste
        tische = [[] for i in range(int(len(spieler)/4))]

        spieleranzahl = [0]*int(len(spieler)/4)
        kanidaten = list(range(len(spieler))) 

        for k in range(4*int(len(spieler)/4)):
            #durchläuft die Anzahl an Spieler die maximal Spielen können, wählt sich jede runden einen aus und ordnet diesen einem Tisch zu 
            zugeordnet = False
            while zugeordnet == False:
                kanidat = kanidaten[random.randrange(0,len(kanidaten),1)]
                zuordung = int(random.random()*len(tische)-0.5)
                if spieleranzahl[zuordung]<4:
                    tische[zuordung].append(kanidat)
                    kanidaten.remove(kanidat)
                    spieleranzahl[zuordung] += 1
                    zugeordnet = True
        
    
        spielplan_t[i]=tische
    
    #Test des Spielplans
    anzahl_mitspieler = []
    vielfachheit_mitspieler = []

    for j in range(len(spieler)):
        #durchläuft die Spieler
        mitspieler = []
        for k in range(len(spielplan_t)):
            #durchläuft k. Runde
            for l in range(len(spielplan_t[k])):
                #durchlüft die Tische
                if j in spielplan_t[k][l]:
                    #wenn Spieler am Tisch werden alle anderen Spieler an diesem Tisch zu seinen Mitspielern hinzugefügt
                    mitspieler.append(spielplan_t[k][l])
        
        #Liste wird 1d und der Spieler selbst wird entfernt
        mitspieler = flatten(mitspieler)
        mitspieler = list(filter((j).__ne__, mitspieler))
        
        #Parameter der Güte des Spielplans
        #1. Anzahl an verschiedenen Mitspielern des Spielers
        anzahl_mitspieler.append(len(Counter(mitspieler).keys()))
        #2. Vielfachheit mit den Mitspielern 
        vielfachheit_mitspieler.append(list(Counter(mitspieler).values()))


    #Bewertung und ggf. abspeichern und ggf. ersetzten
    if min(anzahl_mitspieler)>max_lowest_mitspieler:
        #spielplan ist besser als alle bisherigen und alle anderen werden gelöscht
        spielplan = [spielplan_t]
        i_spielplan = 1
        max_lowest_mitspieler = min(anzahl_mitspieler)
    elif min(anzahl_mitspieler)>=max_lowest_mitspieler:
        #Spielplan ist ähnlich gut, wie der aktuell bester Spielplan, er wird der Liste der validen Spielplände angehangen
        spielplan += [spielplan_t]
        i_spielplan += 1

print(spielplan)

print(max_lowest_mitspieler)













#Alt
"""
#x Anzahl an generierten Spielen 
x=10**7
spielplan = []
for i in range(x):
    spielplan.append([[],[],[],[]])
    for j in range(4):
        spiel = []
        for l in range(int(len(spieler)/4)):
            spiel.append("")
        spieleranzahl = [0,0,0,0]
        kanidaten = spieler[:] 

        for k in range(4*int(len(spieler)/4)):
            zugeordnet = False
            while zugeordnet == False:
                kanidat = kanidaten[int(random.random()*len(kanidaten)-0.5)]
                zuordung = int(random.random()*len(spiel)-0.5)

                if spieleranzahl[zuordung]<4:
                    spiel[zuordung] += " " + kanidat
                    kanidaten.remove(kanidat)
                    spieleranzahl[zuordung]+=1
                    zugeordnet = True
        spielplan[i][j]=spiel


#Kontrolle 
kontrolle = []
wertung = []
for i in range(x):
    #durchläfut die Spielpläne 
    kontrolle.append([0]*len(spieler))
    wertung.append(None)
    for j in range(len(spieler)):
        #durchläuft die Spieler
        mitspieler = ""
        for k in range(len(spielplan[i])):
            #durchläuft k. Runde
            for l in range(len(spielplan[i][k])):
                if str(spieler[j]+" ") in spielplan[i][k][l]:
                    mitspieler += str(spielplan[i][k][l])
            for m in range(len(spieler)):
                if mitspieler.count(spieler[m]) > kontrolle[i][j] and j!=m:
                    kontrolle[i][j] = mitspieler.count(spieler[m])
    wertung[i] = max(kontrolle[i])

print(min(wertung))
min_wert = min(wertung)
alle = True
optimale_x = []
while alle:
    try: 
        optimale_x.append(wertung.index(min_wert))
        wertung[optimale_x[-1]] = 9
    except:
        alle = False
print(optimale_x)
print("\n")
for i in optimale_x:
    print(spielplan[i])
    print(kontrolle[i])
    print("\n")

print("Es wurden {0} Spiele generiert. geringste maximale Überschneidung: {1}".format(x,min_wert))
"""