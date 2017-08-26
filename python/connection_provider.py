# -*- coding: UTF-8 -*-

import socket

class Connection_Provider(object):
    def __init__(self, destination_ip = '', server_port=20001, client_port = 20002):
        self._destination_ip = destination_ip
        self._server_port = server_port
        self._client_port = client_port
        self._buffer_size = 1024;
        self._socket_connected = None

    def set_client_port(self, port):
        self._client_port = port

    def set_server_port(self, port):
        self._server_port = port

    def set_destination_ip(self, ip):
        self._destination_ip = ip

    def get_socket_connected(self):
        return self._socket_connected


    def start_server_mode(self):
        if not hasattr(self, '_server_socket'):
            self._server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._server_socket.bind(('', self._server_port))
            self._server_socket.listen(1)

            conn, addr = self._server_socket.accept()

            self._socket_connected = conn
            self._destination_ip, self._client_port = addr

            self._server_socket.close()

            self._waiting_for_the_data()

    def start_connection(self):
        if not hasattr(self, '_client_socket'):
            self._client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            self._client_socket.bind(('', self._client_port))

            print(self._destination_ip)
            self._client_socket.connect((self._destination_ip, self._server_port))
            self._socket_connected = self._client_socket

    def send_message(self, message):
        if type(message) == str:
            message = message.encode()

        self._socket_connected.sendall(message)

    def _waiting_for_the_data(self):
        while 1:
            data = self._socket_connected.recv(self._buffer_size)
            if not data:
                break
            print("received data:"+data.decode())

        self._socket_connected.close()
