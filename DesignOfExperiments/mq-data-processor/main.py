import csv
import os
from argparse import ArgumentParser
from latency_calculator import LatencyCalculator
from producer_file_parser import ProducerFileParser
from throughput_calculator import ThroughputCalculator


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('-d', '--dir', type=str, help='Path to csv folder')
    return parser.parse_args()


def main(**kwargs):
    """
    :key csv_dir: Path to CSV directory containing all producer output files.
    """

    csv_dir = kwargs['csv_dir']
    files = os.listdir(csv_dir)
    parser = ProducerFileParser()
    for file in files:
        if not file.endswith('csv'):
            print(f'Skipping file {file} because it doesnt end with "csv"')
            continue
        print(f'Processing file {file}')
        parser.collect(parser.parse_file(f'{csv_dir}/{file}'))
    print('Writing latencies to latencies.csv')
    with open('latencies.csv', 'w') as f:
        csv_writer = csv.writer(f)
        for latency in parser.latencies:
            csv_writer.writerow([latency])
    print('Generating throughput...')
    throughput = ThroughputCalculator.calculate_throughput(parser.send_times)
    print('Writing throughput to throughput.csv')
    with open('throughput.csv', 'w') as f:
        csv_writer = csv.writer(f)
        for t in throughput:
            csv_writer.writerow([t])
    print('Done')


if __name__ == '__main__':
    args = parse_args()
    main(csv_dir=args.dir)
