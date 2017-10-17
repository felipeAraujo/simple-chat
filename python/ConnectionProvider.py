# -*- coding: UTF-8 -*-

import socket
import threading

import SystemHelpers

class ConnectionProvider(object):
    def __init__(self, destination_ip = '', server_port=20001, client_port = 20002):
        self._destination_ip = destination_ip
        self._server_port = server_port
        self._client_port = client_port
        self._buffer_size = 1024;
        self._connected_socket = None
        self._function_when_receive_message = print
        self._function_to_alert_user = print

    def set_client_port(self, port):
        self._client_port = port

    def set_server_port(self, port):
        self._server_port = port

    def set_destination_ip(self, ip):
        self._destination_ip = ip

    def get_connected_socket(self):
        return self._connected_socket

    def set_function_when_receive_message(self, function):
        self._function_when_receive_message = function

    def set_function_to_alert_user(self, function):
        self._function_to_alert_user = function

    def connected(self):
        if not self._connected_socket:
            return False

        return True

    def start_server_mode(self):
        t = threading.Thread(target = self._waiting_for_connection)
        t.daemon = True
        t.start()

    def start_connection(self):
        if (not hasattr(self, '_client_socket')) or (not self.connected()) :
            self._client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            self._client_socket.bind(('', self._client_port))

            connection_stablished = True

            try:
                self._client_socket.connect((self._destination_ip, self._server_port))
                self._connected_socket = self._client_socket
                self._waiting_for_the_data()
            except ConnectionRefusedError:
                connection_stablished = False
                message = 'Connection Refused at ' + self._destination_ip +\
                    ':' + str(self._server_port)

                if self._function_to_alert_user:
                    self._function_to_alert_user(message)
                SystemHelpers.log_info(message)
            except Exception as e:
                connection_stablished = False
                message = str(e)
                SystemHelpers.log_debug(message)

            if not connection_stablished:
                self._client_socket.close()
                self._connected_socket = None

            return connection_stablished

        return False

    def send_message(self, message):
        if not self._connected_socket:
            return False

        if type(message) == bytes:
            message = message.decode()

        if type(message) == str:
            message = "message:"+message
            message = message.encode()

        self._connected_socket.sendall(message)

    def close_connection(self):
        if self._connection_activated:
            self._connection_activated = False
            self._connected_socket.close()

    def _waiting_for_connection(self):
        if not hasattr(self, '_server_socket'):
            self._server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._server_socket.bind(('', self._server_port))
            self._server_socket.listen(1)

            conn, addr = self._server_socket.accept()

            self._connected_socket = conn
            self._destination_ip, self._client_port = addr

            self._server_socket.close()

            self._waiting_for_the_data()

    def _waiting_for_the_data(self):
        t = threading.Thread(target = self._waiting_for_the_data_function)
        t.daemon = True
        t.start()

    def _waiting_for_the_data_function(self):
        while self._connected_socket:
            data = self._connected_socket.recv(self._buffer_size)

            if not data:
                self._connected_socket = None
                return

            if self._function_when_receive_message:
                self._function_when_receive_message("received data:"+data.decode())
