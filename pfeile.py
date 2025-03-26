farbe = [["b","test","test","w","b","gs"],["b","gs","test1","w","b","ga"],["b","w","tg","w","b","g"],["b","w","g","w","b","gs"],["b","w","g","w","b","g"],["b","w","g","w","b","g"]]
richtung = [["1","4","6","1","2","3"],["1","4","6","1","2","3"],["1","4","6","1","2","3"],["1","4","6","1","2","3"],["1","4","6","1","2","3"],["1","4","6","1","2","3"]]
matrixs = [farbe, richtung]

matrix_grösse = len(farbe)          #Bei einer 6x6 Matrix logsicher weise = 6


def pos_up(q,x,y):                  #x = x-Achse; y = y-Achse; q = ob die Farbe oder Richtung angesprochen wird
    if y > 0:                       #überprüfen ob wir nicht bereits ganz oben sind
        return matrixs[q][y-1][x]
    else:
        return False

def pos_up_right(q,x,y):
    if y <= 0 or x > matrix_grösse:                       #überprüfen ob wir nicht bereits ganz oben oder am Rand sind
        return False
    else:
        return matrixs[q][y-1][x+1]
    


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
