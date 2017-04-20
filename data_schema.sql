PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE company ( login TEXT, first_name TEXT, last_name TEXT);
INSERT INTO "company" VALUES('9maf4you','Maxim','Timokhin');
INSERT INTO "company" VALUES('superturbo300','Vasily','Ivanov');
COMMIT;

BEGIN TRANSACTION;
CREATE TABLE permission ( login TEXT, type TEXT, authed INT, timestmp INT);
INSERT INTO "permission" VALUES('admin','root', 0, 1492709148);
INSERT INTO "permission" VALUES('yvasya','manager',0, 1492709148);
INSERT INTO "permission" VALUES('maf','user',0, 1492709148);
COMMIT;