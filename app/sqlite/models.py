from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, func
from .database import Base


class Joueur(Base):
    __tablename__ = "joueurs"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True, unique=True)


class Partie(Base):
    __tablename__ = "parties"
    id = Column(Integer, primary_key=True, index=True)
    id_joueur = Column(Integer, ForeignKey('joueurs.id'))
    date_heure = Column(DateTime(timezone=True), server_default=func.now())
    gagnant = Column(Boolean)
