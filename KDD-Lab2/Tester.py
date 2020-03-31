import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def question1(strings):
    i = 0
    while i <= 5:
        print(strings)
        i += 1

def question2(num1, num2, num3, num4, num5, num6):

    result = ((num1*num2)-(num3*num4)/(num5-num6))
    return result

def question3(number_in_feet):

    number_in_meters = number_in_feet * 0.305
    return number_in_meters

def question4(user_input):

    first_digit = user_input[0]
    second_digit = user_input[1]

    first_digit = int(first_digit)
    second_digit = int(second_digit)

    years = first_digit / 365
    days = second_digit

    return years, days

def question5(weight, feet, inches):

    weight = int(weight)
    feet = int(feet)
    inches = int(inches)

    height = (feet * 12) + inches
    BMI = (703 * weight) / (height ** 2)
    BMI = int(BMI)
    return BMI

def question6(list1):
     objects = ('Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++')
     y_pos = np.arange(len(objects))
     popularity = list1

     plt.bar(y_pos, popularity, align='center', alpha=0.5)
     plt.xticks(y_pos, objects)
     plt.ylabel('Popularity')
     plt.title('Programming language popularity')

     plt.show()



if __name__== "__main__":

    question1("Welcome to Data Mining and Knowledge Discovery")
    print(question2(9.5, 4.5, 2.5, 3, 45.5, 3.5))
    print(question3(3))

    keyboard = input("Enter the minutes: ")
    years = question4(keyboard)[0]
    days = question4(keyboard)[1]
    print(f"Years: {years}, Days: {days}")

    user_weight = input("Please enter your weight: ")
    user_feet = input("Please enter how many feet tall are you: ")
    user_inches = input("Please enter how many inches tall are you: ")
    user_bmi = question5(user_weight, user_feet, user_inches)
    print(f"Your BMI: {user_bmi}")

    popularity = [19.2, 22.6, 8.8, 7.6, 7.2, 6.7]
    print(question6(popularity))
