SET FOREIGN_KEY_CHECKS = 0;

TRUNCATE TABLE building_types;

ALTER TABLE building_types AUTO_INCREMENT = 0;

INSERT INTO building_types (name) VALUES
('Poste de police'),
('Centre hospitalier'),
('Caserne de pompier');

SET FOREIGN_KEY_CHECKS = 1;
