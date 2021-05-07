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
			UPDATE data SET reader_id = 1, end_time = clock_timestamp()
			WHERE id = i;
		end LOOP;
END;
$do$;
