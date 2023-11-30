from sqlalchemy.orm import Session
from .models import Joueur, Partie


def create_joueur(db: Session, nom: str):
    joueur = Joueur(nom=nom)
    db.add(joueur)
    db.commit()
    db.refresh(joueur)
    return joueur


def create_partie(db: Session, id_joueur: int, gagnant: bool):
    partie = Partie(id_joueur=id_joueur, gagnant=gagnant)
    db.add(partie)
    db.commit()
    db.refresh(partie)
    return partie


def get_joueur_by_nom(db: Session, nom: str):
    return db.query(Joueur).filter(Joueur.nom == nom).first()


def get_nombre_parties_joueur(db: Session, id_joueur: int):
    return db.query(Partie).filter(Partie.id_joueur == id_joueur).count()


def get_nombre_parties_gagnees_joueur(db: Session, id_joueur: int):
    return db.query(Partie).filter(Partie.id_joueur == id_joueur, Partie.gagnant == True).count()
