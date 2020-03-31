import csv
import operator
from itertools import combinations
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd


def csvReader(file_directory):
    with open(file_directory) as f:
        reader = csv.reader(f)
        next(reader)
        data = []
        for row in reader:
            data.extend(row[2:])
        return data


def dataCleaner(data):
    result = ' '.join(data).split()
    result = [x.lower() for x in result]
    return result


def freqAnalysis(data):
    result = {}
    for keys in data:
        result[keys] = result.get(keys, 0) + 1
    return result


def prettyPrint(dictionary):
    dictionary = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)
    for entry in dictionary:
        print(entry)


def frequentCombinations(dictionary):
    frequent_list = getTopSix(dictionary)
    l = []
    c = 1
    while c <= 6:
        combo = combinations(frequent_list, c)
        for i in list(combo):
            l.append(i)
        c += 1
    return l


def getTopSix(dictionary):
    x = list(dictionary.keys())
    frequent_list = []
    i = 0
    while i <= 6:
        frequent_list.append(x[i])
        i += 1
    return frequent_list


def makeTopSixDict(dictionary):
    sorted_dictionary = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)
    top_six_dictionary = sorted_dictionary[:6]
    return top_six_dictionary


def supportCount(item_sets):
    te = TransactionEncoder()
    te_ary = te.fit(item_sets).transform(item_sets)
    te_ary = te_ary.astype("int")
    df = pd.DataFrame(te_ary, columns=te.columns_)
    frequent_itemsets = apriori(df, min_support=0.01, use_colnames=True)

    print('{Itemsets} ----> support')
    for index, row in frequent_itemsets.iterrows():
        print(set(row['itemsets']), '----->', round(row['support'], 3))


if __name__ == "__main__":
    raw_list_of_items = csvReader("Groceries-CSCI4105-001 - Sheet1.csv")
    clean_list_of_items = dataCleaner(raw_list_of_items)
    frequency_dictionary = freqAnalysis(clean_list_of_items)
    top_six = getTopSix(frequency_dictionary)
    combos = frequentCombinations(frequency_dictionary)
    print(supportCount(combos))