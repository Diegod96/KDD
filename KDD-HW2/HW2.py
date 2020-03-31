from pandas import read_csv
import numpy as np


# Calculates 3 of missing values given in the original csv
def calculateMissingValues(data):
    missing_data = data.isnull().sum()
    print("Missing values for each feature (feature | # missing values): ")
    print(missing_data)


# Finds average age of patients
# Replaces nan values with 0
# Converts 'Age' column to list
def findAverageAge(data):
    data[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]] = data[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]].replace(np.NaN, 0)
    age = data[0].tolist()
    del age[0]
    age = list(map(float, age))
    average_age = round(sum(age) / len(age))
    print(f"Average age: {average_age} years old")


# Calculates range of 'Glucose' column
# Converts 'Glucose' column to a list and then a numpy array
# Swaps nan values with the mean of the numpy array
# Gets min and max values and calculates range
def glucoseRange(data):
    data[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]] = data[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]].replace(0, np.NaN)
    data.fillna(data.mean(), inplace=True)
    glucose = data[2].tolist()
    del glucose[0]
    glucose = list(map(float, glucose))
    glucose = np.array(glucose)
    x = np.where(np.isnan(glucose), np.ma.array(glucose, mask=np.isnan(glucose)).mean(axis=0), glucose)
    max_val = np.amax(x)
    min_val = np.amin(x)
    r = round(max_val - min_val)
    print(f"Glucose range: {r} ng/ml")


if __name__ == "__main__":
    dataset = read_csv('dataR2-w-missing.csv', header=None)
    calculateMissingValues(dataset)
    findAverageAge(dataset)
    glucoseRange(dataset)
