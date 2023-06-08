#!/usr/bin/python3
import json

class Adreca():
    def __init__(self, nom_via, nombre_via,
                 pis, porta, persistencia):
        self._nom_via = nom_via
        self._nombre_via = nombre_via
        self._pis = pis
        self._porta = porta
        self._persistencia = persistencia

    @property 
    def nom_via(self):
        return self._nom_via

    @property 
    def nombre_via(self):
        return self._nombre_via

    @property 
    def pis(self):
        return self._pis

    @property 
    def porta(self):
        return self._porta
    
    def desa(self, contacte_id):
        self._persistencia.desa(self, contacte_id)

    def get_com_diccionari(self):
        return {
            "nom_via": self._nom_via,
            "nombre_via": self._nombre_via,
            "pis": self._pis,
            "porta": self._porta
        }    
    
    def __str__(self):
        return json.dumps(self.get_com_diccionari())