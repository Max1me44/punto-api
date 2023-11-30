from datetime import datetime, timezone
from bson import ObjectId
from .database import mongo_db


def create_joueur(nom: str):
    joueur = {"nom": nom}
    return mongo_db.db.joueurs.insert_one(joueur).inserted_id


def create_partie(id_joueur: ObjectId, gagnant: bool):
    date_heure = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
    partie = {"id_joueur": id_joueur, "date_heure": date_heure, "gagnant": gagnant}
    return mongo_db.db.parties.insert_one(partie).inserted_id


def get_joueur_by_nom(nom: str):
    return mongo_db.db.joueurs.find_one({"nom": nom})


def get_nombre_parties_joueur(id_joueur: ObjectId):
    return mongo_db.db.parties.count_documents({"id_joueur": id_joueur})


def get_nombre_parties_gagnees_joueur(id_joueur: ObjectId):
    return mongo_db.db.parties.count_documents({"id_joueur": id_joueur, "gagnant": True})
