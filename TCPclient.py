import socket, json, random


def randNumber():
    for client in range(20):
        num = random.randint(1,100)
        numbers.append(num)

client = input("How many data? ")
client = int(client)

#Menggunakan TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Menghubungkan ke server
server_address = ('localhost', 1000)

print("Connecting to %s port %s" % server_address)
sock.connect(server_address)

for loop in range(client):
        numbers = []
        randNumber()

        try:
                numbers.sort()
                numbers = json.dumps(numbers)
                print("Sending %s" % numbers)
                # print("Sending HAI")
                sock.sendall(numbers.encode('utf-8'))
                # sock.sendall(b"HAI")
                
                data = json.loads(sock.recv(4096))
                # data = sock.recv(4096)
                print("Received %s" %data)

        except socket.error:
                print("\n\n")

print("Closing socket")
sock.close()
