-- Lists all the cities of California that can be found in the database hbtn_0d_usa
<<<<<<< HEAD
SELECT id, name
FROM cities
WHERE state_id = (
	SELECT id FROM states
	WHERE name = 'California';
)
ORDER BY id ASC;
=======
SELECT * FROM states
WHERE name = 'California';
>>>>>>> 6acb4fa1b1e2ea4d04e759e15b86bfd8e37f8500
