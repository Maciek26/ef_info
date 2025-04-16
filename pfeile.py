farbe = [["g","g","g","g","g","g"],["g","g","g","g","g","g"],["g","g","g","g","g","g"],["g","g","g","g","g","g"],["g","g","g","g","g","g"],["g","g","g","g","g","g"]]
#farbe = [["w","w","w","w","w","w"],["w","w","w","w","w","w"],["w","w","w","w","w","w"],["w","w","w","w","w","w"],["w","w","w","w","w","w"],["w","w","w","w","w","w"]]
richtung = [["4","6","4","4","6","6"],["5","4","3","4","8","8"],["5","1","4","5","7","6"],["1","6","5","6","6","8"],["3","5","2","7","7","5"],["2","2","1","3","3","1"]]
#Richtungen von der Aufgabe Nr. 1 6x6 Matrix

matrixs = [farbe, richtung]

matrix_grösse = len(farbe) - 1          #Bei einer 6x6 Matrix = 5 weil computer bei 0 anfängt zu zählen

#Richtungen:
# 1 - Up
# 2 - Up-right
# 3 - Right
# 4 - Down-right
# 5 - Down
# 6 - Down-left
# 7 - Left
# 8 - Up-left

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

def pos_up_right(q,x,y,n,rtn_str=False):
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
    
def pos_right(q,x,y,n,rtn_str=False):
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

def pos_down_right(q,x,y,n,rtn_str=False):
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

def pos_down(q,x,y,n,rtn_str=False):
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

def pos_down_left(q,x,y,n,rtn_str=False):
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
    
def pos_left(q,x,y,n,rtn_str=False):
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
    
def pos_up_left(q,x,y,n,rtn_str=False):
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
            
#Eine Liste mit allen Richtungen, auf dieser Liste basieren die Richtungen in der Liste "Richtung"
#Der Name ist bezogen auf das Lied "I'm moving up and down like a rolercoaster"
movingUp_Down = [pos_up, pos_up_right, pos_right, pos_down_right, pos_down, pos_down_left,pos_left,pos_up_left]

def color(c,x,y):               # Mit dieser Funktion färben wir die Felder ein, c sagt uns in welcher Farbe wir das Feld einfärben sollen
    if c == "b":
        matrixs[0][y][x] = "b"  # Hier benötigen wir die Variable "q" nicht um uns zu sagen welche Matrix angesprochen wird (Farb- oder Richtungsmatrix) da wir ja natürlich die Farbe verändern
    if c == "w":
        matrixs[0][y][x] = "w"

def print_in_str(q):                            # Wird für das Debugen benutzt um die Matrizen Farbe oder Richtung auszugeben, q gibt an welche von den beiden Matrizen angesprochen wird
    s = ""                                      # Ein leerer String welcher mit allen Pfeilen gefüllt wird und dann "geprinted"                   
    for n in range(0,matrix_grösse+1):          # Geht durch alle Zeilen in der Matrix durch, matrix_grösse plus eins passt es immer auf die Richtige grösse an
        for j in matrixs[q][n]:                 # Geht durch alle Ellemente in einer Zeile der Matrix
            s += str(j) + " "                   # Jedes Element wird an den String hinzugefügt
        s += "\n"                               # Am Ende jeder Zeile fügen wir "\n" hinzu für einen Zeilenumbruch
    return s

def Regel3():                   # Unsere 3te Regel bassiert auf dem ausschliessen, hier überprüfen wir wie viele Unbekannte ("g") wir haben. Falls dann ein Pfeil nur einen Unbekannten und keinen schwarzen sieht, muss dieser Unbekannte ein schwarzer Pfeil sein. Das Gleiche gilt aber auch anders herum, falls ein Pfeil einen schwarzen Pfeil bereits sieht, sind alle anderen gesehenen Pfeile weiss ("w") --> ist das gleiche wie Regel 2, wird hier jedoch wiederhollt um das Skript zu beschleunigen.
    grey_count = 0              # Zählvariabel für wie viele graue (Unbekannte) Pfeile wir gesehen haben               
    w = 0                       # Zählvariabel damit das gesamte Skript zwei mal wiederholt wird.                
    while w < 2:                
        w += 1                  # Zählvariabel vergrössern
        for y in range(0, matrix_grösse + 1):           # Geht alle Zeilen der Matrix durch 
            for x in range(0, matrix_grösse + 1):       # Geht alle Spalten der Matrix durch 
                if matrixs[0][y][x] == "g":             # Durch die Kombination der vorherigen beiden "for" loops, wird hier jedes Element der Matrix kontrolliert auf dessen Inhalt. Falls es "g" (Grau/Unbekannt) ist,
                    grey_count += 1                     # Die Zählvariable "grey_count" wird erhöht
                n = 0                                   # Zählvariable um mitzuzählen wie oft wir die folgende While Schleife wiederholt haben
                black_seen = 0
                grey_seen = []
                richtung = int(matrixs[1][y][x]) - 1    # Wir speichern die Richtung ab in welcher der zurzeit gewählte Pfeil zeigt (man muss minus eins rechnen da die Liste bei 0 beginnt zu zählen, könnte verhindert werden in dem ein decoy Element am Anfang eingefügt wird)
                while n < matrix_grösse + 1:                                        #In dieser Schleife gehen wir in eine Richtung und zählen wie viele Schwarze und Grau Pfeile wir sehen, wird maximal so oft wiederholt wie die Matrix gross ist, auch hier hätte es "while True" sein können, da es durch "if statements" unterbrochen wird. Aus redudanz und zur vermeitung endless-loops nicht "while True" 
                    n += 1                                                          #Zählvariable n erhöhen
                    if movingUp_Down[richtung](0,x,y,n) == "b":                     #In der Liste "movingUp_Down" wählen wir die Richtung in welche wir uns bewegen wollen, in diese Richtung Bewegen wir uns dann entsprechend oft zu welcher durchgang es der Schleife ist (wird in "n" gespeichert)
                        black_seen += 1                                             #Zählvariable wird um eins erhöht
                    elif movingUp_Down[richtung](0,x,y,n) == "g":                   
                        grey_seen.append(movingUp_Down[richtung](0,x,y,n, True))
                    elif  movingUp_Down[richtung](1,x,y,n) == False:             #Falls "False" dann ist er am Rand angekommen
                        if len(grey_seen) == 1 and black_seen == 0:                  #Falls ein Pfeil nur einen Unbekannten sieht und keinen Schwarzen, dann wird dieser Unbekannte Pfeil schwarz
                            color("b", grey_seen[0][0], grey_seen[0][1])                
                        elif len(grey_seen) == 1 and black_seen == 1:
                            color("w", grey_seen[0][0],grey_seen[0][1])
    if grey_count == 0:
        return
    else:
        Regel2()
             
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

def Regel1():
    currentTry = True
    for y in range(0, matrix_grösse+1):
        for x in range(0, matrix_grösse+1):
            richtung = int(matrixs[1][y][x])
            if movingUp_Down[richtung - 1](0,x,y,2) == False:
                toBeColored = movingUp_Down[richtung - 1](0,x,y,1,True)
                #print(toBeColored[0], toBeColored[1], "diese wird angemalt")

                color("b", toBeColored[0], toBeColored[1])
                #print(f"Der sieht nh schwarzen von {x} / {y}")$
    Regel2()
            
matrixs_print = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]

def arrow_print_setup(x,y):
    if matrixs[0][x][y] == "b":
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
            
    if matrixs[0][x][y] == "w":
        if matrixs[1][x][y] == "1":
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
        
    return matrixs_print             

def print_matrix(m):
    s = ""
    for i in range(0,6):
        for j in m[i]:
            s += str(j) +" " 
        s += "\n"
    print(s)

Regel1()

def transformIntoArrows():
    for i in range(0,6):
        for j in range(0,6):
            arrow_print_setup(j,i)

transformIntoArrows()           

print_matrix(matrixs_print)