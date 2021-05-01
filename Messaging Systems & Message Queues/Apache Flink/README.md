## Instructions for running `flink_actor.py`

- to run [`flink_actor.py`](./flink_actor.py) you will need to set up a directory on an Ubuntu 20.04 machine
 - example directory structure:
    ```
   .
   ├── flink_actor.py
   ├── inputs
   │   ├── input_large.txt
   │   ├── input_medium.txt
   │   ├── input_small.txt
   │   ├── input_tiny.txt
   │   └── input_xlarge.txt
   ├── outputs
   └── perf
   ├── large
   ├── medium
   ├── small
   ├── tiny
   └── xlarge
    ```
- with the correct directory structure the program can be run with the following command:
    ```
    python3 flink_actor.py {input_file_name} {size} {test_number}
    ```
  - where input_file_name is `input_tiny.txt`, `input_small.txt`, `input_medium.txt`, `input_large.txt`, or `input_xlarge.txt`
  - size is `tiny`, `small`, `medium`. `large`, or `xlarge`
  - test_number is `0, 1, 2, ... , N`

#### Memory Usage
- to gather performance data on memory usage, please install the Python package, `memory_profiler`:
    ```
    pip3 install -U memory_profiler
    ```
- then run the program with:
    ```
    mprof run flink_actor.py {input_file_name} {size} {test_number}
    ```
- followed by `mprof plot` in the same directory as `flink_actor.py` to see a visualization


#### CPU Usage
- to gather performance data on CPU usage, use this command from with the `outputs` directory of the above tree:
    ```
    pidstat -C "python3|java" 1 | tee -a ./cpuusage_{N}.txt
    ```
  - replace N with your test number
  - `pidstat` is a sub-tool of `sysstat`, which can be downloaded with apt:
    ```
    sudo apt install sysstat
    ```