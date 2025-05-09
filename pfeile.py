from datetime import datetime           #wir importieren die Biblothek "datetime" um am Ende ausgeben zu können wie lange das Skript gebraucht hat um das Rätsel zu lösen
starttime = datetime.now()              #Hier legen wir die Zeit fest bei welcher das Skript angefangen hat, das Rätsel zu lösen.

matrix_grösse = 6                       #Hier eingeben wie gross die Matrix ist, bei einer 6x6 Matrix soll es gleich 6 sein.

farbe = []                              #In dieser Liste wird die Farbe jedes Pfeiles in der Matrix fest gehalten. Für jede Zeile der Matrix wird eine neue Liste in dieser Liste hinzugefügt.
matrixs_print = []                      #In dieser Liste werden später die Richtung und Farbe des Pfeiles zusammengefügt und als ein lesbarer Pfeil gespeichert.

for x in range(0,matrix_grösse):        #Mit diesem for-loop erstellen wir alle Zeilen der Matrix
    farbe.append([])                    #Wir fügen eine neue leere Liste in die Liste namens "farbe". Diese leere Liste ist dann eine Zeile der Matrix.
    matrixs_print.append([])            #Dies gleiche tun wir ebenfalls bereits für die Liste "matrixs_print" welche später im Skript mit den entsprechenden Pfeilen gefüllt wird. 
    for y in range(0,matrix_grösse):    #Hier werden wir die Zeilen nun füllen
        farbe[x].append("g")            #Wir fügen wir nun "g" in die Zeilen ein. Das "g" steht für grau welches Unbekannt signalisiert.
        matrixs_print[x].append(0)

richtung = [["4","6","4","4","6","6"],["5","4","3","4","8","8"],["5","1","4","5","7","6"],["1","6","5","6","6","8"],["3","5","2","7","7","5"],["2","2","1","3","3","1"]]
#------------------------Richtungen von der Aufgabe Nr. 1, 6x6 Matrix----------------------------------
#Richtungen:
# 1 - Up
# 2 - Up-right
# 3 - Right
# 4 - Down-right
# 5 - Down
# 6 - Down-left
# 7 - Left
# 8 - Up-left

matrixs = [farbe, richtung]         #"matrixs" steht für die gesamte matrix welche die Richtung und Farbe in sich hat. Dies ist später nützlich da wir dann mit "matrixs[0]" oder "matrixs[1]" auswählen können ob wir die Farbe oder Richtung ansprechen möchten. Wir werden merken, dass dies sehr praktisch sein wird. Fun-Fact: Der Name kommt davon, dass wir die Mehrzahl von Matrizen auf English nicht wussten und zum Spass einfach ein "s" am Ende gemacht haben.

matrix_grösse -= 1                  #Wir verkleiner die Grösse um eins, da der Computer bei 0 beginnt zu zählen und nicht bei 1.
    

def pos_up(q,x,y,n,rtn_str=False):              #Funktion, Hier: geht eine Position nach oben in der Matrix --> Pos_up ---kurz für---> Position_up
    a = 0                                       #x = x-Achse; y = y-Achse; q = ob die Farbe oder Richtung angesprochen wird; n = wie oft wir in eine Richtung gehen möchten (z.B. n=2 wäre hier zwei mal nach oben gehen in der Matrix); rtn_str = ob wir als Resultat den Inhalt des erreichten Feldes (default) oder die Koordinanten des erreichten Feldes zurück geben
    while a < n:                                #Könnte in der Theorie immer True sein, da wir später mit hilfe einer "If-Schleife" den Loop unterbrechen. Für die schönheit und redundanz überprüfen wir hier jedoch ebenfalls ob wir bereits die gewünschte Anzahl an Versuchen gemacht haben
        a += 1                                  #Wir notieren, dass wir einmal den durchgang wiederhollt haben, somit können wir auch nur so oft wie gewollt in die gewollte Richtung gehen
        if y > 0:                               #überprüfen ob wir nicht bereits ganz oben sind
            y -= 1                              #Um eine Position in der Matrix hoch zu gehen, müssen wir in unserer Liste minus eins rechnen, bei uns ist die Koordinate vom Ecken oben links (0/0) und nicht unten links wie in einem "normalen" Koordinatensystem
        else:
            return False                        #Falls wir am Rand sind, geben wir False zurück
        if a == n:                              #Falls wir bereits die n-mal in die Richtung gegangen sind und nicht auf den Rand gestossen sind, geben wir nun entweder die erreichte Koordinate zurück oder dessen Inhalt
            if rtn_str == True:                 #Wir gucken ob die Koordinaten benötigt werden
                return x,y                      #Falls "rtn_str" gleich "True" war gibt es nun die x,y Koordinaten von der neuen Position. In diesem Fall eine Position über der welche eingereicht wurde
            else:
                return matrixs[q][y][x]         #Falls nicht dann wird die Farbe oder Richtung zurück gegeben
                                                #Je nachdem ob der User für q 0 oder 1 angegeben hat; 0 -> Farbe ; 1 -> Richtung

def pos_up_right(q,x,y,n,rtn_str=False):        #Nach oben-rechts
    a = 0               
    while a < n:
        a += 1
        if y <= 0 or x >= matrix_grösse:                    # Wir gucken ob wir am rechtem Rand oder oberen Rand sind   
            return False                                    # Falls wir am Rand sind, brechen wir ab ---> return False
        else:            
            x += 1
            y -= 1
        if a == n:
            if rtn_str == True:
                return x,y
            else:
                return matrixs[q][y][x]
    
def pos_right(q,x,y,n,rtn_str=False):           #Nach oben
    a = 0              
    while a < n:
        a += 1
        if x < matrix_grösse:                               # Wir überprüfen ob wir am rechtem Rand sind
            x += 1
        else:
            return False
        if a == n:
            if rtn_str == True:
                return x,y
            else:
                return matrixs[q][y][x]

def pos_down_right(q,x,y,n,rtn_str=False):      #Nach unten-rechts
    a = 0               
    while a < n:
        a += 1
        if y >= matrix_grösse or x >= matrix_grösse:        # Wir überprüfen ob wir am unterem Rand oder am rechtem Rand sind           
            return False   
        else:            
            x += 1
            y += 1
        if a == n:
            if rtn_str == True:
                return x,y
            else:
                return matrixs[q][y][x]

def pos_down(q,x,y,n,rtn_str=False):            #Nach unten
    a = 0              
    while a < n:
        a += 1
        if y < matrix_grösse:                               # Wir überprüfen ob wir am unterem Rand sind
            y += 1
        else:
            return False
        if a == n:
            if rtn_str == True:
                return x,y
            else:
                return matrixs[q][y][x]

def pos_down_left(q,x,y,n,rtn_str=False):       #Nach unten-links
    a = 0               
    while a < n:
        a += 1
        if y >= matrix_grösse or x <= 0:                   # Wir überprüfen ob wir am unterem oder linkem Rand sind
            return False   
        else:            
            x -= 1
            y += 1
        if a == n:
            if rtn_str == True:
                return x,y
            else:
                return matrixs[q][y][x]
    
def pos_left(q,x,y,n,rtn_str=False):            #Nach links
    a = 0              
    while a < n:                                                        
        a += 1
        if x > 0:                                          # Wir überprüfen ob wir am linkem Rand sind
            x -= 1
        else:
            return False
        if a == n:
            if rtn_str == True:
                return x,y
            else:
                return matrixs[q][y][x]
    
def pos_up_left(q,x,y,n,rtn_str=False):         #Nach oben-links
    a = 0               
    while a < n:
        a += 1
        if y <= 0 or x <= 0:                             # Wir überprüfen ob wir am oberem oder linkem Rand sind
            return False   
        else:            
            x -= 1
            y -= 1
        if a == n:
            if rtn_str == True:                 
                return x,y
            else:
                return matrixs[q][y][x]

#-----------------------------------------------------------------------------------------------           

#Eine Liste mit allen Richtungen, auf dieser Liste basieren die Richtungen in der Liste "Richtung"
#Der Name ist bezogen auf das Lied "I'm moving up and down like a rolercoaster"
movingUp_Down = [pos_up, pos_up_right, pos_right, pos_down_right, pos_down, pos_down_left,pos_left,pos_up_left]

def color(c,x,y):               # Mit dieser Funktion färben wir die Felder ein, c sagt uns in welcher Farbe wir das Feld einfärben sollen
    if c == "b":
        matrixs[0][y][x] = "b"  # Hier benötigen wir die Variable "q" nicht um uns zu sagen welche Matrix angesprochen wird (Farb- oder Richtungsmatrix) da wir ja natürlich die Farbe verändern
    if c == "w":                
        matrixs[0][y][x] = "w"

def Regel3(count_before):                           # Unsere 3te Regel bassiert auf dem ausschliessen, hier überprüfen wir wie viele Unbekannte ("g") wir haben. Falls dann ein Pfeil nur einen Unbekannten und keinen schwarzen sieht, muss dieser Unbekannte ein schwarzer Pfeil sein. Das Gleiche gilt aber auch anders herum, falls ein Pfeil einen schwarzen Pfeil bereits sieht, sind alle anderen gesehenen Pfeile weiss ("w") --> ist das gleiche wie Regel 2, wird hier jedoch wiederhollt um das Skript zu beschleunigen.
    old_grey_count = count_before                   # Die alte (sprich vom vorherigen durchlauf) Anzahl grauer Pfeile wird als Parameter durch gereicht und wird in "old_grey_count" gespeichert
    grey_count = 0                                  # Zählvariabel für wie viele graue (Unbekannte) Pfeile wir gesehen haben               
    for y in range(0, matrix_grösse + 1):           # Geht alle Zeilen der Matrix durch 
        for x in range(0, matrix_grösse + 1):       # Geht alle Spalten der Matrix durch 
            if matrixs[0][y][x] == "g":             # Durch die Kombination der vorherigen beiden "for" loops, wird hier jedes Element der Matrix kontrolliert auf dessen Inhalt. Falls es "g" (Grau/Unbekannt) ist,
                grey_count += 1                     # Die Zählvariable "grey_count" wird erhöht
            n = 0                                   # Zählvariable um mitzuzählen wie oft wir die folgende While Schleife wiederholt haben
            black_seen = 0                                                      #Zählvariabel um mitzuzählen wie viele schwarze Pfeile gesehen wurden
            grey_seen = []                                                      #Leere Liste in welcher wir die Koordinaten von grauen Pfeilen speichern werden
            richtung = int(matrixs[1][y][x]) - 1                                # Wir speichern die Richtung ab in welcher der zurzeit gewählte Pfeil zeigt (man muss minus eins rechnen da die Liste bei 0 beginnt zu zählen, könnte verhindert werden in dem ein decoy Element am Anfang eingefügt wird)
            while n < matrix_grösse + 1:                                        #In dieser Schleife gehen wir in eine Richtung und zählen wie viele Schwarze und Grau Pfeile wir sehen, wird maximal so oft wiederholt wie die Matrix gross ist, auch hier hätte es "while True" sein können, da es durch "if statements" unterbrochen wird. Aus redudanz und zur vermeitung endless-loops nicht "while True" 
                n += 1                                                          #Zählvariable n erhöhen
                if movingUp_Down[richtung](0,x,y,n) == "b":                     #In der Liste "movingUp_Down" wählen wir die Richtung in welche wir uns bewegen wollen, in diese Richtung Bewegen wir uns dann entsprechend oft zu welcher durchgang es der Schleife ist (wird in "n" gespeichert)
                    black_seen += 1                                             #Zählvariable wird um eins erhöht
                elif movingUp_Down[richtung](0,x,y,n) == "g":                   #Falls das Feld welches angeguckt wird grau ist:
                    grey_seen.append(movingUp_Down[richtung](0,x,y,n, True))    #Fügen wir die Koordinaten des gesehenen Pfeiles an eine Liste an. Dies machen wir weil wir später, in Abhängigkeit von anderen später folgenden Faktoren, diesen grauen Pfeil eventuell einfärben werden. In dem wir es so machen, verhindern wir, dass wir später nochmals nach den Koordinaten abfragen müssen.
                elif  movingUp_Down[richtung](1,x,y,n) == False:                #Falls "False" returnt wird, dann sind wir am Rand angekommen
                    if len(grey_seen) == 1 and black_seen == 0:                 #Falls ein Pfeil nur einen Unbekannten sieht und keinen Schwarzen, 
                        color("b", grey_seen[0][0], grey_seen[0][1])            #dann wird dieser Unbekannte Pfeil schwarz einfärbt
                    elif len(grey_seen) >= 1 and black_seen == 1:               #Falls ein oder mehrere graue Pfeile und ein schwarzer Pfeil gesehen werden
                        for grey_arrow in grey_seen:                            #Werden in diesem for-loop alle grauen/Unbekannten Pfeile weiss eingefärbt (ähnlich Regel 2)
                            color("w", grey_arrow[0],grey_arrow[1])             #Ruft die Funktion zum erwähnten weiss einfärben auf
    
    if grey_count == 0:                                                         #Falls keine grauen Pfeile mehr in der Matrix sind, ist das Skript fertig und es bricht den "loop" ab
        print_matrix(matrixs_print)                                             #Sobald das Rätsel fertig gelöst ist, rufen wir "print_matrix" auf um die Matrix auch visuelle vorzeigen zu können.
        return                                                                  #Nachdem die fertige Matrix geprintet wurde, "beenden" wir die Funktion mit dem "return" Befehl
    elif old_grey_count == grey_count:                                          #Falls die jetzige Anzahl grauer Pfeile gleich ist wie zuvor, sprich es konnte kein neuer weisser oder schwarzer Pfeil gefunden werden, brechen wir das Skript ab da es sonst unendlich lange laufen würde.
        print("")
        print("Da hat etwas nicht geklappt, sind die Richtungen sicher korrekt angegeben worden?")
        print("")
        return                                                                  
    else:                                                                       #Falls es jedoch noch graue Pfeile gibt, wird Regel 3 erneut wiederhollt
        Regel3(grey_count)
             
def Regel1():                                                                       #Regel 1 bassiert darauf, dass falls ein Pfeil nur einen anderen Pfeil sieht, dieser gesehene Pfeil schwarz sein muss. Damit können wir bereits am Anfang einige schwarze Pfeile finden                                                           
    for y in range(1, matrix_grösse+1):                                             #Wir gehen durch fast alle möglichen y Koordinaten durch. Die erste und letzte Zeile kann übersprungen werden, da nur Pfeile welche ein Feld vom Rand entfernt sind, ein positives Resultat liefern können.
        for x in range(1, matrix_grösse+1):                                         #Wir gehen durch fast alle möglichen x Koordinaten durch. Die erste und letzte Zeile kann übersprungen werden, da nur Pfeile welche ein Feld vom Rand entfernt sind, ein positives Resultat liefern können.
            richtung = int(matrixs[1][y][x])                                        #Wir legen die Richtung in welche ein Pfeil guckt fest, indem wir dessen Inhalt aus der "Richtung-Matrix" ablesen
            if movingUp_Down[richtung - 1](0,x,y,2) == False:                       #Wir bewegen uns zwei mal in die zuvor bestimmte Richtung und falls dort "False" zurück kommt, sind wir an den Rand gestossen
                toBeColored = movingUp_Down[richtung - 1](0,x,y,1,True)             #Wir speichern die Koordinaten vom Pfeil welcher angemalt werden soll in "toBeColored" 
                color("b", toBeColored[0], toBeColored[1])                          #Wir färben den erwähnten Pfeil schwarz da ein anderer nur diesen einen Pfeil sieht und per Rätsel Regel, dieser Schwarz sein muss.
    Regel3(0)                                                                       #Wir fahren weiter fort mit Regel 3
            
def arrow_print_setup():                                #Diese funktion wird benutzt um die beiden Matrizen (Richtungs- und Farb-Matrix) zu "übersetzen" in Pfeile welche später ausgegeben werden
    for y in range(0,matrix_grösse + 1):                #Wir legen alle möglichen y-Koordinaten fest um alle durchzugehen
        for x in range(0,matrix_grösse + 1):            #Wir legen alle möglichen x-Koordinaten fest um alle durchzugehen
            if matrixs[0][x][y] == "b":                 #Falls der Pfeil welcher zurzeit angeschaut wird schwarz ist, wird er gemäss der Richtung in welche er zeigt, richtig zugeordnet. Nachdem der richtige Pfeil im String format gefunden wurde, ersetzt dieser den dazu gehörigen Platz in der "matrixs_print" Liste. 
                if matrixs[1][x][y] == "1":
                    matrixs_print[x][y] = "↑"
                if matrixs[1][x][y] == "2":
                    matrixs_print[x][y] = "↗"
                if matrixs[1][x][y] == "3":
                    matrixs_print[x][y] = "→"
                if matrixs[1][x][y] == "4":
                    matrixs_print[x][y] = "↘"
                if matrixs[1][x][y] == "5":
                    matrixs_print[x][y] = "↓"
                if matrixs[1][x][y] == "6":
                    matrixs_print[x][y] = "↙"
                if matrixs[1][x][y] == "7":
                    matrixs_print[x][y] = "←"
                if matrixs[1][x][y] == "8":
                    matrixs_print[x][y] = "↖"
                    
            if matrixs[0][x][y] == "w":                 #Das genau gleiche vorgehen nur falls der Pfeil weiss
                if matrixs[1][x][y] == "1":             #Kommentar: Wir haben den Support für graue Pfeile nicht eingefügt, da graue Pfeile nur beim Debuggen wichtig sind und wir fürs debuggen eine andere einfacherere Möglichkeit den Zustand der Matrix zu überprüfen. Diese Funktion ist ganz unten als Kommentar zu finden. 
                    matrixs_print[x][y] = "⇑"
                if matrixs[1][x][y] == "2":
                    matrixs_print[x][y] = "⇗"
                if matrixs[1][x][y] == "3":
                    matrixs_print[x][y] = "⇒"
                if matrixs[1][x][y] == "4":
                    matrixs_print[x][y] = "⇘"
                if matrixs[1][x][y] == "5":
                    matrixs_print[x][y] = "⇓"
                if matrixs[1][x][y] == "6":
                    matrixs_print[x][y] = "⇙"
                if matrixs[1][x][y] == "7":
                    matrixs_print[x][y] = "⇐"
                if matrixs[1][x][y] == "8":
                    matrixs_print[x][y] = "⇖"          

def print_matrix(m):                                    #Diese funktion printet die "übersetzte" Matrix/Liste "matrixs_print". Der Parameter "m" steht hierbei für die leere Liste "matrixs_print" weclche mit den richtigen Pfeilen gefüllt wird.
    arrow_print_setup()                                 #Ruft die vorherige Funktion auf um die übersetztug zu machen.
    s = ""                                              #Ein leerer String welche später mit den Pfeilen gefüllt wird
    for i in range(0,matrix_grösse + 1):                #wird benutzt um jede Zeile der Matrix durchzugehen
        for j in m[i]:                                  #"j" steht hier immer für einen Pfeil aus einer Zeile. 
            s += str(j) + " "                           #Hier hängen wir "j" an den String "s" an. Somit erhalten wir einen String welcher aus allen Pfeilen in richtiger Reihenfolge besteht
        s += "\n"                                       #Nachdem wir eine ganze Zeile abgegangen sind, fügen wir "\n" beim String hinzu um einen Zeilenumbruch zu erschaffen.
    print("\nEs dauerte:", str(datetime.now() - starttime)[6:],"sekunden \n")         #Dieser Print Befehl gibt heraus wie lange der Code benötigt hat um uns das Resultat zu liefern.
    print(s)                                            #Nun zu guter Letzt, können wir die fertige Matrix ausgeben.

def check_for_user_error():                 # In dieser Funktion überprüfen wir ob es Fehler in der Struktur der Matrix gibt
    n = 1                                   # Zählvariabel um beim Fehler finden zu helfen, gibt an in welcher Zeile der Fehler passiert ist, falls ein Fehler gefunden wird
    for x in richtung:                      # Wir gehen jede Zeile der Matrix durch    x ---> Zeile
        if len(x) != matrix_grösse + 1:     # Falls die Anzahl der Elemente (=Pfeile) in einer Zeile nicht gleich der Grösse der Matrix ist, stimmt etwas nicht. 
            print("Die Anzahl Elemente in einer Zeile stimmt nicht mit der Grösse der Matrix über ein!")
            print("Angegebene Matrix Grösse:", matrix_grösse + 1)           #Wir teilen dem Benutzer mit welche Grösse der Matrix er angegeben hat
            print("Anzahl Elemente in der Zeile", str(n),": ", len(x))      #Wir teilen dem Benutzer mit in welcher Zeile der Fehler passiert ist
            return                                                          #Kommentar: Dies müssen wir nur für die Richtungs-Matrix machen da die Farb-Matrix in Abhängigkeit zur angegebenen Matrixgrösse erstellt wird
        n += 1                                                              
    if len(richtung) != matrix_grösse + 1:              #Hier überprüfen wir ob die Anzahl Zeilen zur Matrixgrösse passt
        print("Die Anzahl Zeilen stimmt nicht mit der Grösse der Matrix über ein!")
        print("Angegebene Matrix Grösse:", matrix_grösse + 1)
        print("Anzahl Zeilen in der Richtungs-Matrix:", len(richtung))
    else:
        Regel1()                        #Keine Fehler wurden gefunden, die Funktion "Regel1" wird aufgerufen und das Lösen des Rätsels beginnt.

check_for_user_error()                  #Wir rufen die Funktion auf um nach Benutzerfehlern zu suchen     

#------------Alles ab hier ist alt und wird nicht mehr benutzt--------------------
#-------------------für den Notfall ist es jedoch da------------------------------
'''
To-Do:
finaly done

def Regel2():
    for y in range(0, matrix_grösse + 1):
        black_seen = 0
        for x in range(0, matrix_grösse + 1):
            #debug1 = input()
            n = 0
            black_seen = 0
            richtung = int(matrixs[1][y][x])
            while n < matrix_grösse + 1:                                         #In dieser Schleife gehen wir in eine Richtung und zählen wie viele Schwarze Pfeile wir sehen                
                n += 1                                                           #Zählvariable um in die Richtung n-mal zu gehen    
                if movingUp_Down[richtung - 1](0,x,y,n) == "b":
                    black_seen += 1 
                elif  movingUp_Down[richtung - 1](1,x,y,n) == False:
                    k = n - 1
                    n = 100
                    if black_seen == 1:
                        while k > 0:
                            toBeColored = movingUp_Down[richtung - 1](0,x,y,k,True)
                            if movingUp_Down[richtung - 1](0,x,y,k) == "g":
                                color("w", toBeColored[0], toBeColored[1])
                            k -= 1
    Regel3()


def print_in_str(q):                            # Wird für das Debugen benutzt um die Matrizen Farbe oder Richtung auszugeben, q gibt an welche von den beiden Matrizen angesprochen wird
    s = ""                                      # Ein leerer String welcher mit allen Pfeilen gefüllt wird und dann "geprinted"                   
    for n in range(0,matrix_grösse+1):          # Geht durch alle Zeilen in der Matrix durch, matrix_grösse plus eins passt es immer auf die Richtige grösse an
        for j in matrixs[q][n]:                 # Geht durch alle Ellemente in einer Zeile der Matrix
            s += str(j) + " "                   # Jedes Element wird an den String hinzugefügt
        s += "\n"                               # Am Ende jeder Zeile fügen wir "\n" hinzu für einen Zeilenumbruch
    return s
'''