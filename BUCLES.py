# -*- coding: utf-8 -*-
# COPYRIGHT (C) 2015 AUGUSTO GORTAIRE C <agortaire@cyg.ec>
__author__ = 'Augusto Gortaire'

# ESTE PROGRAMA MUESTRA EL USO DEL BUCLE FOR
# EL USUARIO DIRA CUANTAS VECES SE REPITE EL MENSAJE, Y CUAL MENSAJE
def imprimir(mensaje):
    print u""

n = raw_input(u"Número de veces")
mensajes = raw_input(u"MENSAJE")
# TRANSFORMO A ENTERI EL NUMERO DE REPETICIONES
n = int(n)

for i in range(n):
    print mensajes

