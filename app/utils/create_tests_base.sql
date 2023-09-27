SET FOREIGN_KEY_CHECKS = 0;

TRUNCATE TABLE building_types;
TRUNCATE TABLE buildings;
TRUNCATE TABLE vehicle_types;
TRUNCATE TABLE vehicles;
TRUNCATE TABLE scenario_types;
TRUNCATE TABLE scenarios;
TRUNCATE TABLE calls;


ALTER TABLE building_types AUTO_INCREMENT = 0;
ALTER TABLE buildings AUTO_INCREMENT = 0;
ALTER TABLE vehicle_types AUTO_INCREMENT = 0;
ALTER TABLE vehicles AUTO_INCREMENT = 0;
ALTER TABLE scenario_types AUTO_INCREMENT = 0;
ALTER TABLE scenarios AUTO_INCREMENT = 0;
ALTER TABLE calls AUTO_INCREMENT = 0;


INSERT INTO building_types (name) VALUES
('Poste de police'),
('Centre hospitalier'),
('Caserne de pompier');

INSERT INTO buildings (name, address, coordinates_latitude, coordinates_longitude, type_id) VALUES
('Gendarmerie La Réole', 'Gendarmerie nationale, A la Bori, Rue de Caumont, 33190 La Réole, France', 44.582476, -0.031490, 1),
('Caserne de pompier La Réole', '4 Avenue du Mahon, 33190 La Réole, France', 44.582074, -0.032260, 3);

INSERT INTO vehicle_types (name) VALUES
('VSAV'),
('Ambulance'),
('Voiture de patrouille');

INSERT INTO vehicles (coordinates_latitude, coordinates_longitude, type_id, building_id, call_id) VALUES
(44.582476, -0.031490, 3, 1, null),
(44.582074, -0.032260, 3, 1, null),
(44.582074, -0.032260, 1, 2, null);

INSERT INTO scenario_types (name) VALUES
('Police'),
('Pompier');

INSERT INTO scenarios (name, description, type_id) VALUES
("Vol de voiture", "Un individu à volé une voiture", 1),
("Ivresse sur la voie publique", "Un individu est ivre sur la voie publique", 1),
("Accident de la route", "Un accident à eu lieu sur la voie publique", 2);

INSERT INTO calls (coordinates_latitude, coordinates_longitude, datetime, completion_datetime, scenario_id, mission_status) VALUES
(44.582476, -0.031490, "2023-09-27 22:28:30", "2023-09-27 22:28:30", 1, "En cours");

SET FOREIGN_KEY_CHECKS = 1;
