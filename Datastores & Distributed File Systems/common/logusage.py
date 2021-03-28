from logger import log_call
from time import sleep

msg = ''


@log_call
def mock_write(m):
    global msg
    sleep(0.001)  # simulate write time
    msg = m


@log_call
def mock_read():
    global msg
    sleep(0.001)  # simulate read time
    print(msg)


# call WRITE/READ functions
mock_write("demo string")
mock_read()
