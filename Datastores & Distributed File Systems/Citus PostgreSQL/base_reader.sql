DO
$do$
DECLARE
	i INT;
BEGIN
	FOR i in 8001..10000
		LOOP
			PERFORM *
			FROM reader10
			ORDER BY id asc
			LIMIT 1 OFFSET i;
			INSERT INTO w25_r25 (reader_id, end_time) VALUES (5, clock_timestamp());
		end LOOP;
END;
$do$;