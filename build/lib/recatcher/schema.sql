DROP TABLE IF EXISTS alert;

CREATE TABLE alert (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    manage_url,
    memo,
    src_ip,
    channel,
    time
);