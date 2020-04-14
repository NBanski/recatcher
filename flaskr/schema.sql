DROP TABLE IF EXISTS alert;
DROP TABLE IF EXISTS user;

CREATE TABLE alert (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    memo,
    src_ip,
    src_data,
    channel,
    time
);

CREATE table user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQE NOT NULL,
    password TEXT NOT NULL
);