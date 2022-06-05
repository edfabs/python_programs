import os
import sys

print('Programa que ordena dos numeros')
num1 = input('Teclea el primer numero: ')
num1 = int(num1)
num2 = input('Teclea el primer numero: ')
num2 = int(num2)
if(num1 > num2):
    print('Esta en orden Descendente')
else:
    print('Estan en orden Ascendente')
