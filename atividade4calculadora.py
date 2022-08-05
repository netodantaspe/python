def calculadora(num1, num2, num3):
    if (num3 == 1):
        return num1 + num2
    elif (num3 == 2):
        return num1 - num2
    elif (num3 == 3):
        return num1 * num2
    elif (num3 == 4):
        return num1 / num2
    else:
        return 0

print (calculadora(int(input("digite seu primeiro numero ")), int(input("digite seu segundo numero ")), int(input("digite a operação 1 soma - 2 subtrai - 3 multiplica e 4 divide"))))
    