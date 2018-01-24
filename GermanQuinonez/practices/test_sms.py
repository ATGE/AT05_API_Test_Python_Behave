import unittest
from datetime import datetime

from sms import SMS_store


class TestSMS_Store(unittest.TestCase):
    def setUp(self):
        self.my_inbox = SMS_store()
        self.time = datetime.now().strftime('%H:%M:%S')
        self.my_inbox.add_new_arrival('123456', self.time, 'hi')
        self.my_inbox.add_new_arrival('123456', self.time, 'hi')
        self.my_inbox.add_new_arrival('123456', self.time, 'hi')

    def test_add_new_arrival_with_3_sms(self):
        self.assertEqual(self.my_inbox.message_count(), 3)

    def test_get_unread_indexes(self):
        self.assertEqual(self.my_inbox.get_unread_indexes(), [0, 1, 2])

    def test_get_message(self):
        self.assertEqual(self.my_inbox.get_message(1), ('123456', self.time, 'hi'))

    def test_get_delete(self):
        self.my_inbox.delete(0)
        self.assertEqual(self.my_inbox.message_count(), 2)

    def test_get_clear(self):
        self.my_inbox.clear()
        self.assertEqual(self.my_inbox.message_count(), 0)
