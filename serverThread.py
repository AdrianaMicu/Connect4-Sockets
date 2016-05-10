import socket
import threading
import pickle

HOST = ''                
PORT = 1333          
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

s.listen(5)

r0 = [0, 0, 0, 0, 0, 0, 0]
r1 = [0, 0, 0, 0, 0, 0, 0]
r2 = [0, 0, 0, 0, 0, 0, 0]
r3 = [0, 0, 0, 0, 0, 0, 0]
r4 = [0, 0, 0, 0, 0, 0, 0]
r5 = [0, 0, 0, 0, 0, 0, 0]

game = [r0, r1, r2, r3, r4, r5]
    
def verifyLines(player):
    
    for i in range(0, 5):
        count = 0
        j = 0
        while j <= 6:
            if (game[i][j] != 0) and (game[i][j] == game[i][j + 1]):
                count += 1
                        
                if count == 3:
                    print (player + " won !!") #trimite player ca parametru
                    sendWin = player + " won !!"
                    playerWin = pickle.dumps(sendWin)
                    connections[0].sendall(playerWin)
                    connections[1].sendall(playerWin)
                    break
                            
            j += 1
                        
        i += 1
        
def verifyColumns(player):
    
    for i in range(0, 6):
        count = 0
        j = 0
        while j <= 5:
            #print ("verifica")
            if (game[j][i] != 0) and (game[j][i] == game[j + 1][i]):
                #print ("verifica")
                count += 1
                        
                if count == 3:
                    print (player + " won !!") #trimite player ca parametru
                    sendWin = player + " won !!"
                    playerWin = pickle.dumps(sendWin)
                    connections[0].sendall(playerWin)
                    connections[1].sendall(playerWin)
                    break
                            
            j += 1
                        
        i += 1


connections = []

def ClientThread(conn, port):
    
    connections.append(conn)
    print (connections)
    
    while True:
        
        data = conn.recv(1024)
        
        try:
            dataToArray = pickle.loads(data)
        except:
            connections[0].close()
            connections[1].close()
            s.close()
            break
        
        player = repr(dataToArray)[3] + repr(dataToArray)[4]
        move = repr(dataToArray)[9]
        moveToInt = int(move) - 1
        print (moveToInt)
        
        if player == 'p1':
            print("Player 1")
            player1 = "Player 1"
        
            i = 0
            for i in range(0, 5):
                if game[i][moveToInt] == 0:
                    game[i][moveToInt] = 1
                    break
                else:
                    i += 1
                                
            #gameArray = pickle.dumps(game)
            #connections[1].sendall(gameArray)
            
            j = 5 
            k = 0
            gamePretty = ""
            while j >= 0:
        
                for k in range(0, 6):
                    poz = str(game[j][k])
                    gamePretty += poz + " | "
                    k = k + 1
                
                gamePretty = gamePretty + "\n"
                j = j - 1
                
            print (gamePretty)
            gameArray = pickle.dumps(gamePretty)
            
            verifyLines(player1)
            verifyColumns(player1)

            connections[1].sendall(gameArray)
            #conn.sendto(toSend, (HOST, 1347))
            print("sent")
        elif player == 'p2':
            player2 = "Player 2"
            print("Player 2")
            
            i = 0
            for i in range(0, 5):
                if game[i][moveToInt] == 0:
                    game[i][moveToInt] = 2
                    break
                else:
                    i += 1
                    
            j = 5 
            k = 0
            gamePretty = ""
            while j >= 0:
        
                for k in range(0, 6):
                    poz = str(game[j][k])
                    gamePretty += poz + " | "
                    k = k + 1
                
                gamePretty = gamePretty + "\n"
                j = j - 1
                
            print (gamePretty)
            
            gameArray = pickle.dumps(gamePretty)
            
            verifyLines(player2)
            verifyColumns(player2)
            
            connections[0].sendall(gameArray)


while True:
    
    try:
        conn, addr = s.accept()
        print ("Connected by", addr)
        threading.Thread(target=ClientThread,args=(conn,addr[1],),).start()
    except:
        break
    
#conn.close()
#s.close()