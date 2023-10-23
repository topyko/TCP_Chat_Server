import socket
import select
from protocol import protocol_write_message,protocol_read_message,SERVER_ADDRESS

def main():
    server=socket.socket()
    server.bind(SERVER_ADDRESS)
    server.listen(5)

    clients=[server]


    while True:
        readabeles, _, _=select.select(clients,[],[],0.2)
        for readabel in readabeles:
            if readabel==server:
                 conn, addr  =   server.accept()
                 print(f'hi new client:{addr}')

                 clients.append(conn)
            else:
                 message =protocol_read_message(readabel)
                 if message in [b'',b'exit']:
                     readabel.shutdown(socket.SHUT_RDWR)
                     readabel.close()
                     client.remove(readabel)
                 for client in clients:
                    if client!=readabel and client!=server:
                        protocol_write_message(client,message)

    client.shutdown(socket.SHUT_RDWR)
    client.close()




if __name__ == '__main__':
    main()
