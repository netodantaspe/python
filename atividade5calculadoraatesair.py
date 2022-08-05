print("digite a operação 1 soma - 2 subtrai - 3 multiplica - 4 divide ou zero para sair")
num1 = int(input("Qual operação deseja fazer?"))
def calculadora(num2, num3):
while num1 != 0:
    if (num1 == 5):
        return "não tem operação válida"
    elif (num1 == 1):
        return num2 + num3
    elif (num1 == 2):
        return num2 - num3
    elif (num1 == 3):
        return num2 * num3
    elif (num1 == 4):
        return num2 / num3
    else:
        return "não tem operação válida"
print ("você saiu do programa")
print(calculadora (int(input("digite seu primeiro numero ")), int(input("digite seu segundo numero "))))) 