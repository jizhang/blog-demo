CREATE TABLE user (id INTEGER PRIMARY KEY, username VARCHAR, password VARCHAR, last_login DATETIME);

INSERT INTO user (username, password, last_login) VALUES
('jizhang', 'password', DATETIME('now', 'localtime')),
('jerry', 'password', DATETIME('now', 'localtime'));
