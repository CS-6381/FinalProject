from collections import Counter

import pandas as pd

pub_file = "pub_out.txt"
sub_file = "sub_out.txt"



def file_loader():
    pass


def main():
    columns = ['topic', 'role', 'uuid', 'id', 'time']
    pub = pd.read_csv(pub_file, names=columns)
    sub = pd.read_csv(sub_file, names=columns)
    pub_round = pub['time'].round(5)
    sub_round = sub['time']
    
    rounded = sub_round.apply(lambda x: '%.1f' % x)
    #pd.options.display.float_format = '{:.5f}'.format
    times = rounded.values.tolist()
    times_count = Counter(times)
    low = min(times_count)
    times_dict = {"%.1f" % (float(t)-float(low)):times_count[t] for t in times_count}
    
    through = pd.DataFrame.from_dict(times_dict, orient="index", columns=['messages'])
    
    through.to_csv("throughput.csv")
    

if __name__ == "__main__":
    main()
