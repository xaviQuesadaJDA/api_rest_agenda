#!/usr/bin/python3
import sqlite3
from Contacte import Contacte
from Persistencia_adreca_sqlite import Persistencia_adreca_sqlite

class Persistencia_contacte_sqlite():
    def __init__(self, ruta_db):
        self._ruta_db = ruta_db

    def get_conn(self):
        conn = sqlite3.connect(self._ruta_db)
        cursor = conn.cursor()
        consulta = "SELECT * FROM contactes;"
        try:
            resultat = cursor.execute(consulta)
        except sqlite3.OperationalError:
            self.genera_taula_contactes(conn)
        return conn
            
    def genera_taula_contactes(self, conn):
        cursor = conn.cursor()
        consulta = """CREATE TABLE if not exists contactes(
            nom TEXT not null,
            cognoms TEXT not null,
            telefon TEXT,
            email TEXT
        );"""
        cursor.execute(consulta)
        conn.commit()
        cursor.close()


    def desa(self, contacte):
        connexio = self.get_conn()
        consulta = f"""INSERT INTO contactes 
            (nom, cognoms, telefon, email) 
            VALUES('{contacte.nom}',
                    '{contacte.cognoms}',
                    '{contacte.telefon}',
                    '{contacte.email}');
        """
        cursor = connexio.cursor()
        cursor.execute(consulta)
        id_contacte = cursor.lastrowid
        connexio.commit()
        cursor.close()
        connexio.close()
        contacte.adreca.desa(id_contacte)

if __name__ == "__main__":
    mi_persistencia = Persistencia_contacte_sqlite("./test_db.db")
    mi_persistencia_adreca = Persistencia_adreca_sqlite("./test_db.db")
    un_contacte = Contacte("Pep", "Bou Company", "555-67-87",
                           "enric@gmail.com", "Pau Claris", "212", "1er", "2a",
                           mi_persistencia, mi_persistencia_adreca)
    un_contacte.desa()
    
