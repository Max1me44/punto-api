-- MySQL Shell:
-- Se mettre en sql avec:\sql
-- Se connecter avec l'utilisateur Punto:\connect Punto@localhost
-- Mot de passe utilisateur Punto: JesuisPunto


-- Créer la base si pas déjà fait:
CREATE DATABASE puntodb;

-- Utiliser la base:
USE puntodb;

-- Créer les tables:
CREATE TABLE joueurs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) UNIQUE
);

CREATE TABLE parties (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_joueur INT,
    date_heure DATETIME DEFAULT CURRENT_TIMESTAMP,
    gagnant BOOLEAN,
    FOREIGN KEY (id_joueur) REFERENCES joueurs(id)
);
