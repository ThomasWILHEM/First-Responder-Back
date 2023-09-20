-- Supprimer toutes les données de la table building_types
TRUNCATE TABLE building_types;

ALTER TABLE building_types AUTO_INCREMENT = 0;

-- Insérer des données dans la table building_types
INSERT INTO building_types (name) VALUES
('Poste de police'),
('Centre hospitalier'),
('Caserne de pompier');
