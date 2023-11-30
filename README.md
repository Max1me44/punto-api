# Punto API

Cette API est dédié pour le jeu Punto. Elle permet de gérer des joueurs et des parties pour un jeu fictif appelé Punto. L'API est développée en utilisant FastAPI et prend en charge les bases de données MongoDB, MySQL, et SQLite.

## Fonctionnalités

L'API offre les fonctionnalités suivantes :

- Création de joueurs
- Enregistrement de parties avec indication du gagnant
- Consultation du nombre total de parties jouées par un joueur
- Consultation du nombre de parties gagnées par un joueur
- Obtention d'informations détaillées sur un joueur (nom, nombre total de parties, nombre de parties gagnées)

## Installation

Pour installer et exécuter l'API localement, suivez ces étapes :

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/votre-utilisateur/mon-api-punto.git
   cd mon-api-punto
   ```
   
2. Installez les dépendances (vous pouvez créer un environnement virtuel au préalable) :
    ```bash
    pip install -r requirements.txt
    ```
   
3. Exécutez l'application :
    ```bash
    uvicorn main:app --reload
    ```
   L'API sera accessible à l'adresse http://127.0.0.1:8000. La documentation interactive Swagger est disponible à http://127.0.0.1:8000/docs.


## Configuration de la base de données

L'API prend en charge trois bases de données : MongoDB, MySQL, et SQLite. Assurez-vous d'avoir une base de données disponible et de mettre à jour les informations de connexion.

### Endpoint

### Création d'un joueur
```bash
POST /parties/create/
```
Permet de créer un nouveau joueur en spécifiant son nom.

### Création d'une partie
```bash
POST /parties/create/
```
Enregistre une nouvelle partie avec le nom du joueur et l'indication s'il a gagné ou non.

### Informations sur un joueur
```bash
GET /joueurs/{nom}/
```
Obtient des informations détaillées sur un joueur, y compris le nombre total de parties et le nombre de parties gagnées.

### Nombre total de parties d'un joueur
```bash
GET /joueurs/{nom}/nombre_parties/
```
Renvoie le nombre total de parties jouées par un joueur.

### Nombre de parties gagnées par un joueur
```bash
GET /joueurs/{nom}/nombre_parties_gagnees/
```
Renvoie le nombre de parties gagnées par un joueur.

