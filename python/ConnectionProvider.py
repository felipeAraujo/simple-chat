# -*- coding: UTF-8 -*-

import socket
import threading;

class ConnectionProvider(object):
    def __init__(self, destination_ip = '', server_port=20001, client_port = 20002):
        self._destination_ip = destination_ip
        self._server_port = server_port
        self._client_port = client_port
        self._buffer_size = 1024;
        self._socket_connected = None
        self._connection_activated = False

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

            self._connection_activated = True

            self._socket_connected = conn
            self._destination_ip, self._client_port = addr

            print('Connection Stablished with ' + self._destination_ip)

            self._server_socket.close()

            t = threading.Thread(target = self._waiting_for_the_data)
            t.daemon = True
            t.start()

    def start_connection(self):
        if not hasattr(self, '_client_socket'):
            self._client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            self._client_socket.bind(('', self._client_port))

            self._client_socket.connect((self._destination_ip, self._server_port))
            self._socket_connected = self._client_socket
            self._connection_activated = True

            t = threading.Thread(target = self._waiting_for_the_data)
            t.daemon = True
            t.start()

    def send_message(self, message):
        if self._connection_activated:
            if type(message) == str:
                message = message.encode()

            self._socket_connected.sendall(message)

    def close_connection(self):
        if self._connection_activated:
            self._connection_activated = False
            self._socket_connected.close()

    def _waiting_for_the_data(self):
        while self._connection_activated:
            data = self._socket_connected.recv(self._buffer_size)
            if not data:
                break
            print("received data:"+data.decode())
