import os
from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('-d', '--dir', type=str, help='Path to csv folder')
    return parser.parse_args()


def main(*kwargs):
    """
    :key csv_dir: Path to CSV directory containing all producer output files.
    """

    csv_dir = kwargs['csv_dir']
    files = os.listdir(csv_dir)



if __name__ == '__main__':
    args = parse_args()
    main()
