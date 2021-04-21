from datetime import datetime
from functools import reduce

from latency_calculator import LatencyCalculator
from producer_file_parser import ProducerFileParser
from throughput_calculator import ThroughputCalculator

data_file_1 = """1618796975.9884315,1618796977.9907966
1618796977.9908154,1618796979.9909422
1618796979.9909608,1618796980.9920914
1618796980.9921165,1618796984.996257
1618796984.9962823,1618796990.0014307"""
data_file_1_send_times = [
    datetime.fromtimestamp(1618796975.9884315),
    datetime.fromtimestamp(1618796977.9908154),
    datetime.fromtimestamp(1618796979.9909608),
    datetime.fromtimestamp(1618796980.9921165),
    datetime.fromtimestamp(1618796984.9962823)
]

data_file_1_receive_times = [
    datetime.fromtimestamp(1618796977.9907966),
    datetime.fromtimestamp(1618796979.9909422),
    datetime.fromtimestamp(1618796980.9920914),
    datetime.fromtimestamp(1618796984.996257),
    datetime.fromtimestamp(1618796990.0014307)
]

data_file_2 = """1618796975.9885576,1618796977.9906356
1618796977.9906676,1618796980.9938157
1618796980.9938347,1618796982.9944143
1618796982.99444,1618796986.9984226
1618796986.9984486,1618796991.0024216"""

data_file_1_2_send_times = [
    datetime.fromtimestamp(1618796975.9884315),
    datetime.fromtimestamp(1618796975.9885576),
    datetime.fromtimestamp(1618796977.9906676),
    datetime.fromtimestamp(1618796977.9908154),
    datetime.fromtimestamp(1618796979.9909608),
    datetime.fromtimestamp(1618796980.9921165),
    datetime.fromtimestamp(1618796980.9938347),
    datetime.fromtimestamp(1618796982.99444),
    datetime.fromtimestamp(1618796984.9962823),
    datetime.fromtimestamp(1618796986.9984486),
]

data_file_3 = """1618796975.9886746,1618796976.98973
1618796976.9897416,1618796979.9904249
1618796979.99045,1618796983.9944057
1618796983.9944315,1618796985.9965658
1618796985.996591,1618796990.9984198"""


def test_producer_file_parser_parses_file():
    send_times, receive_times = ProducerFileParser.parse_file_contents(data_file_1)
    assert len(send_times) == 5
    assert len(receive_times) == 5
    assert send_times[0] == datetime.fromtimestamp(1618796975.9884315)
    assert receive_times[0] == datetime.fromtimestamp(1618796977.9907966)
    assert send_times[-1] == datetime.fromtimestamp(1618796984.9962823)
    assert receive_times[-1] == datetime.fromtimestamp(1618796990.0014307)


def test_producer_file_parser_collect():
    parser = ProducerFileParser()
    parser.collect(ProducerFileParser.parse_file_contents(data_file_1))
    parser.collect(ProducerFileParser.parse_file_contents(data_file_2))
    parser.collect(ProducerFileParser.parse_file_contents(data_file_3))
    assert len(parser.send_times) == 15
    assert len(parser.receive_times) == 15
    assert parser.send_times[0] == datetime.fromtimestamp(1618796975.9884315)
    assert parser.send_times[-1] == datetime.fromtimestamp(1618796986.9984486)
    assert parser.receive_times[0] == datetime.fromtimestamp(1618796976.98973)
    assert parser.receive_times[-1] == datetime.fromtimestamp(1618796991.0024216)


def test_data_calculator_calculate_latencies():
    latencies = LatencyCalculator.calculate_latencies(data_file_1_send_times, data_file_1_receive_times)
    assert len(latencies) == 5
    assert latencies[0] == 2002
    assert latencies[-1] == 5005


def test_throughput_calculator_calculate_throughput_1():
    throughput = ThroughputCalculator.calculate_throughput(data_file_1_send_times)
    # 10 seconds total
    assert len(throughput) == 10
    # throughput at second 1 is 1
    assert throughput[0] == 1
    # throughput at second 2 is 0
    assert throughput[1] == 0
    # throughput at second 3 is 1
    assert throughput[2] == 1
    # second to last throughput is 0
    assert throughput[-2] == 0
    # last throughput is 1
    assert throughput[-1] == 1
    # the sum of the throughput should be the total number of messages sent
    assert reduce(lambda a, b: a + b, throughput, 0) == 5


def test_throughput_calculator_calculate_throughput_2():
    throughput = ThroughputCalculator.calculate_throughput(data_file_1_2_send_times)
    # 12 seconds total
    assert len(throughput) == 12
    # throughput at second 1 is 2
    assert throughput[0] == 2
    # throughput at second 2 is 0
    assert throughput[1] == 0
    # throughput at second 3 is 2
    assert throughput[2] == 2
    # second to last throughput is 0
    assert throughput[-2] == 0
    # last throughput is 1
    assert throughput[-1] == 1
    # the sum of the throughput should be the total number of messages sent
    assert reduce(lambda a, b: a + b, throughput, 0) == 10
