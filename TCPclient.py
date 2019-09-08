import socket, json, random

numbers = []

#Menggunakan TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Menghubungkan ke server
server_address = ('localhost', 1000)

print("Connecting to %s port %s" % server_address)
sock.connect(server_address)

def randNumber():
    for client in range(20):
        num = random.randint(1,100)
        numbers.append(num)

randNumber()

try:
        numbers = json.dumps(numbers)
        print("Sending %s" % numbers)
        sock.sendall(numbers.encode('utf-8'))

        data = json.loads(sock.recv(40960))
        print("Received %s" %data)

except socket.error:
        print("\n\n")

print("Closing socket")
sock.close()