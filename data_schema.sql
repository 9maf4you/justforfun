PRAGMA foreign_keys=OFF;
DROP TABLE company;
DROP TABLE permission;

BEGIN TRANSACTION;
CREATE TABLE company ( login TEXT, first_name TEXT, last_name TEXT);
INSERT INTO "company" VALUES('9maf4you','Maxim','Timokhin');
INSERT INTO "company" VALUES('superturbo300','Vasily','Ivanov');
COMMIT;

BEGIN TRANSACTION;
CREATE TABLE permission ( login TEXT, type TEXT, authed INT, timestmp INT, ip TEXT);
INSERT INTO "permission" VALUES('9maf4you','root', 0, 1492709148, '0.0.0.0');
INSERT INTO "permission" VALUES('superturbo300','manager',0, 1492709148, '0.0.0.0');
INSERT INTO "permission" VALUES('maf','user',0, 1492709148, '0.0.0.0');
COMMIT;