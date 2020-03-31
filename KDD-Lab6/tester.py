import csv
import operator
from itertools import combinations
from itertools import permutations

'''
Reads csv file
Each row is it's own list
Row lists are extended onto one main list 'data'
'''


def csvReader(file_directory):
    with open(file_directory) as f:
        reader = csv.reader(f)
        next(reader)
        data = []
        for row in reader:
            data.extend(row[2:])
        return data


'''
Gets rid of any white space (' ') entries in the list 'data'
'''


def dataCleaner(data):
    result = ' '.join(data).split()
    result = [x.lower() for x in result]
    return result


'''
Initializes an empty dictionary called 'result'
List 'data' is iterated over with keys being the item
Values are frequency of key items in the list 'data' 
'''


def freqAnalysis(data):
    result = {}
    for keys in data:
        result[keys] = result.get(keys, 0) + 1
    return result


'''
Breaks dictionary into individual key-value pair tuples
Sorts tuples by the their value (descending order largest -> smallest)
Prints it out tuple-by-tuple for easy viewing
'''


def prettyPrint(dictionary):
    dictionary = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)
    for entry in dictionary:
        print(entry)


'''
Gets top six frequent items
Prints combination of top six most frequent items
'''


def frequentCombinations(dictionary):
    print("Top six frequent items: ")
    print('\n')
    x = list(dictionary.keys())
    frequent_list = []
    i = 0
    while i <= 6:
        print(x[i])
        frequent_list.append(x[i])
        i += 1

    c = 1
    print('\n')
    print("Combination of top six most frequent items: ")
    while c <= 6:
        print('\n')
        combo = combinations(frequent_list, c)
        print(f"{c} item set:", end='')
        for i in list(combo):
            print(f" {i}", end='')
        c += 1


if __name__ == "__main__":
    raw_list_of_items = csvReader("Groceries-CSCI4105-001 - Sheet1.csv")
    clean_list_of_items = dataCleaner(raw_list_of_items)
    frequency_dictionary = freqAnalysis(clean_list_of_items)
    prettyPrint(frequency_dictionary)
    print('\n')
    frequentCombinations(frequency_dictionary)
