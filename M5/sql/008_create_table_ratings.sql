CREATE TABLE
    IS601_Ratings (
        id INT AUTO_INCREMENT PRIMARY KEY,
        watchlist_id INT,
        ratings DECIMAL NOT NULL,
        heading VARCHAR(100) NOT NULL,
        comments TEXT,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (watchlist_id) REFERENCES IS601_Watchlist(id)
    );