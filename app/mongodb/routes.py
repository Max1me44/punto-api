from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder

from . import crud

router = APIRouter()


@router.post("/joueurs/create/")
def create_joueur(nom: str):
    existing_joueur = crud.get_joueur_by_nom(nom=nom)
    if existing_joueur:
        raise HTTPException(status_code=400, detail="Joueur déjà existant")
    crud.create_joueur(nom=nom)
    return {"message": "Joueur créé avec succès"}


@router.post("/parties/create/")
def create_partie(nom: str, gagnant: bool):
    joueur = crud.get_joueur_by_nom(nom=nom)
    if joueur is None:
        raise HTTPException(status_code=404, detail="Joueur non trouvé")
    # Enregistrer la partie avec l'ID du joueur
    crud.create_partie(id_joueur=joueur["_id"], gagnant=gagnant)
    return {"message": "Partie créée avec succès"}


@router.get("/joueurs/{nom}/")
def get_joueur_by_nom(nom: str):
    joueur = crud.get_joueur_by_nom(nom=nom)
    if joueur is None:
        raise HTTPException(status_code=404, detail="Joueur non trouvé")
    # Convertir l'ObjectId en str avant de le retourner
    joueur['_id'] = str(joueur['_id'])
    return jsonable_encoder(joueur)


@router.get("/joueurs/{nom}/nombre_parties/")
def get_nombre_parties_joueur(nom: str):
    joueur = crud.get_joueur_by_nom(nom=nom)
    if joueur is None:
        raise HTTPException(status_code=404, detail="Joueur non trouvé")
    return {"nombre_parties": crud.get_nombre_parties_joueur(id_joueur=joueur["_id"])}


@router.get("/joueurs/{nom}/nombre_parties_gagnees/")
def get_nombre_parties_gagnees_joueur(nom: str):
    joueur = crud.get_joueur_by_nom(nom=nom)
    if joueur is None:
        raise HTTPException(status_code=404, detail="Joueur non trouvé")
    return {"nombre_parties_gagnees": crud.get_nombre_parties_gagnees_joueur(id_joueur=joueur["_id"])}
