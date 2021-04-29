CS 6381 Final Project Google Cloud Pub Sub Setup:

Plan:

Have the publisher send messages continuously to the broker via ZMQ,
which send messages continuously to the subscriber via Google Cloud, and
when the subscriber receives a specific number of messages, it creates a
CSV file which saves in the timeMeasurements folder and terminates.
Repeat this process for different text-sized messages in the messages
folder.

Procedure:

1.  Set up Google Cloud Pub Sub

    a.  Set up Pub Sub
        (<https://cloud.google.com/pubsub/docs/building-pubsub-messaging-system>,
        <https://www.youtube.com/watch?v=UKAmZBrR300&amp;loop=0>)

        i.  Spin up a Ubuntu 18.04 VM.

        ii. Install Google Cloud SDK on Ubuntu:
            <https://cloud.google.com/sdk/docs/install>

        iii. Put \`\` like where it shows export PROJECT=\`gcloud config
             get-value project\`

        iv. Rename your JSON key to something simple like key.json and
            put it somewhere simple to access like in the Downloads
            folder with respect to the root folder.

2.  To run code each time:

    a.  Automatically

        i.  Navigate to the tests folder and run a test using "./{{test
            name}}" (e. g. "./1producer1consumerTest.sh"). Wait until
            the test finishes (i. e. when all extra terminal tabs have
            closed \[the last one takes a little while to show up\]) and
            then check for results in the timeMeasurements folder.

    b.  Manually

        i.  Open 3 separate terminals or tabs and run each of the
            following separately in this order, applying the "Connect to
            Google Cloud Project" step as follows at the start of all
            the subsequent steps (sub.py, pub.py, broker.py).

            1.  Connect to Google Cloud project.

                a.  export
                    GOOGLE_APPLICATION_CREDENTIALS=\~/Downloads/key.json

                b.  export PROJECT=\`gcloud config get-value project\`

                c.  echo \$PROJECT (make sure project ID shows up)

            2.  Run sub.py:

                a.  "python3 sub.py \$PROJECT {{Google Cloud-created
                    subscription name (e. g. sub_one)}}"

            3.  Run broker.py:

                a.  "python3 broker.py \$PROJECT {{Google Cloud-created
                    topic name (e. g. hello_topic}}"

            4.  Run pub.py:

                a.  \"python3 pub.py {{file name}}\"

        ii. To stop the code properly using Ctrl + C:

            1.  Stop broker.py 1^st^ or else sub.py will receive old
                messages.

            2.  Empty out old messages by 1 of the following ways:

                a.  Run "python3 clear.py".

                b.  Start sub.py and wait until all old messages are
                    emptied out and then stop it before running the code
                    again.

3.  Run python3 calculateStatistics.py or calculateStatisticsAll.py to calculate statistics
            of time measurements and for the latter, also generate graphs.

4.  You can measure hardware performance continuously by running
    hardwareMeasure.py, which will print the latest information.

5.  You can generate a new message file that holds a specific number of
    random characters by running messageGenerator.py and specifying that
    number with a command line argument.

Conditions to Test:

-   1 producer vs. 1 consumer

-   1 producer vs. 5 consumers

-   5 producers vs. 1 consumer

-   3 x (8 producers vs. 8 consumers)

-   4 x (25 producers vs. 25 consumers)
