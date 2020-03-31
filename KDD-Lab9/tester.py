import pandas as pd
import numpy as np
import pyfpgrowth
import csv

if __name__ == "__main__":
    f = open('weather.csv')
    csv_f = csv.reader(f)

    master_list = []

    for row in csv_f:
      master_list.append(row)

    master_list.pop(0)

    print(master_list)
    print("\n")

    for list in master_list:
        print(list)