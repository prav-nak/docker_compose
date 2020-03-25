CREATE DATABASE census;
use census;

CREATE TABLE people_data (
  name VARCHAR(20),
  gender VARCHAR(10), 
  age TINYINT
);

INSERT INTO people_data (name, gender, age) VALUES 
  ('apple', 'male', 20),
  ('bat', 'female', 22);