
USE ssc_chsl_analysis;

LOAD DATA INFILE 'ssc_chsl_cutoff_data.csv'
INTO TABLE cutoff_data
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(year, post, category, cutoff, candidates);
