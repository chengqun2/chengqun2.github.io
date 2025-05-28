### create knowledge base in postgres vector. 
```
create extension if not exists vector;
create table documents (
  id bigserial primary key,
  content text not null,
  metadata jsonb,
  embedding vector(1024)
);

NOTIFY pgrst, 'reload schema';

CREATE OR REPLACE FUNCTION match_documents(
  query_embedding vector(1024),
  match_count int DEFAULT null,
  filter jsonb DEFAULT '{}'
) RETURNS TABLE (
  id bigint,
  content text,
  metadata jsonb,
  similarity float
) LANGUAGE plpgsql AS $$
BEGIN
  RETURN QUERY
  SELECT
    documents.id,
    documents.content,
    documents.metadata,
    1 - (documents.embedding <=> query_embedding) AS similarity
  FROM documents
  WHERE documents.metadata @> filter
  ORDER BY documents.embedding <=> query_embedding
  LIMIT match_count;
END;
$$;
```