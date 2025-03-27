farbe = [["b","test","test","w","b","gs"],["b","gs","test1","w","b","ga"],["b","w","tg","w","b","g"],["b","w","g","w","b","gs"],["b","w","g","w","b","g"],["b","w","g","w","b","g"]]
richtung = [["1","4","6","1","2","3"],["1","4","6","1","2","3"],["1","4","6","1","2","3"],["1","4","6","1","2","3"],["1","4","6","1","2","3"],["1","4","6","1","2","3"]]
matrixs = [farbe, richtung]

matrix_grösse = len(farbe) - 1          #Bei einer 6x6 Matrix bei 5 weil computer bei 0 anfängt zu zählen
print(matrix_grösse)


#eventuell einbauen dass es anstatt -1 bei x/y ist, dass man noch eine Variable mit schickt welche angibt wie viele stellen man sich bewegen möchte

def pos_up(q,x,y):                  #x = x-Achse; y = y-Achse; q = ob die Farbe oder Richtung angesprochen wird
    if y > 0:                       #überprüfen ob wir nicht bereits ganz oben sind
        return matrixs[q][y-1][x]
    else:
        return False

def pos_up_right(q,x,y):
    if y <= 0 or x >= matrix_grösse:                       #überprüfen ob wir nicht bereits ganz oben oder am Rand sind
        return False
    else:
        return matrixs[q][y-1][x+1]
    
def pos_right(q,x,y):
    if x < matrix_grösse - 1:
        matrixs[q][y][x+1]
    else:
        return False
    
def pos_down_right(q,x,y):
    if y >= matrix_grösse or x >= matrix_grösse:
        return False
    else:
        return matrixs[q][y+1][x+1]

def pos_down(q,x,y):
    if y < 5:
        return matrixs[q][y+1][x]
    else:
        return False

def pos_down_left(q,x,y):
    if y >= matrix_grösse or x <= 0:
        return False
    else:
        return matrixs[q][y+1][x-1]
    
def pos_left(q,x,y):
    if x > 0:
        return matrixs[q][y][x-1]
    else:
        return False
    
def pos_up_left(q,x,y):
    if y <= 0 or x <= 0:
        return False
    else:
        return matrixs[q][y-1][x-1]


def print_in_str(q):
    s = ""
    i = 0
    for n in range(0,5):
        for j in matrixs[q][n]:
            s += str(j) + " "
            i+= 1
        s += "\n"
    return s
        
print(pos_up_right(0,1,2))
#print(str(farbe[0][0]))
#print("\u21E8")
print(print_in_str(0))
