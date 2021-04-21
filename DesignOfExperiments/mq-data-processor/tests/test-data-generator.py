import time
import random
from math import ceil
from threading import Thread

"""
Tool to create realistic test data.
Generates all three files simultaneously like the real tests would.
"""

results = []


def generate_csv(producer_id):
    result = ''
    for i in range(5):
        result += str(time.time())
        # somewhere between 1 and 5 seconds
        sleep_seconds = ceil(random.uniform(0, 5))
        print(f'Thread {producer_id} Creating row {i + 1}. Sleeping for {sleep_seconds}...')
        time.sleep(sleep_seconds)
        result += f',{time.time()}\n'
    print(f'Thread {producer_id} Writing output')
    with open(f'./producer{producer_id}.csv', 'w') as f:
        f.write(result)
    print(f'Thread {producer_id} done')


def get_thread(producer_id):
    """
    Store id in a closure
    :param producer_id: ID of producer (used in file name)
    :return Thread
    """
    return Thread(target=lambda: generate_csv(producer_id))


for i in range(3):
    get_thread(i + 1).start()
