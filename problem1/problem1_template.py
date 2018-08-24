################################################################################
################################################################################
## Template file for problem 1. You have to fill in the function findNumbers  ##
## defined below. The function takes in an input number and return the list   ##
## of numbers that satisfy the problem statement. Please ensure you return a  ##
## list as the submission will be auto evaluated. We have provided a little   ##
## helper to ensure that the return value is correct.                         ##
##                                                                            ##
## You can run this template file to see the output of your function.         ##
## First replace the TEST_NUMBER with correct number.                         ##
## Then simply run: `python problem1_template.py`                             ##
## You should see the output printed once your program runs.                  ##
##                                                                            ##
## DO NOT CHANGE THE NAME OF THE FUNCTION BELOW. ONLY FILL IN THE LOGIC.      ##
## DONT FORGET TO RETURN THE VALUES AS A LIST                                 ##
## IF YOU MAKE ANY IMPORTS PUT THEM IN THE BODY OF THE FUNCTION               ##
##                                                                            ##
## You are free to write additional helper functions but ensure they are all  ##
## in this file else your submission wont work.                               ##
##                                                                            ##
## Good Luck!                                                                 ##
################################################################################
################################################################################

TEST_NUMBER = 668**2
prime_num=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661]
def sum_split(add):
    flag=1
    for i in range(int(add/2+1)):
        prod=i*(add-i)
        for x in prime_num:
                if (prod==x):
                    flag=0
                    return(flag)
    return (flag)

def factors(number):
    x=[]
    for i in range (1,number+1):
        if (number % i == 0):
            x.append(i)
    return x
    
def prod_split(product):
    y=[]
    x=factors(product)
    if (product<668**2):
        for i in range(0,int((len(x)+1)/2)):
            add=x[i]+x[len(x)-1-i]
            flag=sum_split(add)
            y.append(flag)
        if (sum(y)==1):
            return [x[y==1], product//x[y==1]]
        else:
            return 0
    else:
        return 0
        
def findNumbers(inputNumber):
    y=[]
    for x in inputNumber:
        y.append(prod_split(x))
    qwert=list(filter(lambda a: a!=0, y))
    for i in range(qwert):
        if (qwert[i][0]!=1 & qwert[i][1]!=1):
            return qwert[i]
return [0]

def ensureNumbers(returnList):
    for num in returnList:
        if type(num) is int:
            continue
        else:
            print(num, ' is not an integer.')
            raise TypeError('The return value is not a list of integers')
    return returnList

def ensureListOfNumbers(returnList):
    if type(returnList) is list:
        return ensureNumbers(returnList)
    else:
        print('Return value is not a list. Please ensure you return a list.')
        raise TypeError('The return value is not a list')



if __name__ == "__main__":
    print(ensureListOfNumbers(findNumbers(TEST_NUMBER)))
