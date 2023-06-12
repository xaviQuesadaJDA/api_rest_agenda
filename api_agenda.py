#!/usr/bin/python3

import flask
import App_agenda
import Contacte
import json
from Persistencia_contacte_sqlite import Persistencia_contacte_sqlite 
from Persistencia_adreca_sqlite import Persistencia_adreca_sqlite

app = flask.Flask(__name__)
core_app = App_agenda.App_agenda()

RUTA_DB = "Contactes.db"

@app.route("/contactes", methods = ["POST", "GET"])
def contactes():
    if flask.request.method == "POST":

        info_body = flask.request.get_data() #texto pla
        contacto_nuevo = json.loads(info_body) #formato json
        contact = Contacte.Contacte(
            contacto_nuevo["nom"],
            contacto_nuevo["cognoms"],
            contacto_nuevo["telefon"],
            contacto_nuevo["email"],
            contacto_nuevo["adreca_nom_via"],
            contacto_nuevo["adreca_nombre_via"],
            contacto_nuevo["adreca_pis"],
            contacto_nuevo["adreca_porta"],
            Persistencia_contacte_sqlite(RUTA_DB),
            Persistencia_adreca_sqlite(RUTA_DB)
        )
        resultat = core_app.afegeix_contacte(contact)
        return "", 201
    
    elif flask.request.method == "GET":
        llista_jsons = []

        contact=Contacte.Contacte(
            None, 
            None,
            None,
            None, 
            None,
            None, 
            None,
            None,
            Persistencia_contacte_sqlite(RUTA_DB),
            Persistencia_adreca_sqlite(RUTA_DB)
        )
        
        llista_contactes= core_app.llegir_llista_contactes(contact)
        for i in llista_contactes:
            contacte_json = str(i)
            contacte_diccioanry=json.loads(contacte_json)
            llista_jsons.append(contacte_diccioanry)
        return flask.jsonify(llista_jsons), 200




app.run( host= "0.0.0.0", debug =False)