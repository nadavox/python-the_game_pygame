
def derection():
#PRINT THE derection OF THE GAME
    print("the west derection is: left (<---) = W")
    print("the east derection is: right (--->) = E")
    print("the south derection is: down = S")
    print("the north derection is: up = N")
def Instructions():
#PRINT THE Instructions OF THE GAME
    print ('''commands:
write when the system ask you where you want to go: "W/E/S/N" **write the letter in caps lock ''')
def ShowStatus(currentRoom):
#PRINT THE ROOM NUMBER YOU ARE IN
     print('---------------------------')
     print('You are in room number: ' + str(currentRoom))
def PrintRoom(currentRoom):
#PRINT THE KIND OF THE ROOMS YOU ARE
    if currentRoom==7 or currentRoom==15: 
        print (" _____")
        print ("|     |")
        print ("|  X  |")
        print ("|  x  |")
        print ("|_____|")
    elif currentRoom==11:
        print (" _____")
        print ("|  w  |")
        print ("|  i  |")
        print ("|  n  |")
        print ("|_____|")
    elif currentRoom==1:
        print (" _____")
        print ("|     |")
        print ("|     -")
        print ("|     |")
        print ("|__/__|")
    elif currentRoom==2 or currentRoom==3:
        print (" _____")
        print ("|     |")
        print ("-     -")
        print ("|     |")
        print ("|__/__|")
    elif currentRoom==4:
        print (" _____")
        print ("|     |")
        print ("-     |")
        print ("|     |")
        print ("|__/__|")
    elif currentRoom==5 or currentRoom==10 or currentRoom==14:
        print (" __/__")
        print ("|     |")
        print ("|     -")
        print ("|     |")
        print ("|__/__|")

    elif currentRoom==6 or currentRoom==16:
        print (" __/__")
        print ("|     |")
        print ("-     -")
        print ("|     |")
        print ("|_____|")
    elif currentRoom==8 or currentRoom==12:
        print (" __/__")
        print ("|     |")
        print ("-     -")
        print ("|     |")
        print ("|__/__|")
    elif currentRoom==9 or currentRoom==13 or currentRoom==17:
        print (" __/__")
        print ("|     |")
        print ("-     |")
        print ("|     |")
        print ("|__/__|")
    elif currentRoom==18:
        print (" __/__")
        print ("|     |")
        print ("|     -")
        print ("|     |")
        print ("|_____|")
    elif currentRoom==19 or currentRoom==20:
        print (" _____")
        print ("|     |")
        print ("-     -")
        print ("|     |")
        print ("|_____|")
    elif currentRoom==21:
        print (" __/__")
        print ("|     |")
        print ("-     |")
        print ("|     |")
        print ("|_____|")
def CreateRooms():
#CREAT ALL THE ROOMS IN THE GAME AND THE COOCTION BETWEEN THEM
    rooms = {1 : {'E':2 , 'S':5},
             2 : {'w':1 , 'E':3 , 'S':6},
             3 : {'W':2 , 'E':4 , 'S':8},
             4 : {'W':3 , 'S':9},
             5 : {'N':1 , 'E':6 , 'S':10},
             6 : {'N':2 , 'E':7 , 'W':5},
             7 : {},
             8 : {'W':7 , 'N':3 , 'E':9 , 'S':3},
             9 : {'W':8 , 'N':4 , 'S':13},
             10 : {'N':5 , 'E':11 , 'S':14},
             11 : {},
             12 : {'W':11, 'N':8 , 'E':13 , 'S':16},
             13 : {'W':12 , 'N':9 , 'S':17},
             14 : {'E':15 , 'N':10 , 'S':18},
             15 : {},
             16 : {'W':15 , 'E':17},
             17 : {'N':13 , 'W':16 , 'S':21},
             18 : {'N':14 , 'E':19},
             19 : {'W':18 , 'E':20},
             20 : {'W':19 , 'E':21},
             21 : {'W':20 , 'N':17}}
    return rooms
def ChooseRoom(rooms, currentRoom):
#MAKE YOU MOVE TO THE ROOM YOU WANT TO
    NextRoom=input("write a way: ") 
    while not NextRoom in rooms[currentRoom]:
         print ("choose another way, there is no way where you choose")
         NextRoom=input("write a way: ")
    x = rooms[currentRoom][NextRoom]
    return x
def main():
# THE MAIN POGRAM
    #CREAT THE ROOMS
    rooms = CreateRooms()
    Instructions()
    derection()
    #INFINTY LOOP OF THE GAME UNTIL OVER
    while True:
        #START THE GAME FROM ROOM NUMBER 1, THE VERIBAL REPRESENT WHERE YOU ARE
        currentRoom = 1
        #SHOW FOR THE FIRST TIME WHERE YOU ARE, IN ROOM NUMBER 1
        ShowStatus(currentRoom)
        #LOOP THAT SAY PLEASE PLAY UNTIL YOU ENTER THE WRONG ROOM OR THE WINNING ROOM
        while currentRoom != 7 and currentRoom != 11 and currentRoom != 15: 
            PrintRoom(currentRoom)
            currentRoom = ChooseRoom(rooms, currentRoom)
            ShowStatus(currentRoom)
        
        
        # CHACK IF YOU ENTER TO THE WRONG ROOM
        if currentRoom == 7 or currentRoom == 15: 
            PrintRoom(currentRoom)
            print ("GAME OVER")
        else:
            #IF YOU DONT IN THE WRONG ROOMS IT MEANS YOU ARE IN THE WINNING ROOM
            PrintRoom(currentRoom) 
            print("W-I-N")
        #ASK THE USER IF HE WANT TO PLAY ONE MORE
        AnotherGame = int(input("do you want play one more? (write 1 to contineu or 2 to exit ")) 
        # IF HE DIECIDE TO EXIT SO THE POGRAM WILL BE STOP
        if AnotherGame == 2: 
           exit(1)
        #IF HE DIECIDE TO CONTINUE WE START FROM ROOM NUMBER 1 
        elif AnotherGame == 1: 
           currentRoom =1



main() 

        
