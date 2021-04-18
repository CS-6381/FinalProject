# Uncomment all commented out sections to do this: After manually creating table, running server, inserting 1 record, and continuously running 1 writer, run 10 readers, 1 by 1, before turning off server and dropping table. Leave commented out as is: just run readers.

source config.sh
# create
# $header "cd ..; python3 capAnalysis.py; bash" & sleep 5
# $header "curl 'http://localhost:5000/i/1'; bash" & sleep 5
# $header "curl 'http://localhost:5000/u/1'; bash" & sleep 5
$header "python3 readIteration.py 10; bash" & sleep 180
$header 'pkill -f capAnalysis.py'
# drop