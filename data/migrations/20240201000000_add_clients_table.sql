-- migrate:up
CREATE TABLE clients (
    id int NOT NULL,
    name character varying NOT NULL
);

-- migrate:down
DROP TABLE clients;
