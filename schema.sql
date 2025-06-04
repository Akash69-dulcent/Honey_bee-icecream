-- DROP TABLE IF EXISTS users;

-- CREATE TABLE users (
--    id INTEGER PRIMARY KEY AUTOINCREMENT,
--    username TEXT UNIQUE NOT NULL,
--    email TEXT UNIQUE NOT NULL,
--    contact TEXT UNIQUE NOT NULL,
--    mesage TEXT UNIQUE NOT NULL,
--    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
-- );

-- -- Initial test data
-- INSERT INTO users (username, email, contact, mesage) VALUES
--    ('john_doe', 'john@example.com', '555-1234', 'Hello from John'),
--    ('jane_smith', 'jane@example.com', '555-5678', 'Hello from Jane'),
--    ('bob_johnson', 'bob@example.com', '555-9012', 'Hello from Bob');