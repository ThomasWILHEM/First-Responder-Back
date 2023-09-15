-- Adminer 4.8.1 PostgreSQL 15.4 (Debian 15.4-1.pgdg120+1) dump

DROP TABLE IF EXISTS "building_types";
DROP SEQUENCE IF EXISTS building_types_id_seq;
CREATE SEQUENCE building_types_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 3 CACHE 1;

CREATE TABLE "public"."building_types" (
    "id" integer DEFAULT nextval('building_types_id_seq') NOT NULL,
    "name" character varying,
    CONSTRAINT "building_types_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "ix_building_types_name" UNIQUE ("name")
) WITH (oids = false);

CREATE INDEX "ix_building_types_id" ON "public"."building_types" USING btree ("id");

TRUNCATE "building_types";
INSERT INTO "building_types" ("id", "name") VALUES
(1,	'Poste de police'),
(2,	'Centre hospitalier'),
(3,	'Caserne de pompier');

DROP TABLE IF EXISTS "buildings";
DROP SEQUENCE IF EXISTS buildings_id_seq;
CREATE SEQUENCE buildings_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 11 CACHE 1;

CREATE TABLE "public"."buildings" (
    "id" integer DEFAULT nextval('buildings_id_seq') NOT NULL,
    "name" character varying,
    "coordinates_latitude" double precision,
    "coordinates_longitude" double precision,
    "type_id" integer,
    "address" text,
    CONSTRAINT "buildings_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "ix_buildings_name" UNIQUE ("name")
) WITH (oids = false);

CREATE INDEX "ix_buildings_id" ON "public"."buildings" USING btree ("id");

TRUNCATE "buildings";
INSERT INTO "buildings" ("id", "name", "coordinates_latitude", "coordinates_longitude", "type_id", "address") VALUES
(10,	'Caserne La Réole',	44.58307066,	-0.0283885,	2,	'Avenue de la Croix d''Hors,La Réole, 33190, France'),
(11,	'Gendarmerie La Réole',	44.58239818,	-0.03124237,	1,	'Rue de Caumont,La Réole, 33190, France');

DROP TABLE IF EXISTS "calls";
DROP SEQUENCE IF EXISTS calls_id_seq;
CREATE SEQUENCE calls_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 2 CACHE 1;

CREATE TABLE "public"."calls" (
    "id" integer DEFAULT nextval('calls_id_seq') NOT NULL,
    "coordinates_latitude" double precision,
    "coordinates_longitude" double precision,
    "datetime" timestamp,
    "completion_datetime" timestamp,
    "scenario_id" integer,
    "mission_status" character varying,
    CONSTRAINT "calls_pkey" PRIMARY KEY ("id")
) WITH (oids = false);

CREATE INDEX "ix_calls_id" ON "public"."calls" USING btree ("id");

TRUNCATE "calls";
INSERT INTO "calls" ("id", "coordinates_latitude", "coordinates_longitude", "datetime", "completion_datetime", "scenario_id", "mission_status") VALUES
(1,	44.5833,	-0.0333,	'2023-09-11 16:00:05.093',	'2023-09-11 16:00:05.093',	1,	'string'),
(2,	44.58326721191406,	-0.029268071055412292,	'2023-09-11 16:21:31.991',	'2023-09-11 16:21:31.991',	2,	'string');

DROP TABLE IF EXISTS "scenario_types";
DROP SEQUENCE IF EXISTS scenario_types_id_seq;
CREATE SEQUENCE scenario_types_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 2 CACHE 1;

CREATE TABLE "public"."scenario_types" (
    "id" integer DEFAULT nextval('scenario_types_id_seq') NOT NULL,
    "name" character varying,
    CONSTRAINT "ix_scenario_types_name" UNIQUE ("name"),
    CONSTRAINT "scenario_types_pkey" PRIMARY KEY ("id")
) WITH (oids = false);

CREATE INDEX "ix_scenario_types_id" ON "public"."scenario_types" USING btree ("id");

TRUNCATE "scenario_types";
INSERT INTO "scenario_types" ("id", "name") VALUES
(1,	'Police'),
(2,	'Pompuer');

DROP TABLE IF EXISTS "scenarios";
DROP SEQUENCE IF EXISTS scenarios_id_seq;
CREATE SEQUENCE scenarios_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 2 CACHE 1;

CREATE TABLE "public"."scenarios" (
    "id" integer DEFAULT nextval('scenarios_id_seq') NOT NULL,
    "name" character varying,
    "description" character varying,
    "type_id" integer,
    CONSTRAINT "ix_scenarios_name" UNIQUE ("name"),
    CONSTRAINT "scenarios_pkey" PRIMARY KEY ("id")
) WITH (oids = false);

CREATE INDEX "ix_scenarios_id" ON "public"."scenarios" USING btree ("id");

TRUNCATE "scenarios";
INSERT INTO "scenarios" ("id", "name", "description", "type_id") VALUES
(1,	'Vol de voiture',	'Un individu à volé une voiture',	1),
(2,	'Tappage',	'Des gens font du bruit',	1);

DROP TABLE IF EXISTS "staff_types";
DROP SEQUENCE IF EXISTS staff_types_id_seq;
CREATE SEQUENCE staff_types_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 2 CACHE 1;

CREATE TABLE "public"."staff_types" (
    "id" integer DEFAULT nextval('staff_types_id_seq') NOT NULL,
    "name" character varying,
    CONSTRAINT "ix_staff_types_name" UNIQUE ("name"),
    CONSTRAINT "staff_types_pkey" PRIMARY KEY ("id")
) WITH (oids = false);

CREATE INDEX "ix_staff_types_id" ON "public"."staff_types" USING btree ("id");

TRUNCATE "staff_types";
INSERT INTO "staff_types" ("id", "name") VALUES
(1,	'Pompier'),
(2,	'Gendarme');

DROP TABLE IF EXISTS "staffs";
DROP SEQUENCE IF EXISTS staffs_id_seq;
CREATE SEQUENCE staffs_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 5 CACHE 1;

CREATE TABLE "public"."staffs" (
    "id" integer DEFAULT nextval('staffs_id_seq') NOT NULL,
    "firstname" character varying,
    "lastname" character varying,
    "type_id" integer,
    "vehicle_id" integer,
    "building_id" integer,
    CONSTRAINT "staffs_pkey" PRIMARY KEY ("id")
) WITH (oids = false);

CREATE INDEX "ix_staffs_firstname" ON "public"."staffs" USING btree ("firstname");

CREATE INDEX "ix_staffs_id" ON "public"."staffs" USING btree ("id");

CREATE INDEX "ix_staffs_lastname" ON "public"."staffs" USING btree ("lastname");

TRUNCATE "staffs";
INSERT INTO "staffs" ("id", "firstname", "lastname", "type_id", "vehicle_id", "building_id") VALUES
(1,	'Max',	'John',	1,	NULL,	10),
(3,	'Adrien',	'Storn',	2,	NULL,	10),
(2,	'Coline',	'Tapard',	1,	NULL,	10);

DROP TABLE IF EXISTS "vehicle_types";
DROP SEQUENCE IF EXISTS vehicle_types_id_seq;
CREATE SEQUENCE vehicle_types_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 3 CACHE 1;

CREATE TABLE "public"."vehicle_types" (
    "id" integer DEFAULT nextval('vehicle_types_id_seq') NOT NULL,
    "name" character varying,
    CONSTRAINT "ix_vehicle_types_name" UNIQUE ("name"),
    CONSTRAINT "vehicle_types_pkey" PRIMARY KEY ("id")
) WITH (oids = false);

CREATE INDEX "ix_vehicle_types_id" ON "public"."vehicle_types" USING btree ("id");

TRUNCATE "vehicle_types";
INSERT INTO "vehicle_types" ("id", "name") VALUES
(1,	'VSAV'),
(2,	'Camion Citerne'),
(3,	'Voiture de police');

DROP TABLE IF EXISTS "vehicles";
DROP SEQUENCE IF EXISTS vehicles_id_seq;
CREATE SEQUENCE vehicles_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 19 CACHE 1;

CREATE TABLE "public"."vehicles" (
    "id" integer DEFAULT nextval('vehicles_id_seq') NOT NULL,
    "coordinates_latitude" double precision,
    "coordinates_longitude" double precision,
    "type_id" integer,
    "building_id" integer,
    "call_id" integer,
    CONSTRAINT "vehicles_pkey" PRIMARY KEY ("id")
) WITH (oids = false);

CREATE INDEX "ix_vehicles_id" ON "public"."vehicles" USING btree ("id");

TRUNCATE "vehicles";
INSERT INTO "vehicles" ("id", "coordinates_latitude", "coordinates_longitude", "type_id", "building_id", "call_id") VALUES
(18,	44.58307066,	-0.0283885,	2,	10,	NULL),
(19,	44.58239818,	-0.03124237,	3,	11,	NULL);

ALTER TABLE ONLY "public"."buildings" ADD CONSTRAINT "buildings_type_id_fkey" FOREIGN KEY (type_id) REFERENCES building_types(id) NOT DEFERRABLE;

ALTER TABLE ONLY "public"."calls" ADD CONSTRAINT "calls_scenario_id_fkey" FOREIGN KEY (scenario_id) REFERENCES scenarios(id) NOT DEFERRABLE;

ALTER TABLE ONLY "public"."scenarios" ADD CONSTRAINT "scenarios_type_id_fkey" FOREIGN KEY (type_id) REFERENCES scenario_types(id) NOT DEFERRABLE;

ALTER TABLE ONLY "public"."staffs" ADD CONSTRAINT "staffs_building_id_fkey" FOREIGN KEY (building_id) REFERENCES buildings(id) NOT DEFERRABLE;
ALTER TABLE ONLY "public"."staffs" ADD CONSTRAINT "staffs_type_id_fkey" FOREIGN KEY (type_id) REFERENCES staff_types(id) NOT DEFERRABLE;
ALTER TABLE ONLY "public"."staffs" ADD CONSTRAINT "staffs_vehicle_id_fkey" FOREIGN KEY (vehicle_id) REFERENCES vehicles(id) NOT DEFERRABLE;

ALTER TABLE ONLY "public"."vehicles" ADD CONSTRAINT "vehicles_building_id_fkey" FOREIGN KEY (building_id) REFERENCES buildings(id) NOT DEFERRABLE;
ALTER TABLE ONLY "public"."vehicles" ADD CONSTRAINT "vehicles_call_id_fkey" FOREIGN KEY (call_id) REFERENCES calls(id) NOT DEFERRABLE;
ALTER TABLE ONLY "public"."vehicles" ADD CONSTRAINT "vehicles_type_id_fkey" FOREIGN KEY (type_id) REFERENCES vehicle_types(id) NOT DEFERRABLE;

-- 2023-09-15 07:42:38.006246+00
