#!/usr/bin/python3
from Contacte import Contacte

RUTA_BD = "./agenda.db"

class App_agenda():
    def __init__(self):
        pass

    def afegeix_contacte(self, contacte: Contacte):
        contacte.desa()