import sys
import numpy as np

if len(sys.argv) == 2:
    text_file = sys.argv[1]
    try:
        output = None
        with open(text_file) as f:
            output = f.readlines()

        numbers = []
        for n in output:
            numbers += [int(n)]
        if len(numbers) > 0:
            print("Statistic Summary")
            print("mean:", np.mean(numbers))
            print("std:",  np.std(numbers))
            print("min:", np.min(numbers))
            print("max:", np.max(numbers))
        else:
            print("No numbers")
    except:
        print("File not found")
else:
    print("Please give a file name")

    




  
