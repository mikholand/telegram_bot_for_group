CREATE TABLE users
(
    user_id   bigint            NOT NULL
        CONSTRAINT users_pk
            PRIMARY KEY,
    username  varchar(200),
    full_name varchar(200),
    referral  bigint
);

CREATE TABLE chats
(
    chat_id   bigint            NOT NULL
        CONSTRAINT chats_pk
            PRIMARY KEY,
    title  varchar(200)
);

CREATE TABLE handsome_man
(
	user_id     bigint REFERENCES users(user_id),
	chat_id     bigint REFERENCES chats(id),
	CONSTRAINT handsome_man_pk PRIMARY KEY (user_id, chat_id),
	score       int,
	last_scored date            NOT NULL
);


ALTER TABLE users
    OWNER TO postgres;

ALTER TABLE chats
    OWNER TO postgres;

ALTER TABLE handsome_man
    OWNER TO postgres;