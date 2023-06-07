#!/usr/bin/python3
import json

class Persona():
    def __init__(self, nom, cognoms):
        self._nom = nom
        self._cognoms = cognoms

    @property
    def nom(self):
        return self._nom
    
    @property
    def cognoms(self):
        return self._cognoms

    def get_com_diccionari(self):
        return {
            "nom": self._nom,
            "cognoms": self._cognoms
        }    
    
    def __str__(self):
        return json.dumps(self.get_com_diccionari())
    
def main():
    una_persona = Persona("Pep", "Prieto")
    print(una_persona)

if __name__=="__main__":
    main()