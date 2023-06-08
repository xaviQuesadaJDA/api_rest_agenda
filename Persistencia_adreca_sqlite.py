#!/usr/bin/python3
import sqlite3

class Persistencia_adreca_sqlite():
    def __init__(self, ruta_db):
        self._ruta_db = ruta_db

    def get_conn(self):
        conn = sqlite3.connect(self._ruta_db)
        cursor = conn.cursor()
        consulta = "SELECT * FROM adreces;"
        try:
            resultat = cursor.execute(consulta)
        except sqlite3.OperationalError:
            self.genera_taula_adreces(conn)
        return conn
            
    def genera_taula_adreces(self, conn):
        cursor = conn.cursor()
        consulta = """CREATE TABLE if not exists adreces(
            contacte int not null,
            nom_via TEXT not null,
            nombre_via TEXT not null,
            pis TEXT not null,
            porta TEXT not null,
            FOREIGN KEY(contacte) REFERENCES contactes(rowid)
        );"""
        cursor.execute(consulta)
        conn.commit()
        cursor.close()


    def desa(self, adreca, contacte_id):
        connexio = self.get_conn()
        consulta = f"""INSERT INTO adreces 
            (contacte, nom_via, nombre_via, pis, porta) 
            VALUES({contacte_id}, 
                    '{adreca.nom_via}',
                    '{adreca.nombre_via}',
                    '{adreca.pis}',
                    '{adreca.porta}');
        """
        cursor = connexio.cursor()
        cursor.execute(consulta)
        connexio.commit()
        cursor.close()
        connexio.close()  
