# Written by *** for COMP9021
#
# Implements three functions:
# - binary_lunar_addition(number_1, number_2)
#   that lunarly (or is it lunatically?) adds number_2 to number_1;
# - lunar_addition(*numbers)
#   that lunarly adds all arguments;
# - binary_lunar_multiplication(multiplicand, multiplier)
#   that lunarly multiplies multiplicand by multiplier.
#
# Both operations are discussed at
# https://www.youtube.com/watch?v=cZkGeR9CWbk
# Watch it!
#
# Essentially, lunar addition and lunar multiplication
# are like standard addition and multiplication, except that:
# - the lunar sum of two digits is the largest of both digits;
# - the lunar product of two digits is the smallest of both digits.
#
# You can assume that the function arguments are exactly as expected,
# namely, positive numbers (possibly equal to 0).

def binary_lunar_addition(number_1, number_2):
    # INSERT YOUR CODE HERE
    str1=str(number_1)          
    str2=str(number_2)
    result = ""

    maxLen = max(len(str1), len(str2))     
        #print(maxLen)

    A = str1.zfill(maxLen)     
    B = str2.zfill(maxLen)

    for i in range(maxLen):
        if int(A[i]) < int(B[i]):
            result += B[i]
        else:
            result += A[i]  

    return result

def lunar_addition(*numbers):
    # INSERT YOUR CODE HERE 
    sum = 0
    for i in range(len(numbers)):
        x= binary_lunar_addition(sum, numbers[i])
        sum = int(x)
    return sum



def binary_lunar_multiplication(multiplicand, multiplier):
    # INSERT YOUR CODE HERE
    str1=str(multiplicand)          
    str2=str(multiplier)
    #print(str1)
    #print(str2)
    result = ""
    toBeSummed =[]
    count = 0

    for j in str2[::-1]:
        number = ""
        for i in str1:
            #print("i = " + i)
            #print("j = " + j)
            
            if int(i) > int(j):
                number += j
            else:
                number += i
        #print(count)  
        #print(number + "0"*count)  
        toBeSummed.append(int(number + "0"*count))
        count += 1
    print(toBeSummed)


    result = lunar_addition(*toBeSummed)
    return result

#numbers = [0,1, 3333,44444,]
#print(lunar_addition(*numbers))

