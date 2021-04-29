CS 6381 Final Project Cassandra Setup:

General:

1.  Spin up a Ubuntu VM (e. g. 18.04).

2.  Install Cassandra.

    a.  sudo apt install openjdk-8-jre-headless

    b.  cd /usr/lib/jvm/java-8-openjdk-amd64

    c.  sudo nano \~/.bashrc

    d.  Scroll to bottom of page and add in
        "JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64"

    e.  Save the file using Ctrl + S on Windows or Command + S on Mac
        and then exit out using Ctrl + X on Windows or Command + X on
        Mac.

    f.  Reopen a new terminal.

    g.  echo \$JAVA_HOME = See if above setup works.

    h.  sudo apt install curl

    i.  echo \"deb http://downloads.apache.org/cassandra/debian 39x
        main\" \| sudo tee -a
        /etc/apt/sources.list.d/cassandra.sources.list

    j.  curl https://downloads.apache.org/cassandra/KEYS \| sudo apt-key
        add -

    k.  sudo apt-get update

    l.  sudo apt-get install cassandra

3.  Run Cassandra.

    a.  Start: sudo service cassandra start

    b.  Check status: sudo service cassandra status (should see "active
        (running)")

    c.  Stop: sudo service cassandra stop

    d.  If Cassandra stops after some time (e. g. Python application
        stops connecting to Cassandra), do the stop command then start
        command.

4.  Create keyspace and table.

    a.  Open Cassandra terminal: cqlsh

    b.  Create keyspace (kind of like a schema): Create KeySpace
        {{keyspace name (e. g. cs6381finalprojectks1)}} with replication
        = {'class': 'SimpleStrategy', 'replication_factor': 3};

    c.  Show all keyspaces: SELECT \* FROM system_schema.keyspaces;

    d.  Select keyspace: use {{your keyspace name}}

    e.  Create table: Create Table table1(id {{id or uuid depending on
        use}} Primary Key, message text);

    f.  Drop table: drop table {{table name (e. g. table1}}

5.  Run code.

    a.  Manually

        i.  Navigate to Code folder and run python3 cassandraRW.py
            accordingly to run writers/readers.

        ii. Run python3 calculateStatistics.py or calculateStatisticsAll.py to calculate statistics
            of time differences and for the latter, also generate graphs.

        iii. Run python3 capAnalysis.py to get CAP-related times.

    b.  Tests

        i.  Navigate to Code/tests folder and run a test (e. g. to run
            all.sh, which runs all the tests in that folder, run
            "./all.sh").

Procedure:

1.  Run hardwareMeasure.py, which will continuously run so the user can
    constantly see the latest max and average statistics. After running
    all conditions as follows, add latest statistics to base file table.

2.  cassandraRW.py

    a.  1 x 1writerTest

    b.  1 x 1readerTest

    c.  10 x 10writer1readerTest

    d.  10 x 1writer10readerTest

    e.  5 x 25writer25readerTest

3.  capAnalysis.py - Run test in 1 of the following ways.

    a.  Way 1

        i.  Create table, run server, insert, and continuously update.

        ii. 10 x: Run readIteration.py with a parameter of
            10 for 10 iterations.

    b.  Way 2

        i.  10 x 1insert1write10readTest
