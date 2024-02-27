import csv    
import numpy as np

with open("./toy.csv", "r") as csvfile:
        input = csv.reader(csvfile, delimiter=",")
        next(input)
        count = len(csvfile)
        print(count)
        # years = np.array((count, 2))
        # duration = np.array((count, 1))
        # count = 0
        # for line in input:
        #     years[count] = [1, line[0]]
        #     duration[count] = [line[1]]
        #     count += 1
