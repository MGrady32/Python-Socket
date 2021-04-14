import socket

HEADER = 64
PORT = 3310
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "disconnect"
SERVER = "192.168.0.47"
ADDR = (SERVER, PORT)
MESSAGE = ' '

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048))


while True:
    MESSAGE = input()
    if (MESSAGE != DISCONNECT_MESSAGE):
        send(MESSAGE)
    elif (MESSAGE == DISCONNECT_MESSAGE):
        send(DISCONNECT_MESSAGE)
        break


#send(input())
#input()
#send(DISCONNECT_MESSAGE)