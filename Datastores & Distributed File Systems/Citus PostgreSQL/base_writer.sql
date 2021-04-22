DO
$do$
DECLARE
	i INT;
BEGIN
	FOR i in 1..10000
		LOOP
			PERFORM *
			FROM w25_r25
			ORDER BY id asc
			LIMIT 1 OFFSET i;
			UPDATE w25_r25 SET reader_id = 3, end_time = clock_timestamp()
			WHERE id = i;
		end LOOP;
END;
$do$;

