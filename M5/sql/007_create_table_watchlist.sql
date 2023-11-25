CREATE TABLE
    IS601_Watchlist (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(500) NOT NULL,
        title_type VARCHAR(10) NOT NULL,
        netflix_id VARCHAR(10) NOT NULL,
        synopsis VARCHAR(1000) NOT NULL,
        rating DECIMAL(5,2) NOT NULL,
        `year` INT NOT NULL,
        imdb_id VARCHAR(10),
        title_date VARCHAR(10) NOT NULL,
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        UNIQUE KEY `title` (
            `netflix_id`,
            `imdb_id`
        )
    );