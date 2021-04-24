
db.createCollection('cap_test')

for (var i =0; i < 1000000; i +=2) {
	db.cap_test.insert({
		_id: i,
		data: "DY3JRAYARCMTRA3FNR33XK9JD3DWSRHG1FRCFT66JERU3G9XSYPLUGEVZAV2RG99WNLK05IE4ML6M78PIN7UA7XCJ8SD1V1A9HHDK8JKMWB0XY0PFD666LRU9PR8MTL6",
		writer_id: 1,
		start_time: new Date()
	})
}


for (var i =1; i < 1000000; i+=2) {
	db.cap_test.insert({
		_id: i,
		data: "DY3JRAYARCMTRA3FNR33XK9JD3DWSRHG1FRCFT66JERU3G9XSYPLUGEVZAV2RG99WNLK05IE4ML6M78PIN7UA7XCJ8SD1V1A9HHDK8JKMWB0XY0PFD666LRU9PR8MTL6",
		writer_id: 2,
		start_time: new Date()
	})
}


for (var i = 0; i <=1000; i++) {
	db.cap_test.update({ _id: i }, {$set: {reader_id: 1, end_time: new Date()}})
}

for (var i = 1001; i <=2000; i++) {
	db.cap_test.update({ _id: i }, {$set: {reader_id: 2, end_time: new Date()}})
}












