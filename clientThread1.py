import socket
import json
import pickle

HOST = ''                
PORT = 1398
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

s.connect(('', 1321))

while True:
    
    message = input("Your move: ")
    
    data = [{ 'p1':message }]
    
    #s.send(bytes(data, 'utf-8'))
    s.send(pickle.dumps(data))
    
    print ("Waiting for player 2 to move")
    reply = s.recv(1024)
    replyCheck = pickle.loads(reply)
    print (replyCheck)
    if (replyCheck == "Player 1 won !!" or replyCheck == "Player 2 won !!"):
        break
    
s.close()