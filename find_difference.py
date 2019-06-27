# data handling library
import numpy as np
import pandas as pd
import string
import glob
import time

###reading csv files
res1_dir = r"Result_v1.csv"
read_rs1 = pd.read_csv(res1_dir, sep='|', index_col=0, header=0, error_bad_lines=False, encoding="utf-8")
read_rs1.fillna(0, inplace=True)

res2_dir = r"Result_v2.csv"
read_rs2 = pd.read_csv(res2_dir, sep='|', index_col=0, header=0, error_bad_lines=False, encoding="utf-8")
read_rs2.fillna(0, inplace=True)

###check if some differences have between the files
if read_rs1.equals(read_rs2) is False:
    print('Find some differences!')
    ####### looking for differences
    resBool = (read_rs1 != read_rs2).stack()  # Create Frame of comparison booleans
    find_diff = pd.concat([read_rs1.stack()[resBool], read_rs2.stack()[resBool]], axis=1)
    find_diff.columns = ["Result_v1", "Result_v2"]
    print(find_diff)
    with open("differences.txt", 'w') as d:
        d.write(str(find_diff))
        d.close()
    print('Differences has been saved in text file')
    time.sleep(5)

else:
    print('No differences are found!')
