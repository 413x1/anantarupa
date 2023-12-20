CREATE TABLE users
(
    id          INT PRIMARY KEY AUTO_INCREMENT ,
    username    VARCHAR(20) NOT NULL,
    join_date   TIMESTAMP   NULL
);

INSERT INTO users (username, join_date)
VALUES  ('Kings885', '2022-07-22 00:00:00'),
        ('Cool_Guy', '2019-03-07 11:00:40'),
        ('Vicious_Hydra', '2021-04-11 13:04:06');

CREATE TABLE currencies
(
    id      INT PRIMARY KEY AUTO_INCREMENT,
    name    VARCHAR(10) NOT NULL
);

INSERT INTO currencies (name)
VALUES  ('Gold'),
        ('Silver'),
        ('Copper');

CREATE TABLE user_currencies
(
    id              INT PRIMARY KEY AUTO_INCREMENT,
    user_id         INT NOT NULL,
    currency_id     INT DEFAULT 0 NULL,
    amount          INT NULL,
    CONSTRAINT user_currencies___fk_currency_id
        FOREIGN KEY (currency_id) REFERENCES currencies (id)
            ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT user_currencies___fk_user_id
        FOREIGN KEY (user_id) REFERENCES users (id)
            ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO user_currencies (user_id, currency_id, amount)
VALUES  (1, 1, 40),
        (1, 2, 100),
        (1, 3, 50000),
        (2, 1, 3),
        (2, 2, 50),
        (2, 3, 1000),
        (3, 1, 10),
        (3, 2, 500),
        (3, 3, 20050);

CREATE TABLE items
(
    id      INT PRIMARY KEY AUTO_INCREMENT,
    name    VARCHAR(20) NOT NULL
);

INSERT INTO items (name)
VALUES  ('healing potion'),
        ('revival beads'),
        ('invincible amulet'),
        ('name changer');

CREATE TABLE catalogs (
    id INT PRIMARY KEY AUTO_INCREMENT,
    item_id INT not NULL,
    price INT NOT NULL,
  	currency_id INT NOT NULL,
    max_user_stack INT DEFAULT 0,
  	CONSTRAINT catalogs___fk_item_id
    	FOREIGN KEY (item_id) REFERENCES items (id),
  	CONSTRAINT catalogs___fk_currency_id
    	FOREIGN KEY (currency_id) REFERENCES currencies (id)
);

INSERT INTO catalogs (item_id, price, currency_id, max_user_stack)
VALUES  (1, 100, 2, 50),
        (2, 2, 1, 10),
        (4, 3000, 3, 3);


CREATE TABLE transactions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    catalog_id INT NOT NULL,
    qty INT NOT NULL,
    total_price INT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    status ENUM('success', 'failed') NOT NULL,
    CONSTRAINT transactions___fk_user_id
        FOREIGN KEY (user_id) REFERENCES users (id),
    CONSTRAINT transactions___fk_catalog_id
        FOREIGN KEY (catalog_id) REFERENCES catalogs (id)
);

CREATE TABLE user_items (
    id          INT PRIMARY KEY AUTO_INCREMENT,
    user_id     INT NOT NULL,
    item_id     INT NOT NULL,
    qty         INT DEFAULT 0,
    CONSTRAINT user_items___fk_user_id
        FOREIGN KEY (user_id) REFERENCES users (id),
    CONSTRAINT user_items___fk_item_id
        FOREIGN KEY (item_id) REFERENCES items (id)
);