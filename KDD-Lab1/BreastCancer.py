import csv
import matplotlib.pyplot as plt;

plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from pylab import *


# Converts dataR2.csv to list of dictionaries
def csv_to_dictlist(csv_file):
    columns = []

    with open(csv_file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            row_as_dict = {k: v for k, v in row.items()}
            columns.append(row_as_dict)
    return columns


# Calculates the # of control patients and healthy patients
def healthy_or_control(dicts):
    classification_list = list(map(lambda x: x['Classification'], dicts))
    classification_list = list(map(int, classification_list))
    controls = 0
    healthy = 0

    for i in range(len(classification_list)):
        if classification_list[i] == 1:
            controls += 1
        else:
            healthy += 1

    return controls, healthy


# Calculates the # of young, middle aged, and senior patients
def determine_age(dicts):
    age_list = list(map(lambda x: x['Age'], dicts))
    age_list = list(map(int, age_list))

    young = 0
    middle_aged = 0
    senior = 0

    for i in range(len(age_list)):
        if 0 < age_list[i] < 30:
            young += 1
        elif 30 <= age_list[i] < 40:
            middle_aged += 1
        else:
            senior += 1

    return young, middle_aged, senior


# Calculates the # of underweight, normal, overweight, and obese patients
def determine_bmi(dicts):
    bmi_list = list(map(lambda x: x['BMI'], dicts))
    bmi_list = list(map(float, bmi_list))

    underweight = 0
    normal = 0
    overweight = 0
    obese = 0

    for i in range(len(bmi_list)):
        if bmi_list[i] < 18.5:
            underweight += 1
        elif 18.5 <= bmi_list[i] < 25:
            normal += 1
        elif 25 <= bmi_list[i] < 30:
            overweight += 1
        else:
            obese += 1

    return underweight, normal, overweight, obese


# Creates bar chart of patients v. age group
def age_plot(young, middle_aged, senior):
    objects = ('Young', 'Middle Aged', 'Senior')
    y_pos = np.arange(len(objects))
    num_patients = [young, middle_aged, senior]

    plt.bar(y_pos, num_patients, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Patients')
    plt.title('Age of Patients')

    plt.show()


# Creates bar chart of patients v. weight group based off BMI
def bmi_plot(underweight, normal, overweight, obese):
    objects = ('Underweight', 'Normal', 'Overweight', 'Obese')
    y_pos = np.arange(len(objects))
    num_patients = [underweight, normal, overweight, obese]

    plt.bar(y_pos, num_patients, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Patients')
    plt.title('Weights based off of patients bmi')

    plt.show()


# Calculates the number of patients that are at risk of diabetes based off their glucose levels
# It has been studied that people with diabetes have a greater chance to have breast cancer
def glucose_plot(dicts):
    glucose_list = list(map(lambda x: x['Glucose'], dicts))
    glucose_list = list(map(float, glucose_list))

    none = 0
    slight = 0
    moderate = 0
    severe = 0
    diabetes = 0

    for i in range(len(glucose_list)):
        if 75 < glucose_list[i] < 95:
            none += 1
        elif 95 < glucose_list[i] < 100:
            slight += 1
        elif 100 < glucose_list[i] < 110:
            moderate += 1
        elif 110 < glucose_list[i] < 125:
            severe += 1
        else:
            diabetes += 1

    objects = ('None', 'Slight', 'Moderate', 'Severe', 'Diabetic')
    y_pos = np.arange(len(objects))
    num_patients = [none, slight, moderate, severe, diabetes]

    plt.bar(y_pos, num_patients, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Patients')
    plt.title('Diabetic risk based off glucose levels')

    plt.show()


def insulin_plot(dicts):
    insulin_list = list(map(lambda x: x['Insulin'], dicts))
    insulin_list = list(map(float, insulin_list))

    none = 0
    slight = 0
    moderate = 0
    severe = 0

    for i in range(len(insulin_list)):
        if 3 < insulin_list[i] < 8:
            none += 1
        elif 8 < insulin_list[i] < 10:
            slight += 1
        elif 10 < insulin_list[i] < 12:
            moderate += 1
        else:
            severe += 1

    objects = ('None', 'Slight', 'Moderate', 'Severe')
    y_pos = np.arange(len(objects))
    num_patients = [none, slight, moderate, severe]

    plt.bar(y_pos, num_patients, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Patients')
    plt.title('Diabetic risk based off insulin levels')

    plt.show()


def HOMA_plot(dicts):
    HOMA_list = list(map(lambda x: x['HOMA'], dicts))
    HOMA_list = list(map(float, HOMA_list))

    none = 0
    slight = 0
    moderate = 0
    severe = 0

    for i in range(len(HOMA_list)):
        if 0.5 < HOMA_list[i] < 1.5:
            none += 1
        elif 1.5 < HOMA_list[i] < 2.5:
            slight += 1
        elif 2.5 < HOMA_list[i] < 3.0:
            moderate += 1
        else:
            severe += 1

    objects = ('None', 'Slight', 'Moderate', 'Severe')
    y_pos = np.arange(len(objects))
    num_patients = [none, slight, moderate, severe]

    plt.bar(y_pos, num_patients, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Patients')
    plt.title('Diabetic risk based off HOMA')

    plt.show()


def leptin_plot(dicts):
    leptin_list = list(map(lambda x: x['Leptin'], dicts))
    leptin_list = list(map(float, leptin_list))

    insulin_list = list(map(lambda x: x['Insulin'], dicts))
    insulin_list = list(map(float, insulin_list))

    plt.plot(leptin_list, label='Leptin')
    plt.plot(insulin_list, label='Insulin')

    plt.title("Leptin levels v Insulin levels")
    plt.xlabel("Insulin Levels (ng/ml)")
    plt.ylabel("Leptin Levels (ng/ml)")

    plt.legend()
    plt.show()


def adiponectin_plot(dicts):
    adiponectin_list = list(map(lambda x: x['Adiponectin'], dicts))
    adiponectin_list = list(map(float, adiponectin_list))

    glucose_list = list(map(lambda x: x['Glucose'], dicts))
    glucose_list = list(map(float, glucose_list))

    plt.plot(adiponectin_list, label='Adiponectin')
    plt.plot(glucose_list, label='Glucose')


    plt.title("Adiponectin levels v. Glucose levels")
    plt.xlabel("Adiponectin Levels (µg/mL)")
    plt.ylabel("Glucose Levels (ng/ml)")

    plt.legend()
    plt.show()

def resistin_plot(dicts):
    resistin_list = list(map(lambda x: x['Resistin'], dicts))
    resistin_list = list(map(float, resistin_list))

    insulin_list = list(map(lambda x: x['Insulin'], dicts))
    insulin_list = list(map(float, insulin_list))

    plt.plot(resistin_list, label='Resistin')
    plt.plot(insulin_list, label='Insulin')

    plt.title("Resistin levels v. Insulin levels")
    plt.xlabel("Resistin Levels (ng/mL)")
    plt.ylabel("Insulin Levels (µU/mL)")

    plt.legend()
    plt.show()

def MCP_plot(dicts):
    MCP_list = list(map(lambda x: x['MCP.1'], dicts))
    MCP_list = list(map(float, MCP_list))

    age_list = list(map(lambda x: x['Age'], dicts))
    age_list = list(map(int, age_list))

    plt.plot(MCP_list, label='MCP-1')
    plt.plot(age_list, label='Age')

    plt.title("Age v. MCP Levels")
    plt.xlabel("Age")
    plt.ylabel("MCP Levels")

    plt.legend()
    plt.show()


if __name__ == "__main__":
    dictlist = csv_to_dictlist('dataR2.csv')
    num_of_instances = len(dictlist)
    print(f"Number of instances: {num_of_instances}")
    print("\n")

    control_patients = healthy_or_control(dictlist)[0]
    healthy_patients = healthy_or_control(dictlist)[1]
    print(f"Number of health controls: {control_patients}")
    print(f"Number of patients: {healthy_patients}")
    print("\n")

    young_patients = determine_age(dictlist)[0]
    middle_aged_patients = determine_age(dictlist)[1]
    senior_patients = determine_age(dictlist)[2]
    print(f"Number of patients younger than 30 years old: {young_patients}")
    print(f"Number of patients between 30 years old & 40 years old: {middle_aged_patients}")
    print(f"Number of patients older than 40 years old: {senior_patients}")
    print("\n")

    underweight_patients = determine_bmi(dictlist)[0]
    normal_patients = determine_bmi(dictlist)[1]
    overweight_patients = determine_bmi(dictlist)[2]
    obese_patients = determine_bmi(dictlist)[3]
    print(f"Number of underweight patients based off of BMI: {underweight_patients}")
    print(f"Number of normal patients based off of BMI: {normal_patients}")
    print(f"Number of overweight patients based off of BMI {overweight_patients}")
    print(f"Obese patients based off of BMI: {obese_patients}")

    age_plot(young_patients, middle_aged_patients, senior_patients)
    bmi_plot(underweight_patients, normal_patients, overweight_patients, obese_patients)
    glucose_plot(dictlist)
    insulin_plot(dictlist)
    HOMA_plot(dictlist)
    leptin_plot(dictlist)
    adiponectin_plot(dictlist)
    resistin_plot(dictlist)
    MCP_plot(dictlist)
