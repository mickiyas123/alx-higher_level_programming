-- script that lists all cities contained in the database hbtn_0d_usa
-- record will display: cities.id - cities.name - states.name
-- Results will be sorted in ascending order by cities.id
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id;