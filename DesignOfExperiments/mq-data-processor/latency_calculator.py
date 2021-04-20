from typing import List


class LatencyCalculator:
    @staticmethod
    def calculate_latencies(send_times, receive_times) -> List[int]:
        """
        Takes a list of send times and receive times and returns a list of latencies (in milliseconds) between them
        :param send_times: List of send times, sorted
        :type send_times: List[datetime]
        :param receive_times: List of receive times, sorted
        :type receive_times: List[datetime]
        :return: List of latencies in milliseconds
        """
        result = []
        for i in range(len(send_times)):
            send_time = send_times[i]
            receive_time = receive_times[i]
            latency = receive_time - send_time
            result.append(round(latency.total_seconds() * 1000))
        return result
