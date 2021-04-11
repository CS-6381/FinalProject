import pandas as pd

data_table = '''
| Metric | Value |
| --- | --- |
| Processing Latency Min |{processing_latency_min} |
| Processing Latency Max |{processing_latency_max} |
| Processing Latency Average | {processing_latency_avg}|
| Processing Latency Standard Deviation |{processing_latency_std} |
| Send Time Min |{send_time_min} |
| Send Time Max |{send_time_max} |
| Send Time Average |{send_time_avg} |
| Send Time Standard Deviation |{send_time_std} |
| Processing Throughput Min |{processing_through_min} |
| Processing Throughput Max |{processing_through_max}|
| Processing Throughput Average |{processing_through_avg}|
| Processing Throughput Standard Deviation |{processing_through_std}|
| Send Throughput Min |{send_through_min} |
| Send Throughput Max |{send_through_max} |
| Send Throughput Average |{send_through_avg} |
| Send Throughput Standard Deviation |{send_through_std} |
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
    data['processing_latency_min'] = latencies_data.min()
    data['processing_latency_max'] = latencies_data.max()
    data['processing_latency_avg'] = latencies_data.mean()
    data['processing_latency_std'] = "%.12f" % latencies_data.std()

    data['send_time_min'] = 'n/a'
    data['send_time_max'] = 'n/a'
    data['send_time_avg'] = 'n/a'
    data['send_time_std'] = 'n/a'

    data['processing_through_min'] = throughput_data.min()
    data['processing_through_max'] = throughput_data.max()
    data['processing_through_avg'] = throughput_data.mean()
    data['processing_through_std'] = throughput_data.std()
    
    data['send_through_min'] = 'n/a'
    data['send_through_max'] = 'n/a'
    data['send_through_avg'] = 'n/a'
    data['send_through_std'] = 'n/a'

    
    print(data_table.format(**data))
    

if __name__ == "__main__":
    main()
