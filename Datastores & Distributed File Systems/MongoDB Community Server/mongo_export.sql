mongoexport --host localhost --db general_db --collection one_reader --type=csv --out one_reader.csv --fields=_id,writer_id,reader_id,start_time