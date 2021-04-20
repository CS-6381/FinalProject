import csv
from datetime import datetime
from typing import List, Tuple


class ProducerFileParser:
    @staticmethod
    def parse_file_contents(file_contents) -> Tuple[List[datetime], List[datetime]]:
        """
        Parses a producer file's contents and stores its data
        :param file_contents: Contents of a producer file
        :type file_contents: str
        :return: Tuple of send times and receive times sorted
        """
        rows = list(csv.reader(file_contents.splitlines()))
        send_times = []
        receive_times = []
        for row in rows:
            send_times.append(datetime.fromtimestamp(float(row[0])))
            receive_times.append(datetime.fromtimestamp(float(row[1])))
        return send_times, receive_times

    @staticmethod
    def parse_file(file_path) -> Tuple[List[datetime], List[datetime]]:
        """
        Parses a producer file and stores its data
        :param file_path: Path to the producer file
        :type file_path: str
        :return: Tuple of send times and receive times sorted
        """
        with open(file_path, 'r') as f:
            return ProducerFileParser.parse_file_contents(f.read(file_path))
