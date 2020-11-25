import socket, sys, time

def commands(s):
    while(True):
        try:
            print('''

                Type any command.
                Exit from the server and the program pressing "ctrl + c"

                ''')
            command = input("\n--> ")
            s.send(command.encode())
            data = s.recv(1048000)
            print(str(data, "utf-8"))
            continue    
        except KeyboardInterrupt:
            print("quitting from the server...")
            s.close()
            time.sleep(4)
            sys.exit(0)

        except UnicodeDecodeError:
            print("WARNING\nThe typed command doesn't support utf-8 encoding, so will be returned the original output form.")
        
            print(data)

            
def connection_to_server(address):
    try:
        s = socket.socket()
        s.connect(address)
        print(f"connection established with the server at the address: {address}")
    except socket.error as error:
        print(f"something went wrong during the connection\n{error}")
        retry = input("retry? Y/N: ")
        if retry == "Y" or retry == "y":
            connection_to_server(address)
        else:
            print("no connection established. quitting...")
            sys.exit(0)
    commands(s)


if __name__ == "__main__":
    
    print("Waiting for a connection...")
    
    connection_to_server(("192.168.1.1", 15000)) # you gotta change this ip if it's different
