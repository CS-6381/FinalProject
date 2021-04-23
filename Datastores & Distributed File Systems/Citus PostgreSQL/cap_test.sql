CREATE TABLE data (
	id integer,
	data text,
	writer_id integer,
	start_time timestamp without time zone
);

CREATE TABLE data_reader (
	reader_id integer,
	start_time timestamp without time zone,
	end_time timestamp without time zone
);


#set-up rows to write-over for writers
INSERT INTO data (id) VALUES (1);
INSERT INTO data (id) VALUES (2);

DO
$do$
DECLARE
	i INT;
BEGIN
	FOR i in 1..1000000
		LOOP
			UPDATE data SET id = 1, data = 'DY3JRAYARCMTRA3FNR33XK9JD3DWSRHG1FRCFT66JERU3G9XSYPLUGEVZAV2RG99WNLK05IE4ML6M78PIN7UA7XCJ8SD1V1A9HHDK8JKMWB0XY0PFD666LRU9PR8MTL6', writer_id = 1, start_time = clock_timestamp()
			WHERE id = 1;
		END LOOP;
END; 
$do$;


DO
$do$
DECLARE
	i INT;
BEGIN
	FOR i in 1..1000
		LOOP
			INSERT INTO data_reader(start_time) SELECT start_time FROM data WHERE writer_id = 1;
			INSERT INTO data_reader (reader_id, end_time) VALUES(1, clock_timestamp());
		END LOOP;
END;
$do$;




#for other node

DO
$do$
DECLARE
	i INT;
BEGIN
	FOR i in 1..1000000
		LOOP
			UPDATE data SET id = 2, data = 'DY3JRAYARCMTRA3FNR33XK9JD3DWSRHG1FRCFT66JERU3G9XSYPLUGEVZAV2RG99WNLK05IE4ML6M78PIN7UA7XCJ8SD1V1A9HHDK8JKMWB0XY0PFD666LRU9PR8MTL6', writer_id = 1, start_time = clock_timestamp()
			WHERE id = 2;
		END LOOP;
END; 
$do$;


DO
$do$
DECLARE
	i INT;
BEGIN
	FOR i in 1..1000
		LOOP
			INSERT INTO data_reader(start_time) SELECT start_time FROM data WHERE writer_id = 2;
			INSERT INTO data_reader (reader_id, end_time) VALUES(2, clock_timestamp());
		END LOOP;
END;
$do$;




