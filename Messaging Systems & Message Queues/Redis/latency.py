import pandas as pd
import sys

def file_loader():
    pass


def main():
    pub_file = sys.argv[1] if len(sys.argv) > 1 else 'publisher.csv'

    columns = ['sent', 'recv']
    pub = pd.read_csv(pub_file, names=columns)
    sent = pub['sent'].round(5)
    recv = sub['recv'].round(5)
    

    difference = recv-sent
    rounded = difference.apply(lambda x: '%.10f' % x)
    #pd.options.display.float_format = '{:.5f}'.format
    rounded.to_csv("difference.csv")
    

if __name__ == "__main__":
    main()
