import re

class Lexico(object):
    
    def __init__(self):
        '''
        Constructor
        '''
        self.__estado = 0
        self.__tipos = { 1 : 'Entero', 3 : 'Real', 4 : 'Identificador', 6 : 'Op. Logico', 8 : 'Op Aritmetico', 9 : 'Op Relacional',
                         10 : 'Op Relacional', 11 : 'Op Logico', 12: 'Asignacion', 14 : 'Cadena', -1 : 'NULL'}
        self.__simbolos = ['\d','[a-zA-Z_]','\.','&','\|','\+|-|\*|/','<','>','=','!','\"','.',' ']
        self.__matriz = [
            [ 1, 4,-1, 5, 7, 8, 9, 9,12,11,13,-1],#0
            [ 1,-1, 2,-1,-1,-1,-1,-1,-1,-1,-1,-1],#1
            [ 3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],#2
            [ 3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],#3
            [ 4, 4,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],#4
            [-1,-1,-1, 6,-1,-1,-1,-1,-1,-1,-1,-1],#5
            [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],#6
            [-1,-1,-1,-1, 6,-1,-1,-1,-1,-1,-1,-1],#7
            [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],#8
            [-1,-1,-1,-1,-1,-1,-1,-1,10,-1,-1,-1],#9
            [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],#10
            [-1,-1,-1,-1,-1,-1,-1,-1,10,-1,-1,-1],#11
            [-1,-1,-1,-1,-1,-1,-1,-1,10,-1,-1,-1],#12
            [13,13,13,13,13,13,13,13,13,13,14,13],#13
            [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1] #14
        ]

    def analiza(self,cadena):
        for c in cadena:
            if not self.__estado == -1: 
                for index in range(self.__simbolos.__len__()):
                    if re.match(self.__simbolos[index], c):
                        self.__estado = self.__matriz[self.__estado][index]
                        break
    
    def getEstado(self):
        return self.__estado
    
    def getTipo(self):
        if self.__tipos.__contains__(self.__estado):
            return self.__tipos[self.__estado]
        else:
            return self.__tipos[-1]

if __name__ == "__main__":
    x = Lexico()
    entrada = raw_input("Ingresa una cadena \n")
    x.analiza(entrada)
    print(x.getTipo())
