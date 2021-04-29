import datetime
import csv
import sys
from pathlib import Path
import statistics
import math

sns_csv_data = None
lambda_csv_data = None

sns_thr_grp = None
sns_dt = []
lambda_dt = []


def extract_sns_csv(size):
    global sns_csv_data
    message_dir = "{}/Messaging Systems & Message Queues/AWS SNS/Results/test_results/".format(str(Path(__file__).parents[3]))
    rows = []
    fields = []
    if size == 'tiny-1-1':
        with open(message_dir + 'tiny-1-1/sns-1-1-tiny.csv', 'r') as file:
            csvreader = csv.reader(file)
            fields = next(csvreader)
            for row in csvreader:
                rows.append(row)
            sns_csv_data = rows
    elif size == 'small':
        with open(message_dir + 'small-1-1/sns-small-1-1.csv', 'r') as file:
            csvreader = csv.reader(file)
            fields = next(csvreader)
            for row in csvreader:
                rows.append(row)
            sns_csv_data = rows
    elif size == 'medium':
        with open(message_dir + 'medium-1-1/sns-medium-1-1.csv', 'r') as file:
            csvreader = csv.reader(file)
            fields = next(csvreader)
            for row in csvreader:
                rows.append(row)
            sns_csv_data = rows
    elif size == 'large':
        with open(message_dir + 'large-1-1/sns-large-1-1.csv', 'r') as file:
            csvreader = csv.reader(file)
            fields = next(csvreader)
            for row in csvreader:
                rows.append(row)
            sns_csv_data = rows
    else:
        print("No size provided!!!")


def extract_lambda_csv(size):
    global lambda_csv_data
    message_dir = "{}/Messaging Systems & Message Queues/AWS SNS/Results/test_results/".format(str(Path(__file__).parents[3]))
    rows = []
    fields = []
    if size == 'tiny':
        with open(message_dir + 'tiny-1-1/lambda-1-1-tiny.csv', 'r') as file:
            csvreader = csv.reader(file)
            fields = next(csvreader)
            for row in csvreader:
                rows.append(row)
            lambda_csv_data = rows
    elif size == 'small':
        with open(message_dir + 'small-1-1/lambda-small-1-1.csv', 'r') as file:
            csvreader = csv.reader(file)
            fields = next(csvreader)
            for row in csvreader:
                rows.append(row)
            lambda_csv_data = rows
    elif size == 'medium':
        with open(message_dir + 'medium-1-1/lambda-medium-1-1.csv', 'r') as file:
            csvreader = csv.reader(file)
            fields = next(csvreader)
            for row in csvreader:
                rows.append(row)
            lambda_csv_data = rows
    elif size == 'large':
        with open(message_dir + 'large-1-1/lambda-large-1-1.csv', 'r') as file:
            csvreader = csv.reader(file)
            fields = next(csvreader)
            for row in csvreader:
                rows.append(row)
            lambda_csv_data = rows
    else:
        print("No size provided!!!")


def calc_sns_data():
    global sns_dt
    global sns_thr_grp
    current_second = None
    counts = {}
    dwell = {}
    for row in sns_csv_data:
        _dt = datetime.datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S.%f")
        sns_dt.append(_dt)
        _rv = '{}.{}.{}'.format(_dt.hour, _dt.minute, _dt.second)
        if current_second is None:
            current_second = _rv

        if _rv == current_second:
            if counts.get(current_second):
                counts[current_second] += 1
                dwell[current_second].append(row[2])
            else:
                counts[current_second] = 1
                dwell[current_second] = list()
                dwell[current_second].append(row[2])
        else:
            current_second = _rv
            counts[current_second] = 1
            dwell[current_second] = list()
            dwell[current_second].append(row[2])

    sns_thr_grp = counts
    minimum = min(counts.values())
    maximum = max(counts.values())
    average = math.ceil(sum(counts.values())/len(counts.values()))
    st_dev = math.ceil(statistics.pstdev(counts.values()))
    print("---THROUGHPUT PROCESSING---")
    print("Min: {}".format(minimum))
    print("Max: {}".format(maximum))
    print("Average: {}".format(average))
    print("Standard Dev.: {}".format(st_dev))


def calc_lambda_data():
    global lambda_dt
    for row in lambda_csv_data:
        if "START" not in row[1]:
            pass
        else:
            _dt = datetime.datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S.%f")
            lambda_dt.append(_dt)

    res_dt_diff = []
    ind = min([len(lambda_dt), len(sns_dt)])
    for i in range(0, ind-1):
        _td = abs(lambda_dt[i] - sns_dt[i]).total_seconds() * 1000
        res_dt_diff.append(_td)

    minimum = min(res_dt_diff)
    maximum = max(res_dt_diff)
    average = math.ceil(sum(res_dt_diff)/len(res_dt_diff))
    st_dev = math.ceil(statistics.pstdev(res_dt_diff))
    print("--- PROCESSING LATENCY ---")
    print("Min: {}".format(minimum))
    print("Max: {}".format(maximum))
    print("Average: {}".format(average))
    print("Standard Dev.: {}".format(st_dev))

    cur_window = 0
    thr_time = {}
    win_aves = []
    for key, val in sns_thr_grp.items():
        try:
            if val == 1:
                thr_time[key] = []
                thr_time[key].append(res_dt_diff[cur_window])
            else:
                try:
                    thr_time[key] = res_dt_diff[cur_window:cur_window+val]
                except Exception:
                    import pdb;pdb.set_trace()
            cur_window += val
        except Exception:
            pass
    thr_time = {k: v for k, v in thr_time.items() if v}

    for grp in thr_time.values():
        win_aves.append(sum(grp)/len(grp))

    minimum = min(win_aves)
    maximum = max(win_aves)
    average = math.ceil(sum(win_aves) / len(win_aves))
    st_dev = math.ceil(statistics.pstdev(win_aves))
    print("--- SEND THROUGHPUT ---")
    print("Min: {}".format(minimum))
    print("Max: {}".format(maximum))
    print("Average: {}".format(average))
    print("Standard Dev.: {}".format(st_dev))




if __name__ == "__main__":
    csv_size = sys.argv[1]
    extract_sns_csv(csv_size)
    extract_lambda_csv(csv_size)
    calc_sns_data()
    calc_lambda_data()
