import sys
import numpy as np

text_file = sys.argv[1]

try:
    output = None
    with open(text_file) as f:
        output = f.readlines()

    numbers = []
    for n in output:
        numbers += [int(n)]
    
    print("Statistic Summary")
    print("mean:", np.mean(numbers))
    print("std:",  np.std(numbers))
    print("min:", np.min(numbers))
    print("max:", np.max(numbers))
except:
    print("File not found")


  
