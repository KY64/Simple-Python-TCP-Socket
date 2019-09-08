import socket, json

primeNumbers = []

def checkPrimary(num):
        #Boolean untuk mengecek bilangan primer
        isPrimary = True

        #Validasi bilangan primer dengan membagi input dengan n
        for x in range(2,num):
            #Jika dapat dibagi dengan selain bilangan itu sendiri, maka bukan bilangan primer
            if(num%x == 0):
                isPrimary = False
        if(isPrimary):
            print(num," ",thread)
            #Memasukkan bilangan primer ke dalam array
            primeNumbers.append(num)

#Menggunakan TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Memasang server pada localhost port 1000
server_address = ('localhost', 1000)
print("Starting up on %s port %s" % server_address)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(server_address)

sock.listen(10)

while True:
    print("Waiting for connection")
    connection, client_address = sock.accept()

    try:
        print("Connection from", client_address)

        while True:
            data = json.loads(connection.recv(40960))
            print("Received %s" % data)
            if data:
                data = json.dumps(data)
                print("Sending back %s to the client" % data)
                connection.sendall(data.encode('utf-8'))

            else:
                print("\n\n=====no more data from", client_address,"=====\n\n")
                break
    
    except json.JSONDecodeError:
        print("\n")

    finally:
        connection.close()