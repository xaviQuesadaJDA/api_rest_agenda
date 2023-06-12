# api_rest_agenda

API REST per gestionar una agenda de contactes.
Desenvolupada durant el curs del SOC al juny de 2023.

## Diagrama de classes de l'agenda de contactes.

```mermaid
classDiagram

class App_agenda{
    + afegeix_contacte(contacte)
}
class Persona{
    + str: nom
    + str: cognoms
}
class Contacte{
    + str: telefon
    + str: email
    + Adreca: adreca
}
class Adreca{
    + str: nom_via
    + str: nombre_via
    + str: pis
    + str: porta
}
Persona  <|-- Contacte
Adreca <-- Contacte
App_agenda --> Contacte
```

:)
