SET FOREIGN_KEY_CHECKS = 0;

TRUNCATE TABLE building_types;
TRUNCATE TABLE buildings;
TRUNCATE TABLE vehicle_types;
TRUNCATE TABLE vehicles;


ALTER TABLE building_types AUTO_INCREMENT = 0;
ALTER TABLE buildings AUTO_INCREMENT = 0;
ALTER TABLE vehicle_types AUTO_INCREMENT = 0;
ALTER TABLE vehicles AUTO_INCREMENT = 0;


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


SET FOREIGN_KEY_CHECKS = 1;
