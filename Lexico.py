import re

class Lexico(object):
    
    def __init__(self):
        '''
        Constructor
        '''
        self.__cadena = ''
        self.__estado = 0
        self.__posicion = 0
        self.__tipos = {1 : 'Entero', 3 : 'Real', 4 : 'Identificador', 
                        6 : 'Op. Logico', 8 : 'Op Aritmetico', 9 : 'Op Relacional',
                        10 : 'Op Relacional', 11 : 'Op Logico', 12: 'Asignacion', 
                        14 : 'Cadena', 15: 'Agrupacion', -1 : 'Error'}
        self.__simbolos = ['\d','[a-zA-Z_]','\.','&','\|','\+|-|\*|/','<','>','=',
                           '!','\"','\[|\]|\(|\)|\{|\}','\n','.']
        self.__matriz = [
        [ 1, 4,-1, 5, 7, 8, 9, 9,12,11,13,15, 0,-1],#0
        [ 1,-1, 2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],#1
        [ 3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],#2
        [ 3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],#3
        [ 4, 4,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],#4
        [-1,-1,-1, 6,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],#5
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],#6
        [-1,-1,-1,-1, 6,-1,-1,-1,-1,-1,-1,-1,-1,-1],#7
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],#8
        [-1,-1,-1,-1,-1,-1,-1,-1,10,-1,-1,-1,-1,-1],#9
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],#10
        [-1,-1,-1,-1,-1,-1,-1,-1,10,-1,-1,-1,-1,-1],#11
        [-1,-1,-1,-1,-1,-1,-1,-1,10,-1,-1,-1,-1,-1],#12
        [13,13,13,13,13,13,13,13,13,13,14,13,13,13],#13
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],#14
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1] #15
        ]

    def analiza(self, cadena):
        self.__cadena = cadena
        self.__posicion = -1
        print 'Analizado:'
        while True:
            resp = self.sigSimbolo()
            print resp
            if resp == '':
                break

    def sigSimbolo(self):
        simbolo = ''
        self.__estado = 0
        if self.__posicion == len(self.__cadena) - 1:
            return ''
        while self.__posicion < len(self.__cadena) - 1:
            self.__posicion += 1
            if self.__cadena[self.__posicion] != ' ' and \
                    self.__cadena[self.__posicion] != '\n':
                self.__estado = self.__transicion(self.__cadena[self.__posicion])
                simbolo += self.__cadena[self.__posicion]
                if self.__posicion < len(self.__cadena) - 1:
                    if self.__transicion(self.__cadena[self.__posicion + 1]) == -1:
                        return simbolo+': '+self.getTipo()
                else:
                    return simbolo+': '+self.getTipo()
        return ''                
    
    def __transicion(self, caracter):
        for index in range(len(self.__simbolos)):
            if re.match(self.__simbolos[index], caracter):
                return self.__matriz[self.__estado][index]
        
    def getEstado(self):
        return self.__estado
    
    def getTipo(self):
        if self.__tipos.__contains__(self.__estado):
            return self.__tipos[self.__estado]
        else:
            return self.__tipos[-1]

if __name__ == "__main__":
    import time
    x = Lexico()
    archivo = open('test.ari')
    contenido = archivo.read()
    t1 = time.time()
    x.analiza(contenido)
    t2 = time.time()
    print t2 - t1
