from collections import Counter

import pandas as pd


def file_loader():
    pass


def main():
    pub_file = sys.argv[1] if len(sys.argv) > 1 else 'publisher.csv'

    columns = ['sent', 'recv']
    pub = pd.read_csv(pub_file, names=columns)
    recv = sub['recv']
    
    rounded = recv.apply(lambda x: '%.1f' % x)
    #pd.options.display.float_format = '{:.5f}'.format
    times = rounded.values.tolist()
    times_count = Counter(times)
    low = min(times_count)
    times_dict = {"%.1f" % (float(t)-float(low)):times_count[t] for t in times_count}
    
    through = pd.DataFrame.from_dict(times_dict, orient="index", columns=['messages'])
    
    through.to_csv("throughput.csv")
    

if __name__ == "__main__":
    main()
