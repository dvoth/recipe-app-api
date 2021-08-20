from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase

class CommandTests(TestCase):

    def test_wait_for_db_ready(self):
        """"Test waiting for db when db is available"""

        # gi will override the __getitem__ function from django
        # This function is what gets database connectivity, so we will override to simulate a successful connection ALWAYS
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)

    # our wait_for_db command we created in management/commands/wait_for_db.py uses time.sleep. This overwrites it so it doesn't actually sleep during tests (that would take forever)
    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        """ Test waiting for db"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            # raises the error 5 times, and on the 6th return True
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)

        