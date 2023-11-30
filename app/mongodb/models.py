from datetime import datetime

from bson import ObjectId
from pydantic import BaseModel


class Joueur(BaseModel):
    id: ObjectId
    nom: str


class Partie(BaseModel):
    id: ObjectId
    id_joueur: ObjectId
    date_heure: datetime
    gagnant: bool
