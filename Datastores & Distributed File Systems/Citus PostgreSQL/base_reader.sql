DO
$do$
DECLARE
	i INT;
BEGIN
	FOR i in 1..10000
		LOOP
			PERFORM *
			FROM data
			ORDER BY id asc
			LIMIT 1 OFFSET i;
			INSERT INTO data (reader_id, end_time) VALUES (1, clock_timestamp());
		end LOOP;
END;
$do$;
