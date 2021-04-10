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
    sub_round = sub['time'].round(5)
    

    difference = sub_round-pub_round
    rounded = difference.apply(lambda x: '%.10f' % x)
    #pd.options.display.float_format = '{:.5f}'.format
    rounded.to_csv("difference.txt")
    

if __name__ == "__main__":
    main()
