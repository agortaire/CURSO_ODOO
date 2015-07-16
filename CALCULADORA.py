# EJEMPLO PARA CONSTRUIR UNA CALCULADORA SIMPLE. VA A TOMAR DOS NUMEROS Y ME PREGUNTA QUE OPERACION QUIERO HACER.
# RAWINPUT para capturar la entrada
# CONVIERTO LA ENTRADA DE RAW INPUT A FLOAT
# RAWINPUT SIEMPRE BOTA UN STR
a = float(raw_input("Primero: "))
b = float(raw_input("Segundo: "))
resultado = 0.0
op = raw_input("QUE OPERACION QUIERES REALIZAR (+,-,*,/)")

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

print "El resultado es: " + str(resultado)
raw_input("Presione cualquier tecla para salir..")
