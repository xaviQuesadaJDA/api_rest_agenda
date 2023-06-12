#!/usr/bin/python3
from Contacte import Contacte
from Persistencia_contacte_sqlite import Persistencia_contacte_sqlite 
from Persistencia_adreca_sqlite import Persistencia_adreca_sqlite
import json

RUTA_DB = "Contactes.db"
class App_agenda():
    def __init__(self):
        
        self._persistencia_contacte_sqlite = Persistencia_contacte_sqlite(RUTA_DB)
        self._persistencia_adreca_sqlite = Persistencia_adreca_sqlite(RUTA_DB)

    def afegeix_contacte(self, contacte: Contacte):
        contacte.desa()

    def llegir_llista_contactes(self, contacte: Contacte):
        resultat = []
        resultat = contacte.get_llista_contactes()
        return resultat