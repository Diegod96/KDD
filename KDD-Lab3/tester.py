from pandas import read_csv
import numpy as np

if __name__ == "__main__":
    dataset = read_csv('diabetes_missingdata.csv', header=None)
    # print(dataset.head(20))

    # Shows header and other stats of the dataset
    print(dataset.describe())

    # # Counts missing data per column
    # print((dataset[1] == 0).sum())
    # print((dataset[2] == 0).sum())
    # print((dataset[3] == 0).sum())
    # print((dataset[4] == 0).sum())
    # print((dataset[5] == 0).sum())
    # print((dataset[[1, 2, 3, 4, 5]] == 0).sum())

    # mark zero values as missing of NaN
    dataset[[1, 2, 3, 4, 5]] = dataset[[1, 2, 3, 4, 5]].replace(0, np.NaN)
    # count number if NaN values in each column
    print(dataset.isnull().sum())
    #
    # # drop rows with missing values
    # dataset.dropna(inplace=True)
    # # summarize the number of rows and columns in the dataset
    # print(dataset.describe())

    # fill missing values with mean column values
    # dataset[[1, 2, 3, 4, 5]] = dataset[[1, 2, 3, 4 ,5]].replace(0, np.NaN)
    # dataset.fillna(dataset.mean(), inplace=True)
    # print(dataset.isnull().sum())
    # print(dataset.describe())