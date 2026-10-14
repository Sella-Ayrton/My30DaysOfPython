# DIA 1

print(2+3)
print(3**2)
print(10%3)
print(10//3)

print(type(10))
print(type(10.3))
print(type('hola'))
print(type([1, 2, 3]))
print(type({
    "nombre":"Pepe",
    "edad":30}))
    
"""
 Exercise: Level 1

    Check the python version you are using
    Open the python interactive shell and do the following operations. The operands are 3 and 4.
        addition(+)
        subtraction(-)
        multiplication(*)
        modulus(%)
        division(/)
        exponential(**)
        floor division operator(//)
    Write strings on the python interactive shell. The strings are the following:
        Your name
        Your family name
        Your country
        I am enjoying 30 days of python
    Check the data types of the following data:
        10
        9.8
        3.14
        4 - 4j
        ['Asabeneh', 'Python', 'Finland']
        Your name
        Your family name
        Your country

Exercise: Level 2

    Create a folder named day_1 inside 30DaysOfPython folder. Inside day_1 folder, create a python file helloworld.py and repeat questions 1, 2, 3 and 4. Remember to use print() when you are working on a python file. Navigate to the directory where you have saved your file, and run it.

Exercise: Level 3

    Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
    Find an Euclidean distance between (2, 3) and (10, 8)

🎉 CONGRATULATIONS ! 🎉
 """

"""
PS C:\\Users\\alumno\\Desktop\\30DaysOfPython> python --version
Python 3.15.0
"""

print(3+4)      # ADDITTION
print(3-4)      # SUBTRACTION
print(3*4)      # MULTIPLICATION
print(3%4)      # MODULUS
print(3/4)      # DIVISION
print(3**4)     # EXPONENTIAL
print(3//4)     # FLOOR DIVISION

str1 = "Ayrton"
str2 = "Sella"
str3 = "Argentina"
str4 = "I am enjoying 30 days of python"
print(str1 + " " + str2 + " I am from " + str3 + " and " + str4)

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh','Python','Finland']))
print(type(str1))
print(type(str2))
print(type(str3))