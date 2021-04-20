import csv
from datetime import datetime
from typing import List, Tuple


class ProducerFileParser:
    def __init__(self):
        self.send_times = []
        self.receive_times = []

    @staticmethod
    def _merge_sorted(a, b):
        # combine sorted lists https://www.geeksforgeeks.org/python-combining-two-sorted-lists/
        i = 0
        j = 0
        result = []
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                result.append(a[i])
                i += 1
            else:
                result.append(b[j])
                j += 1

        # add the remaining items
        result = result + a[i:] + b[j:]
        return result

    def _collect_send(self, send_times):
        if len(self.send_times) < 1:
            self.send_times = send_times
            return
        self.send_times = ProducerFileParser._merge_sorted(send_times, self.send_times)

    def _collect_receive(self, receive_times):
        if len(self.receive_times) < 1:
            self.receive_times = receive_times
            return
        self.receive_times = ProducerFileParser._merge_sorted(receive_times, self.receive_times)

    def collect(self, send_receive_tuple):
        """
        Collects all of the data from a send/receive tuple (from parse_file_contents) into
        the send_times and receive_times fields in sorted order
        :param send_receive_tuple: Tuple[List[datetime], List[datetime]]
        """
        self._collect_send(send_receive_tuple[0])
        self._collect_receive(send_receive_tuple[1])

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
