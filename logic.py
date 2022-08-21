import numpy as np

file_csv = "C:/users/scott_is_mobile/desktop/qa.csv"

with open(file_csv) as file_name:
    arr = np.loadtxt(file_name, delimiter=",")

print(arr)
