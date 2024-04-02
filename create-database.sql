CREATE  DATABASE dogs_are_better;

CREATE USER dog_admin with PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE dogs_are_better TO dog_admin;