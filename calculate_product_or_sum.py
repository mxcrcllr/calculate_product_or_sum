
#User inputs number 1
num1 = int(input('Enter number 1: '))
#User inputs number 2
num2 = int(input('Enter number 2: '))

#product(num1, num2):
def prod_or_sum(num1, num2):
    #Multiply num1 and num2 
    product = num1 * num2
    #Add num1 and num2 
    sum = num1 + num2

    #If the product is less than or equal to 1000:
    if product <= 1000:
        #Print multiply
        return product
    #Else:
    else:
        #Print sum
        return sum

result = prod_or_sum(num1, num2)
print('The result is', result)

