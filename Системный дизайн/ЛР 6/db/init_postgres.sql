CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL
);

CREATE TABLE folders (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    name VARCHAR(100) NOT NULL
);

CREATE TABLE emails (
    id SERIAL PRIMARY KEY,
    folder_id INT REFERENCES folders(id),
    subject VARCHAR(255),
    body TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Test data
INSERT INTO users (username, password_hash) VALUES ('admin', 'hashed_password');