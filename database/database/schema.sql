
CREATE DATABASE IF NOT EXISTS ssc_chsl_analysis;
USE ssc_chsl_analysis;

CREATE TABLE IF NOT EXISTS cutoff_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    year INT NOT NULL,
    post VARCHAR(20) NOT NULL,
    category VARCHAR(10) NOT NULL,
    cutoff DECIMAL(5,2) NOT NULL,
    candidates INT NOT NULL
);
