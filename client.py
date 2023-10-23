
import socket
import select
import sys
from protocol import SERVER_ADDRESS,protocol_write_message,protocol_read_message

def main():
    client=socket.socket()
    client.connect(SERVER_ADDRESS)
    to_read=[client,sys.stdin]
    cond=False
    while not cond:
        readabeles, _, _=select.select(to_read,[],[],0.2)
        for readabel in readabeles:
            if readabel == client:
                from_server=protocol_read_message(client)
                print(f'from server{from_server}')
            else:
                message=readabel.readline().strip().encode()
                protocol_write_message(client,message)
                if message == b'exit':
                    cond=True
    client.shutdown(socket.SHUT_RDWR)
    client.close()




if __name__ == '__main__':
    main()
