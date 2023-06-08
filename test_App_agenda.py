#!/usr/bin/python3
import sqlite3
from  Contacte import Contacte
from Persistencia_contacte_sqlite import Persistencia_contacte_sqlite
from Persistencia_adreca_sqlite import Persistencia_adreca_sqlite

RUTA_DB_TEST = "test_db.db"
class Test_App_agenda():

    def drop_table_contactes(self):
        conn = sqlite3.connect(RUTA_DB_TEST)
        consulta = "DROP TABLE IF EXISTS adreces;"
        cursor = conn.cursor()
        cursor.execute(consulta)
        cursor.close()
        consulta = "DROP TABLE IF EXISTS contactes;"
        cursor = conn.cursor()
        cursor.execute(consulta)
        conn.commit()
        cursor.close()
        conn.close()

    def llegeix_contactes(self):
        conn = sqlite3.connect(RUTA_DB_TEST)
        consulta = "SELECT * FROM contactes;"
        cursor = conn.cursor()
        cursor.execute(consulta)
        n = len(cursor.fetchall())
        cursor.close()
        conn.close()
        return n
    
    def test_afegir_contacte(self):
        self.drop_table_contactes()
        per_contacte = Persistencia_contacte_sqlite(RUTA_DB_TEST)
        per_adreca = Persistencia_adreca_sqlite(RUTA_DB_TEST)
        un_contacte = Contacte("Josep", 
                               "Martínez Bordiu", 
                               "555-66-77", 
                               "jsp@mail.com", 
                               "Sol", 
                               "2", 
                               "3r", 
                               "1a", 
                               per_contacte, 
                               per_adreca)
        un_contacte.desa()
        assert self.llegeix_contactes() > 0
        assert True
