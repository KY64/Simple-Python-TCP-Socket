import socket, threading, json

threads = []
primeNumbers = []
connections = []
address = []
count = 0

def checkPrimary(num):
    global primeNumbers
    # Boolean untuk mengecek bilangan primer
    isPrimary = True

    # Validasi bilangan primer dengan membagi input dengan n
    for x in range(2, num):
        # Jika dapat dibagi dengan selain bilangan itu sendiri, maka bukan bilangan primer
        if(num % x == 0):
            isPrimary = False
    if(isPrimary):
        # Memasukkan bilangan primer ke dalam array
        primeNumbers.append(num)


def dataHandler(clients):
    global primeNumbers, connections, address

    try:

        while True:
            data = json.loads(connections[clients].recv(4096))
            print("Received %s\n\n" % data)
            if data:
                for loop in range(len(data)):
                    checkPrimary(data[loop])
                data = json.dumps(primeNumbers)
                print("Sending back ", data, " to the client ", address[clients])
                connections[clients].sendall(data.encode('utf-8'))
                primeNumbers = []

            else:
                print("\n\n=====no more data from",
                    address[clients], "=====\n\n")
                break
        
    except json.JSONDecodeError:
        print("\n")

    finally:
        connections[clients].close()

def createSocket():
    global client, sock, server_address, connections
    # for c in connections:
    #     print("halo")
    #     c.close()

    # del connections[:]
    # del address[:]

    # Menggunakan TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Memasang server pada localhost port 1000
    server_address = ('localhost', 1000)
    print("Starting up on %s port %s" % server_address)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(server_address)

    sock.listen(client)

    print("Waiting for connection\n")

def listener():
    global sock, connection, client_address, connections, address, count, clientThread
    sock.setblocking(True)    
    connection, client_address = sock.accept()
    connections.append(connection)
    address.append(client_address)
    print("Connection from client with address:", address[count], "\n\n")

    clientThread = threading.Thread(target=dataHandler, args=(count,))
    threads.append(clientThread)
    count = count + 1

def init():
    createSocket()
    listener()

client = input("How many clients? ")
client = int(client)

for loop in range(client):
    # init()
    serverThread = threading.Thread(target=init)
    serverThread.start()
    serverThread.join()

clientThread.start()
clientThread.join()