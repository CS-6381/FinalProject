# Test for 1 writer, 10 readers
source config.sh
cat "w 128"
cat "w 254"
cat "w 512"
cat "w 1024"
cat "w 10000"
cat "r"
cat "r"
cat "r"
cat "r"
cat "r"
cat "r"
cat "r"
cat "r"
cat "r"
cat "r"