CREATE TABLE
    IS601_PremiumUser(
        id int auto_increment PRIMARY KEY,
        premium tinyint(1) default 0,
        user_id int not null,
        is_active tinyint(1) default 1,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        UNIQUE KEY (id, user_id),
        FOREIGN KEY user_id REFERENCES IS601_Users(id))