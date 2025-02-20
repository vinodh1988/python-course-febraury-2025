numbers=[43,35,356,353,353,53,456,443,5346,634,364,333,351,23,2666,53,43]

def threeDigit(number):
    return number>99 and number<1000

def isEven(number):
    return number%2==0

def divisibleByThree(number):
    return number%3==0

#result = list(filter(threeDigit,numbers))
#result2= list(filter(isEven,numbers))
#result3= list(filter(divisibleByThree,numbers))
result = list(filter(lambda number:number>99 and number<1000,numbers))
result2= list(filter(lambda number:number%2==0,numbers))
result3= list(filter(lambda number:number%3==0,numbers))
print(result)
print(result2)
print(result3)