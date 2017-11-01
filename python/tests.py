# -*- coding: UTF-8 -*-

import unittest
from unittest.mock import patch
from time import sleep
import os
from pathlib import Path

from ConnectionProvider import ConnectionProvider
import SystemHelpers

class ConnectionTester(unittest.TestCase):
    def setUp(self):
        SystemHelpers.LOG_FILE_DEBUG = 'log_debug_test.txt'
        SystemHelpers.LOG_FILE_INFO = 'log_file_test.txt'
        SystemHelpers.LOG_FILE_WARNING = 'log_warning_test.txt'

    def test_to_return_false_when_no_connection(self):
        client_side = ConnectionProvider()
        client_side.set_function_to_alert_user(None)
        self.assertFalse(
            client_side.start_connection(),
            'Connection was stablished without any connection'
        )

    def test_connected_function(self):
        connection = ConnectionProvider()
        connection.set_function_to_alert_user(None)

        self.assertFalse(
            connection.connected(),
            'Return true to connected() function when connection was stablished'
        )

        connection.start_connection()

        self.assertFalse(
            connection.connected(),
            'Return true to connected() function when connection was stablished'
        )

    def test_that_will_have_socket_timedout(self):
        file_path = Path(SystemHelpers.LOG_FILE_DEBUG)

        if file_path.is_file():
            os.remove(SystemHelpers.LOG_FILE_DEBUG)

        server = ConnectionProvider(timeout=1)
        server.start_server_mode()
        sleep(3)

        log_file = open(SystemHelpers.LOG_FILE_DEBUG, 'r')
        line = log_file.read()
        log_file.close()

        self.assertTrue(
            'Timeout when waiting for the data on server mode' in line,
            'The timeout exception wasn\'t handled')



if __name__ == '__main__':
    unittest.main()
