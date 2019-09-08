import socket, threading, json

threads = []

def checkPrimary(num):
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


def handler(connection, client_address):
    try:

        while True:
            data = json.loads(connection.recv(4096))
            print("Received %s\n\n" % data)
            if data:
                for loop in range(len(data)):
                    checkPrimary(data[loop])
                data = json.dumps(primeNumbers)
                print("Sending back ", data, " to the client ", client_address)
                connection.sendall(data.encode('utf-8'))

            else:
                print("\n\n=====no more data from",
                      client_address, "=====\n\n")
                break

    except json.JSONDecodeError:
        print("\n")

    finally:
        connection.close()


# Menggunakan TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Memasang server pada localhost port 1000
server_address = ('localhost', 1000)
print("Starting up on %s port %s" % server_address)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(server_address)

client = input("How many clients? ")
client = int(client)

sock.listen(client)

print("Waiting for connection\n")

for loop in range(client):
    primeNumbers = []
    connection, client_address = sock.accept()
    print("Connection from client",loop+1,"with address:", client_address, "\n\n")
    clientThread = threading.Thread(target=handler, args=(connection,client_address))
    threads.append(clientThread)
    clientThread.start()
    clientThread.join()
