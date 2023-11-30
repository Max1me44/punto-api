from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from . import crud, database

router = APIRouter()


@router.post("/joueurs/create/")
def create_joueur(nom: str, db: Session = Depends(database.get_db)):
    existing_joueur = crud.get_joueur_by_nom(db=db, nom=nom)
    if existing_joueur:
        raise HTTPException(status_code=400, detail="Joueur déjà existant")
    crud.create_joueur(db=db, nom=nom)
    return {"message": "Joueur créé avec succès"}


@router.post("/parties/create/")
def create_partie(nom_joueur: str, gagnant: bool, db: Session = Depends(database.get_db)):
    joueur = crud.get_joueur_by_nom(db=db, nom=nom_joueur)
    if joueur is None:
        raise HTTPException(status_code=404, detail="Joueur non trouvé")
    # Enregistrer la partie avec l'ID du joueur
    crud.create_partie(db=db, id_joueur=joueur.id, gagnant=gagnant)
    return {"message": "Partie créée avec succès"}


@router.get("/joueurs/{nom}/")
def get_joueur_by_nom(nom: str, db: Session = Depends(database.get_db)):
    db_joueur = crud.get_joueur_by_nom(db=db, nom=nom)
    if db_joueur is None:
        raise HTTPException(status_code=404, detail="Joueur non trouvé")
    return jsonable_encoder(db_joueur)


@router.get("/joueurs/{nom}/nombre_parties/")
def get_nombre_parties_joueur(nom: str, db: Session = Depends(database.get_db)):
    joueur = crud.get_joueur_by_nom(db=db, nom=nom)
    if joueur is None:
        raise HTTPException(status_code=404, detail="Joueur non trouvé")
    return {"nombre_parties": crud.get_nombre_parties_joueur(db=db, id_joueur=joueur.id)}


@router.get("/joueurs/{nom}/nombre_parties_gagnees/")
def get_nombre_parties_gagnees_joueur(nom: str, db: Session = Depends(database.get_db)):
    joueur = crud.get_joueur_by_nom(db=db, nom=nom)
    if joueur is None:
        raise HTTPException(status_code=404, detail="Joueur non trouvé")
    return {"nombre_parties_gagnees": crud.get_nombre_parties_gagnees_joueur(db=db, id_joueur=joueur.id)}
