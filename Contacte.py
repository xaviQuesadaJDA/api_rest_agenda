#!/usr/bin/python3
from Persona import Persona
from Adreca import Adreca
import json

class Contacte(Persona):
    def __init__(self, nom, cognoms, telefon, email, 
                 adreca_nom_via, adreca_nombre_via, 
                 adreca_pis, adreca_porta):
        super().__init__(nom, cognoms)
        self._telefon = telefon
        self._email = email
        self._adreca = Adreca(adreca_nom_via, adreca_nombre_via, 
                        adreca_pis, adreca_porta)

    @property 
    def telefon(self):
        return self._telefon
    
    @property
    def email(self):
        return self._email
    
    @property
    def adreca(self):
        return self._adreca
    
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
    contacte = Contacte("Xavi", "Quesada", "555-55-55", "mail@google.com", "Pau Claris", "21", "3er", "2ona")
    print(str(contacte))