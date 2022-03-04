import unittest
import os
import psycopg2
from dotenv import load_dotenv
from urllib.parse import urlparse
from decimal import Decimal

from src.back.database import Database

load_dotenv(dotenv_path="config")

def is_in(player, lst):
    if player in lst:
        return True
    else:
        return False

class TestDatabase(unittest.TestCase):
    url = os.getenv("DATABASE_URL")
    parse_url = urlparse(url)
    db = Database(url)
    lst = []

    ## Connection

    def test_db_connection_1(self):
        self.assertIsInstance(self.db.conn, psycopg2.extensions.connection , msg="Wrong connection type")

    def test_db_connection_2(self):
        self.assertTrue(self.db.conn.autocommit, msg="Wrong autocommit bool type")

    def test_db_connection_3(self):
        self.assertEqual(self.db.conn.get_dsn_parameters()["krbsrvname"] , self.parse_url.scheme,  msg="Wrong name connection")

    def test_db_connection_4(self):
        self.assertEqual(self.db.conn.get_dsn_parameters()["dbname"], self.parse_url.path[1:], msg="Wrong db name")

    def test_db_connection_5(self):
        self.assertEqual(self.db.conn.get_dsn_parameters()["user"], self.parse_url.username, msg="Wrong user name")

    def test_db_connection_6(self):
        self.assertEqual(self.db.conn.get_dsn_parameters()["host"], self.parse_url.hostname, msg="Wrong host name")

    def test_db_connection_7(self):
        self.assertEqual(int(self.db.conn.get_dsn_parameters()["port"]), self.parse_url.port, msg="Wrong port")

    ## DB Modification

    db.add_player("test")
    lst = db.get_players()

    def test_db_get_players_1(self):
        self.assertIsInstance(self.lst, list)

    def test_db_get_player_2(self):
        self.assertGreater(len(self.lst), 0 , msg="No players in list")

    def test_db_add_1(self):
        self.assertTrue(is_in((Decimal('0'), 'test'), self.lst), msg="Test player dont find")

    db.add_player("test", 42)

    def test_db_add_2(self):
        self.lst = self.db.get_players()
        self.assertTrue(is_in((Decimal('42'), 'test'), self.lst), msg="Test player dont find")


    def test_db_remove_1(self):
        self.db.delete_player("test")
        self.lst = self.db.get_players()
        self.assertFalse(is_in((Decimal('0'), 'test'), self.lst), msg="Test player dont removed")

    def test_db_remove_2(self):
        self.assertFalse(is_in((Decimal('42'), 'test'), self.lst), msg="Test player dont removed")
