-- pgvector stub, demo does not connect
CREATE EXTENSION IF NOT EXISTS vector;
CREATE TABLE IF NOT EXISTS documents (id serial primary key, project text, content text, embedding vector(1536));
