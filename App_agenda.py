#!/usr/bin/python3
from Contacte import Contacte

class App_agenda():
    def __init__(self):
        pass

    def afegeix_contacte(self, contacte: Contacte):
        contacte.desa()

    def llegir_llista_contactes(self, contacte: Contacte):
        resultat = []
        resultat = contacte.get_llista_contactes()
        return resultat