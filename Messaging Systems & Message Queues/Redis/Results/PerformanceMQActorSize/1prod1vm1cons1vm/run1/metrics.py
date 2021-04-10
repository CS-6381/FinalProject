import pandas as pd

data_table = '''
| Metric | Value |
| --- | --- |
| Processing Latency Min | |
| Processing Latency Max | |
| Processing Latency Average | |
| Processing Latency Standard Deviation | |
| Send Time Min |{send_time_min} |
| Send Time Max |{send_time_max} |
| Send Time Average |{send_time_avg} |
| Send Time Standard Deviation |{send_time_stdv} |
| Processing Throughput Min | |
| Processing Throughput Max | |
| Processing Throughput Average | |
| Processing Throughput Standard Deviation | |
| Send Throughput Min |{send_through_min} |
| Send Throughput Max |{send_through_max} |
| Send Throughput Average |{send_through_avg} |
| Send Throughput Standard Deviation |{send_through_stdv} |
'''


latencies = "latencies.csv"
throughput = "throughput.csv"


def main():
    columns = ['', 'time']
    latencies_data = pd.read_csv(latencies, names=columns, skiprows=1)
    columns = ['', 'messages']
    throughput_data = pd.read_csv(throughput, names=columns, skiprows=1)
    latencies_data = latencies_data['time']
    throughput_data = throughput_data['messages']
    
    data = {}
    data['send_time_min'] = latencies_data.min()
    data['send_time_max'] = latencies_data.max()
    data['send_time_avg'] = latencies_data.mean()
    data['send_time_stdv'] = latencies_data.std()

    data['send_through_min'] = throughput_data.min()
    data['send_through_max'] = throughput_data.max()
    data['send_through_avg'] = throughput_data.mean()
    data['send_through_stdv'] = throughput_data.std()

    
    print(data_table.format(**data))
    

if __name__ == "__main__":
    main()
