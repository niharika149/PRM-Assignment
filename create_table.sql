DROP TABLE IF EXISTS countries;
CREATE TABLE countries(
country_id VARCHAR(100),
country_name VARCHAR(100)
CHECK(country_name IN('Italy','India','China')) ,
region_id decimal(10,0)
);
