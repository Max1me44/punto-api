from neomodel import StructuredNode, StringProperty, config, db
from datetime import datetime, timezone
from fastapi import APIRouter, HTTPException

config.DATABASE_URL = "bolt://neo4j:JesuisPunto@localhost:7687"

router = APIRouter()


# Opérations CRUD Neo4j
def create_joueur(nom: str):
    query = f"CREATE (j:Joueur {{nom: '{nom}'}})"
    db.cypher_query(query)


def create_partie(nom_joueur: str, gagnant: bool):
    date_heure = datetime.now(timezone.utc)
    gagnant_str = 'True' if gagnant else 'False'
    query = (
        f"CREATE (p:Partie {{date_heure: '{date_heure}', gagnant: '{gagnant_str}'}})"
        f"RETURN p"
    )
    partie = db.cypher_query(query)
    node = partie[0][0][0]
    id_partie = node.id
    # crée une relation entre le joueur et la partie
    query = f"MATCH (j:Joueur {{nom: '{nom_joueur}'}}), (p:Partie) WHERE ID(p)={id_partie} CREATE (j)-[:JOUE]->(p)"
    db.cypher_query(query)


def joueur_exists(nom: str):
    query = f"MATCH (j:Joueur {{nom: '{nom}'}}) RETURN id(j) AS id"
    joueur = db.cypher_query(query)
    return bool(joueur and joueur[0])  # True si joueur existe, False sinon


def get_joueur(nom: str):
    query = f"MATCH (j:Joueur {{nom: '{nom}'}}) RETURN j.nom AS nom"
    result = db.cypher_query(query)
    return result[0][0]


def get_nombre_parties_joueur(nom: str):
    query = f"MATCH (j:Joueur {{nom: '{nom}'}})-[:JOUE]->(p:Partie) RETURN count(p) AS nombre_parties"
    result = db.cypher_query(query)
    return result[0][0]


def get_nombre_parties_gagnees_joueur(nom: str):
    query = (f"MATCH (j:Joueur {{nom: '{nom}'}})-[:JOUE]->(p:Partie) WHERE p.gagnant='True' RETURN count(p) AS "
             f"nombre_parties_gagnees")
    result = db.cypher_query(query)
    return result[0][0]


def delete_all_data():
    db.cypher_query("MATCH (n:Joueur) DETACH DELETE n")
    db.cypher_query("MATCH (n:Partie) DETACH DELETE n")


# Routes FastAPI pour Neo4j
@router.post("/joueurs/create/")
def create_joueur_r(nom: str):
    if joueur_exists(nom=nom):
        raise HTTPException(status_code=200, detail="Joueur déjà existant")
    create_joueur(nom=nom)
    return {"message": "Joueur créé avec succès"}


@router.post("/parties/create/")
def create_partie_r(nom_joueur: str, gagnant: bool):
    if not joueur_exists(nom=nom_joueur):
        raise HTTPException(status_code=404, detail="Joueur non trouvé")
    create_partie(nom_joueur=nom_joueur, gagnant=gagnant)
    return {"message": "Partie créée avec succès"}


@router.get("/joueurs/{nom}/")
def get_joueur_by_nom_r(nom: str):
    if not joueur_exists(nom=nom):
        raise HTTPException(status_code=404, detail="Joueur non trouvé")
    return {
        "nom": nom,
        "nombre_parties": get_nombre_parties_joueur(nom=nom)[0],
        "nombre_parties_gagnees": get_nombre_parties_gagnees_joueur(nom=nom)[0]
    }


@router.get("/joueurs/{nom}/nombre_parties/")
def get_nombre_parties_joueur_r(nom: str):
    if not joueur_exists(nom=nom):
        raise HTTPException(status_code=404, detail="Joueur non trouvé")
    return {"nombre_parties": get_nombre_parties_joueur(nom=nom)}


@router.get("/joueurs/{nom}/nombre_parties_gagnees/")
def get_nombre_parties_gagnees_joueur_r(nom: str):
    if not joueur_exists(nom=nom):
        raise HTTPException(status_code=404, detail="Joueur non trouvé")
    return {"nombre_parties_gagnees": get_nombre_parties_gagnees_joueur(nom=nom)}


@router.post("/reset/all")
def reset_data():
    delete_all_data()
    return {"message": "Données de Neo4j réinitialisées avec succès"}
