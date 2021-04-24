# one reader

#use database
use general_db

#create table
db.createCollection('ten_reader')

for (var i =0; i < 10000; i++) {
	db.ten_writer.insert({
		_id: i,
		data: "DY3JRAYARCMTRA3FNR33XK9JD3DWSRHG1FRCFT66JERU3G9XSYPLUGEVZAV2RG99WNLK05IE4ML6M78PIN7UA7XCJ8SD1V1A9HHDK8JKMWB0XY0PFD666LRU9PR8MTL6",
		writer_id: 1,
		start_time: new Date()
	})
}

for (var i = 0; i <=1000; i++) {
	db.ten_writer.update({ _id: i }, {$set: {reader_id: 1, end_time: new Date()}})


}

for (var i = 1001; i <=2000; i++) {
	db.ten_writer.update({ _id: i }, {$set: {reader_id: 2, end_time: new Date()}})


}

for (var i = 2001; i <=3000; i++) {
	db.ten_writer.update({ _id: i }, {$set: {reader_id: 3, end_time: new Date()}})


}

for (var i = 3001; i <=4000; i++) {
	db.ten_writer.update({ _id: i }, {$set: {reader_id: 4, end_time: new Date()}})


}
for (var i = 4001; i <=5000; i++) {
	db.ten_writer.update({ _id: i }, {$set: {reader_id: 5, end_time: new Date()}})


}
for (var i = 5001; i <=6000; i++) {
	db.ten_writer.update({ _id: i }, {$set: {reader_id: 6, end_time: new Date()}})


}
for (var i = 6001; i <=7000; i++) {
	db.ten_writer.update({ _id: i }, {$set: {reader_id: 7, end_time: new Date()}})


}
for (var i = 7001; i <=8000; i++) {
	db.ten_writer.update({ _id: i }, {$set: {reader_id: 8, end_time: new Date()}})
}

for (var i = 8001; i <=9000; i++) {
	db.ten_writer.update({ _id: i }, {$set: {reader_id: 9, end_time: new Date()}})
}

for (var i = 9001; i <10000; i++) {
	db.ten_writer.update({ _id: i }, {$set: {reader_id: 10, end_time: new Date()}})
}










