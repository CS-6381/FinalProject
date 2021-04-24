#writer

CREATE TABLE ten_reader (
	id integer,
	data text,
	writer_id integer,
	reader_id integer,
	start_time timestamp without time zone,
	end_time timestamp without time zone,
	cum_diff_time interval
);


DO
$do$
DECLARE
	i INT;
BEGIN
	FOR i in 1..10000
		LOOP
			INSERT INTO ten_reader (id, data, writer_id, start_time) VALUES(i , 'abc', 1, clock_timestamp());
		end LOOP;
END; 
$do$


#reader



DO
$do$
DECLARE
	i INT;
BEGIN
	FOR i in 1..1000
		LOOP
			PERFORM *
			FROM ten_reader
			LIMIT 1 OFFSET i;
			UPDATE ten_reader SET reader_id = 1, end_time = clock_timestamp()
			WHERE id = i;
		end LOOP;
END;
$do$

DO
$do$
DECLARE
	i INT;
BEGIN
	FOR i in 1001..2000
		LOOP
			PERFORM *
			FROM ten_reader
			LIMIT 1 OFFSET i;
			UPDATE ten_reader SET reader_id = 2, end_time = clock_timestamp()
			WHERE id = i;
		end LOOP;
END;
$do$

DO
$do$
DECLARE
	i INT;
BEGIN
	FOR i in 2001..3000
		LOOP
			PERFORM *
			FROM ten_reader
			LIMIT 1 OFFSET i;
			UPDATE ten_reader SET reader_id = 3, end_time = clock_timestamp()
			WHERE id = i;
		end LOOP;
END;
$do$

DO
$do$
DECLARE
	i INT;
BEGIN
	FOR i in 3001..4000
		LOOP
			PERFORM *
			FROM ten_reader
			LIMIT 1 OFFSET i;
			UPDATE ten_reader SET reader_id = 4, end_time = clock_timestamp()
			WHERE id = i;
		end LOOP;
END;
$do$

DO
$do$
DECLARE
	i INT;
BEGIN
	FOR i in 4001..5000
		LOOP
			PERFORM *
			FROM ten_reader
			LIMIT 1 OFFSET i;
			UPDATE ten_reader SET reader_id = 5, end_time = clock_timestamp()
			WHERE id = i;
		end LOOP;
END;
$do$

DO
$do$
DECLARE
	i INT;
BEGIN
	FOR i in 5001..6000
		LOOP
			PERFORM *
			FROM ten_reader
			LIMIT 1 OFFSET i;
			UPDATE ten_reader SET reader_id = 6, end_time = clock_timestamp()
			WHERE id = i;
		end LOOP;
END;
$do$

DO
$do$
DECLARE
	i INT;
BEGIN
	FOR i in 6001..7000
		LOOP
			PERFORM *
			FROM ten_reader
			LIMIT 1 OFFSET i;
			UPDATE ten_reader SET reader_id = 7, end_time = clock_timestamp()
			WHERE id = i;
		end LOOP;
END;
$do$

DO
$do$
DECLARE
	i INT;
BEGIN
	FOR i in 7001..8000
		LOOP
			PERFORM *
			FROM ten_reader
			LIMIT 1 OFFSET i;
			UPDATE ten_reader SET reader_id = 8, end_time = clock_timestamp()
			WHERE id = i;
		end LOOP;
END;
$do$

DO
$do$
DECLARE
	i INT;
BEGIN
	FOR i in 8001..9000
		LOOP
			PERFORM *
			FROM ten_reader
			LIMIT 1 OFFSET i;
			UPDATE ten_reader SET reader_id = 9, end_time = clock_timestamp()
			WHERE id = i;
		end LOOP;
END;
$do$

DO
$do$
DECLARE
	i INT;
BEGIN
	FOR i in 9001..10000
		LOOP
			PERFORM *
			FROM ten_reader
			LIMIT 1 OFFSET i;
			UPDATE ten_reader SET reader_id = 10, end_time = clock_timestamp()
			WHERE id = i;
		end LOOP;
END;
$do$