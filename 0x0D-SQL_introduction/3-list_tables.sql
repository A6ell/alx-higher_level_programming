-- Lists all tables in a database passed as arg to mysql cmd
USE mysql;
SELECT table_name
FROM information_schema.tables
WHERE table_type = 'BASE TABLE'
  AND table_schema = DATABASE();