import pandas as pd
import os

script_dir = os.getcwd()

def convert_to_csv(textFilePath, csvFilePath):
    textFile = os.path.join(script_dir, textFilePath)
    read_file = pd.read_csv(textFile, header = None)
    read_file.columns = ['reader_id', 'writer_id', 'key', 'start_time', 'end_time', 'delta_time']
    csvFile = os.path.join(script_dir, csvFilePath)
    read_file.to_csv(csvFile, index=None)
    print("done converting")



