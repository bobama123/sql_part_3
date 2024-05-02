
DROP TABLE IF EXISTS user_accounts CASCADE;
DROP SEQUENCE IF EXISTS user_accounts_id_seq;
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;



CREATE SEQUENCE IF NOT EXISTS user_accounts_id_seq;
CREATE TABLE user_accounts (
    id SERIAL PRIMARY KEY,
    email_address text,
    username text
);

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    content text,
    no_of_views int,
-- The foreign key name is always {other_table_singular}_id
    user_account_id int,
    constraint fk_user_account foreign key(user_account_id)
        references user_accounts(id)
        on delete cascade
);



INSERT INTO user_accounts (email_address, username) VALUES ('bob@hot.co.uk', 'bobby');
INSERT INTO user_accounts (email_address, username) VALUES ('lol@yahoo.com', 'lolol');
INSERT INTO user_accounts (email_address, username) VALUES ('yoyo@joke.com', 'yoyoyoyo');



INSERT INTO posts (title, content, no_of_views, user_account_id) VALUES ('Pixies', 'Rock', 10, 1);
INSERT INTO posts (title, content, no_of_views, user_account_id) VALUES ('ABBA', 'Pop', 2000000, 2);
INSERT INTO posts (title, content, no_of_views, user_account_id) VALUES ('Taylor Swift', 'Pop', 100, 1);
INSERT INTO posts (title, content, no_of_views, user_account_id) VALUES ('Nina Simone', 'Jazz', 0, 3);
