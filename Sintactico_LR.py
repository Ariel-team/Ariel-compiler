#!/usr/bin/python
import re
from Lexico import Lexico

class Nodo(object):
    simbolo = ''
    sig = ''

class Syntactico(Nodo):

    def __init__(self,cadena):
        self.lexico = Lexico()
        self.lexico.analiza(cadena)
    
    def obtenColumna(self,entrada):
        if entrada == '':
            entrada = '\n'
        for index in range(len(self.indice)):
            if re.match(self.indice[index], entrada):
                return index
        print 'Error'
        return 'error'

    def analiza(self):
        pila = [0]
        while True:
            try:
                columna = self.obtenColumna(self.lexico.simbolo())
                accion = self.matriz[pila[-1]][columna]
                len(accion)
            except:
                print 'Error'
                break
            else:
                if accion[0] == 's':
                    pila.append(self.lexico.simbolo())
                    pila.append(int(accion[1:]))
                    self.lexico.sigSimbolo()
                elif accion[0] == 'r':
                    regla = self.reglas[int(accion[1:])]
                    izquierda = regla.keys()[0]
                    tamano = len(regla[izquierda]) * 2
                    for c in range(tamano):
                        pila.pop()
                    pila.append(izquierda)
                    pila.append(self.matriz[pila[-2]][self.obtenColumna(pila[-1])])
                else:
                    print 'Accept'
                    break

    indice = ['\(','\)','-','\d','\n','A','E']

    matriz = [
            ['s1',  -1,'s2','s3',  -1, 4, 5],
            ['s1',  -1,'s2','s3',  -1, 4, 6],
            ['s7',  -1,  -1,'s3',  -1, 8,-1],
            [  -1,'r5',  -1,  -1,'r5',-1,-1],
            [  -1,'r3',  -1,  -1,'r3',-1,-1],
            [  -1,  -1,  -1,  -1,'ac',-1,-1],
            [  -1,'s9',  -1,  -1,  -1,-1,-1],
            ['s1',  -1,'s2','s3',  -1, 4,10],
            [  -1,'r2',  -1,  -1,'r2',-1,-1],
            [  -1,'r1',  -1,  -1,'r1',-1,-1],
            [  -1,'s11',  -1,  -1,  -1,-1,-1],
            [  -1,'r4',  -1,  -1,'r4',-1,-1]
            ]

    reglas = [
            {'E`':'E'  },
            {'E' :'(E)'},
            {'E' :'-A' },
            {'E' :'A'  },
            {'A' :'(E)'},
            {'A' :'n'},
            ]

if __name__ == '__main__':
    while True:
        entrada = raw_input('Entrada: ')
        if entrada == 'x':
            break
        syntactic = Syntactico(entrada)
        syntactic.analiza()

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

