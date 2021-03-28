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
    sleep(0.0001)
    print(msg)  # simulated read time


# call WRITE/READ functions
for i in range(int(1e3)):  # loop 1,000
    mock_write(f'demo string {i}')
    mock_read()
