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

def pos_up(q,x,y,n,rtn_str=False):
    a = 0                                       #x = x-Achse; y = y-Achse; q = ob die Farbe oder Richtung angesprochen wird
    while a < n:
        a += 1
        if y > 0:                               #überprüfen ob wir nicht bereits ganz oben sind
            y -= 1
        else:
            return False                        #Falls wir am Rand sind, geben wir False zurück
        if a == n:
            if rtn_str == True:                 #Wir gucken ob die Koordinaten benötigt werden
                return x,y
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
        if y >= matrix_grösse or x >= matrix_grösse:                       
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
        if y < matrix_grösse:                
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
        if y >= matrix_grösse or x <= 0:                       
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
        if x > 0:                
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
        if y <= 0 or x <= 0:                       
            return False   
        else:            
            x -= 1
            y -= 1
        if a == n:
            if rtn_str == True:                 #gibt an ob es die Kordinaten schickt oder inhalt
            
                return x,y
            else:
                return matrixs[q][y][x]
            
#Eine Liste mit allen Richtungen, auf dieser Liste basieren die Richtungen in der Liste "Richtung"
#Der Name ist bezogen auf das Lied "I'm moving up and down like a rolercoaster"
movingUp_Down = [pos_up, pos_up_right, pos_right, pos_down_right, pos_down, pos_down_left,pos_left,pos_up_left]

def color(c,x,y):               # Mit dieser Funktion färben wir die Felder ein, c sagt uns in welcher Farbe wir das Feld einfärben sollen
    if c == "b":
        matrixs[0][y][x] = "b"
    if c == "w":
        matrixs[0][y][x] = "w"

def print_in_str(q):            # Wir für das Debugen benutzt um die Matrizen Farbe oder Richtung auszugeben, q gibt an welche von den beiden
    s = ""
    i = 0
    for n in range(0,6):
        for j in matrixs[q][n]:
            s += str(j) + " "
            i+= 1
        s += "\n"
    return s

def Regel3():
    w = 0
    test = 0
    while w < 2:
        w += 1
        print("regel3 begonnen")
        grey_seen = 0
        black_seen = 0
        for y in range(0, matrix_grösse + 1):
            for x in range(0, matrix_grösse + 1):
                n = 0
                black_seen = 0
                grey_seen = []
                richtung = int(matrixs[1][y][x])
                while n < matrix_grösse + 1:                                        #In dieser Schleife gehen wir in eine Richtung und zählen wie viele Schwarze Pfeile wir sehen
                    n += 1                                                          #Zählvariable um in die Richtung n-mal zu gehen
                    if movingUp_Down[richtung - 1](0,x,y,n) == "b":
                        black_seen += 1 
                    elif movingUp_Down[richtung - 1](0,x,y,n) == "g":
                        grey_seen.append(movingUp_Down[richtung - 1](0,x,y,n, True))
                    elif  movingUp_Down[richtung - 1](1,x,y,n) == False:             #Falls False dann ist er am Rand angekommen
                    
                        
                        if len(grey_seen) == 1 and black_seen == 0:                     #Falls ein Pfeil nur einen Unbekannten sieht und keinen Schwarzen
                            color("b", grey_seen[0][0], grey_seen[0][1])                #dann wird dieser Unbekannte Pfeil schwarz
                        
                        elif len(grey_seen) == 1 and black_seen == 1:
                            print("wird weiss eingefärbt")
                            color("w", grey_seen[0][0],grey_seen[0][1])
        
        print("Regel 3 Durchlauf", n)
        print(print_in_str(0))
    

            
def Regel2():
    print("begann to lock for black")
    for y in range(0, matrix_grösse + 1):
        black_seen = 0
        for x in range(0, matrix_grösse + 1):
            #debug1 = input()
            print(print_in_str(0))

            print(x,y)
            n = 0
            black_seen = 0
            richtung = int(matrixs[1][y][x])
            while n < matrix_grösse + 1:                                       #In dieser Schleife gehen wir in eine Richtung und zählen wie viele Schwarze Pfeile wir sehen    
                
                    
                
                
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
    print("Regel 2")
    print(print_in_str(0))
                        
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
    print("Regel 1")
    print(print_in_str(0))
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

def printm(m):
    s = ""
    for i in range(0,6):
        for j in m[i]:
            s += str(j) +" " 
        s += "\n"
    print(s)

Regel1()
Regel2()
Regel2()
#print(str(farbe[0][0]))
print("\u21E8")
def test():
    for i in range(0,6):
        for j in range(0,6):
            arrow_print_setup(j,i)

test()           

printm(matrixs_print)












