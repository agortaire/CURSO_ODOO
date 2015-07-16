# -*- coding: utf-8 -*-
# COPYRIGHT (C) 2015 AUGUSTO GORTAIRE C <agortaire@cyg.ec>
__author__ = 'Augusto Gortaire'

#DEFINO MI FUNCION
def calculadora (a, b, op, resultado = 0):
    if op == '+':
        resultado = a + b
    elif op == '-':
        resultado = a - b
    elif op == '*':
        resultado = a * b
    elif op == '/':
    #CAPTURO EL ERROR ZERO DIVISION ERROR
        try:
            resultado = a / b
        except ZeroDivisionError:
            print "NO PUEDES DIVIDIR PARA CERO"
    else:
        print "No existe esa opcion!!!!"
    return resultado

def imprimir (mensaje):
    print mensaje.upper()

# ESTE ES EL PROGRAMA PCPAL
imprimir("######## mi programa   #####")
imprimir(u"######    versión 2.0 ######")
imprimir("\n")

a = float(raw_input("Ingrese el primer numero "))
b = float(raw_input("Ingrese el segundo numero "))
op = raw_input("Que quiere realizar todas las operaciones y/n ")

if op!= 'y' and op!= 'n':
    print "Error opcion invalida y/n"
elif op == 'y':
    imprimir("suma: " + str(calculadora(a, b, '+')))
    imprimir("resta: " + str(calculadora(a, b, '-')))
    imprimir("multip: " + str(calculadora(a, b, '*')))
    imprimir("div: " + str(calculadora(a, b, '/')))

else:
    print "Chao"

