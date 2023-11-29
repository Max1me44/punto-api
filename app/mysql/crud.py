from sqlalchemy.orm import Session
from . import models


def create_joueur(db: Session, nom: str):
    db_joueur = models.Joueur(nom=nom)
    db.add(db_joueur)
    db.commit()
    db.refresh(db_joueur)
    return db_joueur


def create_partie(db: Session, id_joueur: int, gagnant: bool):
    db_partie = models.Partie(id_joueur=id_joueur, gagnant=gagnant)
    db.add(db_partie)
    db.commit()
    db.refresh(db_partie)
    return db_partie


def get_joueur_by_nom(db: Session, nom: str):
    return db.query(models.Joueur).filter(models.Joueur.nom == nom).first()


def get_nombre_parties_joueur(db: Session, id_joueur: int):
    return db.query(models.Partie).filter(models.Partie.id_joueur == id_joueur).count()


def get_nombre_parties_gagnees_joueur(db: Session, id_joueur: int):
    return db.query(models.Partie).filter(models.Partie.id_joueur == id_joueur, models.Partie.gagnant == True).count()
