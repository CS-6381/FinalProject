from datetime import datetime
from math import floor
from typing import List


class ThroughputCalculator:
    @staticmethod
    def calculate_throughput(send_times) -> List[int]:
        """
        Takes a sorted list of send times and calculates a list of throughput (messages sent per second)
        :param send_times: A list of send times
        :type send_times: List[datetime]
        :return: A list of throughput
        """
        buckets = {}
        start_time = send_times[0]

        for send_time in send_times:
            key = floor((send_time - start_time).total_seconds())
            if key in buckets:
                buckets[key] += 1
            else:
                buckets[key] = 1

        end_key = list(buckets.keys())[-1]
        result = []
        for i in range(end_key + 1):
            if i not in buckets:
                result.append(0)
                continue

            result.append(buckets[i])

        return result
