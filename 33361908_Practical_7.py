#cd c://programs python 33361908_Practical_7.py
#python 33361908_Practical_7.py

#Question 1
#Loop While less than user input
n = int(input("Enter the number of values to display: "))
i = 0
#Print i < n
while (i < n):
    i = i + 1
    print(i)
print('')

#Question 2
#Calculate sum of Positive Floats
#not supposed to sum negative numbers as per illustration
sum = 0
i = 0
calculate = True
while calculate:
    i = i + 1
    n = float(input('Enter value ' + str(i) + ' : '))
    if n > 0:
        sum = sum + n
    else:
        calculate = False
        print('The sum of ' + str(i) + ' values = ' + str(sum))
print('')

#Question 3
#Convert decimal int to another number system
decimal = int(input("Enter decimal number to convert to base: "))
base = int(input("Enter base for conversion: "))

def convertToBase(decimal,base):
    base_num = ""
    while (decimal > 0):
        digit = int(decimal%base)
        if digit<10:
            base_num += str(digit)
        else:
            base_num += chr(ord('A')+digit-10)
        decimal //= base
    base_num = base_num[::-1]
    print('  ___')
    print(str(base) + '|' + str(decimal))
    print('Base ' + str(base) + ' value of ' + str(decimal) + ' = ' + base_num)

convertToBase(decimal,base)
