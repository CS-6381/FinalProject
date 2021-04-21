#!/usr/bin/env bash

# Pre-set variables
time1="5"
time2="10"
waitTime="5"
iterations="10"
header="gnome-terminal -- bash -c"

# Concatenate arguments as a function to run.
function cat ()
{
    bash -c "cd ..; sudo xterm -T 'cassandraRW' -e python3 cassandraRW.py $iterations $1" & sleep $time1
}

function create ()
{
    bash -c "cd ..; sudo xterm -T 'table' -e python3 table.py c int" & sleep $time1
}

function drop ()
{
    bash -c "cd ..; sudo xterm -T 'table' -e python3 table.py d" & sleep $time1
}

# Extract file name.
function get ()
{
    testPath=$(readlink -f "$1")
    testFile=$(basename "$testPath")
    testExt=".sh"
    testName="${testFile//$testExt/}"
    echo $testName
}