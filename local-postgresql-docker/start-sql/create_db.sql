CREATE SCHEMA if not exists "ratings-schema" AUTHORIZATION "ratings-user";
SET search_path TO "ratings-schema";

CREATE TABLE IF NOT EXISTS "ratings-schema".ratings (
    id SERIAL UNIQUE PRIMARY KEY,
    model_version VARCHAR(30),
    translation_id VARCHAR(30),
    rating INTEGER
);

GRANT USAGE ON SCHEMA "ratings-schema" TO "ratings-user";
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA "ratings-schema" TO "ratings-user";
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA "ratings-schema" TO "ratings-user";

alter role "ratings-user" set search_path = "ratings-schema"