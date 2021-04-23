# one writer

#create database
use general_db

#create table
db.createCollection('one_writer')


#insert rows in for loop
#smallest size insert
for (var i =0; i <= 1000; i++) {
	db.one_writer.insert({
		_id: i,
		data: "abc",
		writer_id: 1,
		reader_id: "n/a",
		start_time: new Date()
	})
}

#next insert size
for (var i =0; i <= 1000; i++) {
	db.one_writer.insert({
		_id: i,
		data: "abc",
		writer_id: 1,
		reader_id: "n/a",
		start_time: new Date()
	})
}

#next insert size
for (var i =0; i <= 1000; i++) {
	db.one_writer.insert({
		_id: i,
		data: "abc",
		writer_id: 1,
		reader_id: "n/a",
		start_time: new Date()
	})
}

#next insert size
for (var i =0; i <= 1000; i++) {
	db.one_writer.insert({
		_id: i,
		data: "abc",
		writer_id: 1,
		reader_id: "n/a",
		start_time: new Date()
	})
}

#max insert size
for (var i =0; i <= 1000; i++) {
	db.one_writer.insert({
		_id: i,
		data: "abc",
		writer_id: 1,
		reader_id: "n/a",
		start_time: new Date()
	})
}





