#!/bin/bash
export DATABASE_URL=postgres://postgres:postgres@db:5439/db?sslmode=disable
dbmate -d ./data/migrations --no-dump-schema up

echo "SELECT 'DROP DATABASE db_test' WHERE EXISTS (SELECT FROM pg_database WHERE datname = 'db_test')\gexec" | psql "${DATABASE_URL}"
echo "SELECT 'CREATE DATABASE db_test' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'db_test')\gexec" | psql "${DATABASE_URL}"
DATABASE_URL=postgres://postgres:postgres@db:5439/db_test?sslmode=disable dbmate -d ./data/migrations --no-dump-schema up

