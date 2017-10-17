# -*- coding: UTF-8 -*-

import unittest
from ConnectionProvider import ConnectionProvider

class ConnectionTester(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()
