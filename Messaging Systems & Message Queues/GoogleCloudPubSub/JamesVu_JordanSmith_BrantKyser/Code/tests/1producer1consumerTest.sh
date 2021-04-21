# Test for 1 Producer and 1 Consumer
source config.sh

$header "cd ..; export GOOGLE_APPLICATION_CREDENTIALS=~/Downloads/key.json; export PROJECT=`gcloud config get-value project`; python3 sub.py $projectID sub_one"
$header "cd ..; export GOOGLE_APPLICATION_CREDENTIALS=~/Downloads/key.json; export PROJECT=`gcloud config get-value project`; python3 broker.py $projectID hello_topic; bash"
$header "cd ..; export GOOGLE_APPLICATION_CREDENTIALS=~/Downloads/key.json; export PROJECT=`gcloud config get-value project`; python3 pub.py Message_22_04-11-2021_181607_89b57e25-b9f8-4b5d-8cb2-659fa06347e8" & sleep $longTime
$header 'pkill -f broker.py'
$header 'pkill -f pub.py'
$header 'pkill -f sub.py' & sleep $shortTime
$header 'cd ..; python3 clear.py' & sleep $mediumTime

$header "cd ..; export GOOGLE_APPLICATION_CREDENTIALS=~/Downloads/key.json; export PROJECT=`gcloud config get-value project`; python3 sub.py $projectID sub_one"
$header "cd ..; export GOOGLE_APPLICATION_CREDENTIALS=~/Downloads/key.json; export PROJECT=`gcloud config get-value project`; python3 broker.py $projectID hello_topic; bash"
$header "cd ..; export GOOGLE_APPLICATION_CREDENTIALS=~/Downloads/key.json; export PROJECT=`gcloud config get-value project`; python3 pub.py Message_149_04-11-2021_181604_5306f2d6-7576-4015-8d19-e85a0c89926e" & sleep $longTime
$header 'pkill -f broker.py'
$header 'pkill -f pub.py'
$header 'pkill -f sub.py' & sleep $shortTime
$header 'cd ..; python3 clear.py' & sleep $mediumTime

$header "cd ..; export GOOGLE_APPLICATION_CREDENTIALS=~/Downloads/key.json; export PROJECT=`gcloud config get-value project`; python3 sub.py $projectID sub_one"
$header "cd ..; export GOOGLE_APPLICATION_CREDENTIALS=~/Downloads/key.json; export PROJECT=`gcloud config get-value project`; python3 broker.py $projectID hello_topic; bash"
$header "cd ..; export GOOGLE_APPLICATION_CREDENTIALS=~/Downloads/key.json; export PROJECT=`gcloud config get-value project`; python3 pub.py Message_6815_04-11-2021_181559_d652d75f-dccf-4cc1-805b-9a8711d5d2d6" & sleep $longTime
$header 'pkill -f broker.py'
$header 'pkill -f pub.py'
$header 'pkill -f sub.py' & sleep $shortTime
$header 'cd ..; python3 clear.py' & sleep $mediumTime

$header "cd ..; export GOOGLE_APPLICATION_CREDENTIALS=~/Downloads/key.json; export PROJECT=`gcloud config get-value project`; python3 sub.py $projectID sub_one"
$header "cd ..; export GOOGLE_APPLICATION_CREDENTIALS=~/Downloads/key.json; export PROJECT=`gcloud config get-value project`; python3 broker.py $projectID hello_topic; bash"
$header "cd ..; export GOOGLE_APPLICATION_CREDENTIALS=~/Downloads/key.json; export PROJECT=`gcloud config get-value project`; python3 pub.py Message_155355_04-11-2021_181532_95b0ef07-4dda-42e2-88a5-f6f29a270716" & sleep $longTime
$header 'pkill -f broker.py'
$header 'pkill -f pub.py'
$header 'pkill -f sub.py' & sleep $shortTime
$header 'cd ..; python3 clear.py' & sleep $mediumTime

$header "cd ..; export GOOGLE_APPLICATION_CREDENTIALS=~/Downloads/key.json; export PROJECT=`gcloud config get-value project`; python3 sub.py $projectID sub_one"
$header "cd ..; export GOOGLE_APPLICATION_CREDENTIALS=~/Downloads/key.json; export PROJECT=`gcloud config get-value project`; python3 broker.py $projectID hello_topic; bash"
$header "cd ..; export GOOGLE_APPLICATION_CREDENTIALS=~/Downloads/key.json; export PROJECT=`gcloud config get-value project`; python3 pub.py Message_761135_04-11-2021_181612_fbefdcfd-b1f4-4904-ae12-8f5be47d591d" & sleep $longTime
$header 'pkill -f broker.py'
$header 'pkill -f pub.py'
$header 'pkill -f sub.py' & sleep $shortTime
$header 'cd ..; python3 clear.py' & sleep $mediumTime