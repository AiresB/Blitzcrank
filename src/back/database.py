import psycopg2

class Database():

    def __init__(self, url) -> None:
        try:
            self.conn = psycopg2.connect(url)
            self.conn.autocommit = True
        except:
            print("Cannot connect to db")


    def __delattr__(self, __name: str) -> None:
        self.conn.close()

    def get_players(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM a_player;")
            res = cur.fetchall()
        return res

    def add_player(self, pseudo, id=0):
        with self.conn.cursor() as cur:
            cur.execute('INSERT INTO a_player (pseudo, id) VALUES(%s,%s)', (pseudo, id))

    def delete_player(self, pseudo):
        with self.conn.cursor() as cur:
            cur.execute('DELETE FROM a_player WHERE pseudo = %s;', (pseudo,))