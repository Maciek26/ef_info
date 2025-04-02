farbe = [["w","w","w","w","w","w"],["w","w","w","w","w","w"],["w","w","w","w","w","w"],["w","w","w","w","w","w"],["w","w","w","w","w","w"],["w","w","w","w","w","w"]]
richtung = [["4","6","4","4","6","6"],["5","4","3","4","8","8"],["5","1","4","5","7","6"],["1","6","5","6","6","8"],["4","5","2","7","7","5"],["2","2","1","3","3","1"]]
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
    a = 0                  #x = x-Achse; y = y-Achse; q = ob die Farbe oder Richtung angesprochen wird
    while a < n:
        a += 1
        if y > 0 or a == n:                #überprüfen ob wir nicht bereits ganz oben sind
            y -= 1
        else:
            return False
        if a == n:
            if rtn_str == True:
                return x,y
            else:
                return matrixs[q][y][x]

                    
        
    

def pos_up_right(q,x,y,n,rtn_str=False):
    a = 0               
    while a < n:
        a += 1
        if y <= 0 or x >= matrix_grösse:                       
            return False   
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
        if x < matrix_grösse:                
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
        if x > 0 or a == n:                
            x -= 1
        else:
            return False
        if a == n:
            if rtn_str == True:
                return x,y
            else:
                return matrixs[q][y][x]
    
def pos_up_left(q,x,y,n,rtn_str=False):
    print("received")
    a = 0               
    while a < n:
        a += 1
        print(x)
        print(y)
        print(y<=0)
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

movingUp_Down = [pos_up, pos_up_right, pos_right, pos_down_right, pos_down, pos_down_left,pos_left,pos_up_left]

def color(c,x,y):
    if c == "b":
        matrixs[0][y][x] = "b"
    if c == "w":
        matrixs[0][y][x] = "w"
    if c == "g":
        matrixs[0][y][x] = "g"



def print_in_str(q):
    s = ""
    i = 0
    for n in range(0,5):
        for j in matrixs[q][n]:
            s += str(j) + " "
            i+= 1
        s += "\n"
    return s
        


def Regel1():
    currentTry = True
    for y in range(0, matrix_grösse+1):
        for x in range(0, matrix_grösse+1):
            richtung = int(matrixs[1][y][x])
            print(x,y)
            print(richtung)
            if movingUp_Down[richtung - 1](0,x,y,2) == False:
                toBeColored = movingUp_Down[richtung - 1](0,x,y,1,True)
                print(toBeColored[0])

                color("b", toBeColored[0],toBeColored[1])
                print(f"Der sieht nh schwarzen von {x} / {y}")
            
            matrixs[1][y][x]



Regel1()
#print(str(farbe[0][0]))
print("\u21E8")
print(print_in_str(0))







