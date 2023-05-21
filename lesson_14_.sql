CREATE DATABASE cheltor;
USE cheltor;
CREATE TABLE animal (
    animal_id int  NOT NULL AUTO_INCREMENT,
    animal_name varchar(255),
    animal_type varchar(255) NOT NULL,
    animal_age varchar(255),
    animal_sex varchar(255),
    animal_weight varchar(255),
    PRIMARY KEY (animal_id)
);
ALTER TABLE animal ADD created_at datetime;
INSERT INTO animal (animal_name, animal_type, animal_age, animal_sex, animal_weight) VALUES ("Bobik", "dog", 10, "m", 5);
INSERT INTO animal (animal_name, animal_type, animal_age, animal_sex, animal_weight) VALUES ("Sara", "dog", 11, "f", 3);
INSERT INTO animal (animal_name, animal_type, animal_age, animal_sex, animal_weight) VALUES ("Ajra", "dog", 2, "f", 10);
INSERT INTO animal (animal_name, animal_type, animal_age, animal_sex, animal_weight) VALUES ("Kazik", "cat", 3, "m", 5);
INSERT INTO animal (animal_name, animal_type, animal_age, animal_sex, animal_weight) VALUES ("Bianka", "cat", 14,"f", 12);
SELECT count(*) FROM animal;
SELECT count(*) FROM animal WHERE animal_type LIKE "dog";
SELECT AVG(animal_weight) FROM animal WHERE animal_type LIKE "dog";
SELECT DISTINCT animal_type FROM animal;
SELECT count(*) FROM animal WHERE animal_name LIKE "Villy";
SELECT count(*) FROM animal WHERE animal_type LIKE "dog" AND animal_sex LIKE "f";
SELECT count(*) FROM animal WHERE animal_type LIKE "dog" AND animal_sex LIKE "m";
SELECT DISTINCT animal_name FROM animal ORDER BY animal_name ASC;
SELECT * FROM animal WHERE animal_name LIKE '%ik'