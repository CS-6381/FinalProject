from logger import log
from time import sleep

msg = ''


# add @log to the principle method call.

@log
def mock_write(m):
    global msg
    sleep(0.0001)  # simulated write time
    msg = m


@log
def mock_read():
    global msg
    sleep(0.0001)  # simulated read time
    print(msg)


# call WRITE/READ functions
for i in range(1000):
    mock_write(f'demo string {i}')
    mock_read()
