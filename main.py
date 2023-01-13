import sys
import numpy as np
from typing import List

def getResult(file_name, array_input: List[int], calculate_from_array: bool) -> List[int]:
    try:
        output = None
        if (calculate_from_array == False):
            with open(file_name) as f:
                output = f.readlines()
                f.close()

        numbers = array_input
        if (calculate_from_array == False and output != None):
            for n in output:
                if (n.strip().isnumeric()):
                    numbers += [int(n.strip())]
                
        if calculate_from_array == False:
            print(file_name)
        print("mean:", np.mean(numbers), "std:", np.std(numbers), "min:", np.min(numbers), "max:", np.max(numbers))
        return numbers
    except:
        print("File not found")
        return []


if len(sys.argv) > 1:
    file_names = sys.argv
    total = []
    print("Statistic Summary")
    for i in range(1, len(file_names)):
        text_file = sys.argv[i]
        result = getResult(text_file, [], False)
        total += result
        print("")
    print("combined:")
    getResult(None, total, True)
else:
    print("Please give file names")

    




  
