SET FOREIGN_KEY_CHECKS = 0;

TRUNCATE TABLE back_buildingtype;
TRUNCATE TABLE back_building;
TRUNCATE TABLE back_vehicletype;
TRUNCATE TABLE back_vehicle;
TRUNCATE TABLE back_scenariotype;
TRUNCATE TABLE back_scenario;
TRUNCATE TABLE back_stafftype;
TRUNCATE TABLE back_staff;
TRUNCATE TABLE back_call;


ALTER TABLE back_buildingtype AUTO_INCREMENT = 0;
ALTER TABLE back_building AUTO_INCREMENT = 0;
ALTER TABLE back_vehicletype AUTO_INCREMENT = 0;
ALTER TABLE back_vehicle AUTO_INCREMENT = 0;
ALTER TABLE back_scenariotype AUTO_INCREMENT = 0;
ALTER TABLE back_scenario AUTO_INCREMENT = 0;
ALTER TABLE back_stafftype AUTO_INCREMENT = 0;
ALTER TABLE back_staff AUTO_INCREMENT = 0;
ALTER TABLE back_call AUTO_INCREMENT = 0;


INSERT INTO back_buildingtype (name) VALUES
('Poste de police'),
('Centre hospitalier'),
('Caserne de pompier');

INSERT INTO back_building (name, address, coordinates_latitude, coordinates_longitude, type_id) VALUES
('Gendarmerie La Réole', 'Gendarmerie nationale, A la Bori, Rue de Caumont, 33190 La Réole, France', 44.582476, -0.031490, 1),
('Caserne de pompier La Réole', '4 Avenue du Mahon, 33190 La Réole, France', 44.582074, -0.032260, 3);

INSERT INTO back_vehicletype (name) VALUES
('VSAV'),
('Ambulance'),
('Voiture de patrouille');

INSERT INTO back_vehicle (name, coordinates_latitude, coordinates_longitude, type_id, building_id, call_id) VALUES
("Patrouille 1", 44.582476, -0.031490, 3, 1, null),
("Patrouille 2", 44.582074, -0.032260, 3, 1, null),
("Ambulance La Réole",44.582074, -0.032260, 1, 2, null);

INSERT INTO back_scenariotype (name) VALUES
('Police'),
('Pompier');

INSERT INTO back_scenario (name, description, type_id) VALUES
("Vol de voiture", "Un individu à volé une voiture", 1),
("Ivresse sur la voie publique", "Un individu est ivre sur la voie publique", 1),
("Accident de la route", "Un accident à eu lieu sur la voie publique", 2);

INSERT INTO back_stafftype (name) VALUES
('Pompier'),
('Gendarme');

INSERT INTO back_staff (firstname, lastname, type_id, vehicle_id, building_id) VALUES
("Jack", "Brown", 1, null, 2),
("Marie", "Lisle", 2, null, 1);

INSERT INTO back_call (coordinates_latitude, coordinates_longitude, datetime, completion_datetime, scenario_id, mission_status) VALUES
(44.582476, -0.031490, "2023-09-27 22:28:30", "2023-09-27 22:28:30", 1, "En cours");

SET FOREIGN_KEY_CHECKS = 1;
