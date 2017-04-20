PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE company ( login TEXT, first_name TEXT, last_name TEXT);
INSERT INTO "company" VALUES('9maf4you','Maxim','Timokhin');
INSERT INTO "company" VALUES('superturbo300','Valily','Ivanov');
COMMIT;
