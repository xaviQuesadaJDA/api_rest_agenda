#!/usr/bin/python3
from Persona import Persona
from Adreca import Adreca
import json

class Contacte(Persona):
    def __init__(self, nom, cognoms, telefon, email, 
                 adreca_nom_via, adreca_nombre_via, 
                 adreca_pis, adreca_porta, persistencia, persistencia_adreca):
        super().__init__(nom, cognoms)
        self._telefon = telefon
        self._email = email
        self._adreca = Adreca(adreca_nom_via, adreca_nombre_via, 
                        adreca_pis, adreca_porta, persistencia_adreca)
        self._persistencia = persistencia

    @property 
    def telefon(self):
        return self._telefon
    
    @property
    def email(self):
        return self._email
    
    @property
    def adreca(self):
        return self._adreca
    
    def desa(self):
        self._persistencia.desa(self)

    def get_llista_contactes(self):
        return self._persistencia.get_llista()
    
    def get_com_diccionari(self):
        return {
            "nom": self._nom,
            "cognoms": self._cognoms,
            "telefon": self._telefon,
            "email": self._email,
            "adreca": self._adreca.get_com_diccionari()
        }    
    
    def __str__(self):
        return json.dumps(self.get_com_diccionari(), indent=2)

if __name__ == "__main__":
    import Persistencia_adreca_sqlite
    import Persistencia_contacte_sqlite
    pc = Persistencia_contacte_sqlite.Persistencia_contacte_sqlite("test.db")
    pa = Persistencia_adreca_sqlite.Persistencia_adreca_sqlite("test.db")
    contacte = Contacte("nom", "cognoms", "telefon", "email", "nom_via", "numero", "pis", "porta", pc, pa)
    contacte.desa()
    contacte.get_llista_contactes()
    