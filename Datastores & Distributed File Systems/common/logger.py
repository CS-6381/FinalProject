
from datetime import datetime


def log(func):
    def wrapper(*args):

        t1 = datetime.now()
        result = func(*args)
        t2 = datetime.now()

        ts1 = datetime.timestamp(t1)
        ts2 = datetime.timestamp(t2)

        with open('output.txt', 'a') as log_file:
            # FUNC_NAME|before time|after time|Time Lapse
            log_file.write(
                f'{func.__name__}|{args}|{t1}|{t2}|{float(ts2-ts1)}\n')

        return result

    return wrapper
