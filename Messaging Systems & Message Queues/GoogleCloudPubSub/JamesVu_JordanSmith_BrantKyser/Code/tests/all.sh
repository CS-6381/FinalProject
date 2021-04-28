# Run all tests.
source config.sh
for f in *Test.sh; do
    bash "$f"
    sleep $waitTime
done