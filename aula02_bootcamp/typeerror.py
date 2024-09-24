try:
    numero_01 = int(input("inserir numero inteiro:  "))
    numero_02 = int(input("inserir outro numero inteiro:  "))
    resultado = numero_01 // numero_02
    print (resultado)

except:
    print(" integer division or modulo by zero")




try:
    resultado = len(3)
    print (resultado)
except TypeError as e:
    print(e)
else:
    print('tudo ocorreu bem')
finally:
    print("O importante é participar")

numero = int(input("insira um numero: "))
if isinstance(numero, int):
    print("A variável não é um inteiro.")
else:
    print("A variável não mé um inteiro.")



