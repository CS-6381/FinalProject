from pyflink.common.serialization import SimpleStringEncoder
from pyflink.common.typeinfo import Types
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors import StreamingFileSink
import time
import sys


def data_transfer():
    # input file name
    input_file = sys.argv[1]
    # tiny, small, medium, large, or xlarge for writing to appropriate directory
    test_size = sys.argv[2]
    # 0 - 9 to keep track of test runs
    run_num = sys.argv[3]
    # replace { /path/to/inputs } with where you pull the data from
    # in an alternate implementation, this could be replaced with a datastore or a messaging queue
    file_string = 'file:///path/to/inputs/' + str(input_file)
    perf_file = './perf/' + str(test_size) + '/perf_' + str(run_num) + '.csv'
    start = time.time()

    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)

    ds = env.read_text_file(file_string, 'UTF-8')
    # replace { /path/to/outputs } with where you will move the data to
    # in an alternate implementation, this could be replaced with a datastore or a messaging queue
    ds.add_sink(StreamingFileSink
                .for_row_format('/path/to/outputs', SimpleStringEncoder())
                .build())

    env.execute('data_transfer_job')

    end = time.time()
    perf_file = open(perf_file, 'w+')
    perf_file.write(f'{start},{end}\n')


if __name__ == '__main__':
    data_transfer()
