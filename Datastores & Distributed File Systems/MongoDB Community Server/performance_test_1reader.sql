# one reader

#use database
use general_db

#create table
db.createCollection('one_reader')


#5k values to match the size of the writers
for (var i = 0; i <=5000; i++) {
db.one_writer.find().limit(1)
db.one_reader.insert({
	_id : i,
	writer_id: "N/A",
	reader_id: 1,
	start_time: new Date()
})
}