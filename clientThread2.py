import socket
import json
import pickle

HOST = ''                
PORT = 1332
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

s.connect(('', 1333))

while True:
    
    print ("Waiting for player 1 to move")
    reply = s.recv(1024)
    replyCheck = pickle.loads(reply)
    print (replyCheck)
    if (replyCheck == "Player 1 won !!" or replyCheck == "Player 2 won !!"):
        break
    
    message = input("Your move: ")
    
    data = [{ 'p2':message }]
    
    s.send(pickle.dumps(data))
    
s.close()