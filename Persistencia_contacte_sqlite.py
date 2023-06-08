#!/usr/bin/python3
import sqlite3
from Contacte import Contacte
from Persistencia_adreca_sqlite import Persistencia_adreca_sqlite

class Persistencia_contacte_sqlite():
    def __init__(self, ruta_db):
        self._ruta_db = ruta_db
        conn = self.get_conn()
        conn.close()

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
    
    def get_llista(self):
        resultat = []
        connexio = self.get_conn()
        consulta = f"""SELECT
            nom, cognoms, telefon, email, nom_via, nombre_via, pis, porta
          FROM contactes join adreces 
                    on contactes.rowid = adreces.contacte;"""
        cursor = connexio.cursor()
        cursor.execute(consulta)
        resultat_consulta = cursor.fetchall()
        connexio.commit()
        cursor.close()
        connexio.close()
        for registre in resultat_consulta:
            contacte = Contacte(
                registre[0],
                registre[1],
                registre[2],
                registre[3],
                registre[4],
                registre[5],
                registre[6],
                registre[7],
                self,
                Persistencia_adreca_sqlite(self._ruta_db)
            )
            resultat.append(contacte)
            print(contacte)
        return resultat

