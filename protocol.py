import struct
MESSAGE_FORMAT = struct.Struct('!I')

SERVER_ADDRESS = ('127.0.0.1', 1337)

def protocol_write_message(socket,message):
    message_len=len(message)
    message=MESSAGE_FORMAT.pack(message_len)+message
    socket.sendall(message)
def protocol_read_message(socket):
    meta_data=socket.recv(MESSAGE_FORMAT.size)
    if meta_data == b'':
        return b''
    message_len=MESSAGE_FORMAT.unpack(meta_data)[0]
    message=socket.recv(message_len)
    return message
