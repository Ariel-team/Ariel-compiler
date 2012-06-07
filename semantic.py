from arbol import *

class Semantic(object):
    
    def __init__(self):
        self.tablasimbol = {}
    
    def analiza(self,arbol):
        self.tablasimbol = {}
        self.procesa(arbol)
        print 'Accept'
            
    def procesa(self,arbol):
        if type(arbol) == Variables:
            self.procesaVariables(arbol)
        elif type(arbol) == Asignacion:
            self.procesaAsignacion(arbol)
        elif type(arbol) == ID:
            self.procesaID(arbol)
        elif type(arbol) == Entero:
            self.procesaEntero(arbol)
        elif type(arbol) == Real:
            self.procesaReal(arbol)
        elif type(arbol) == Imprime:
            self.procesaImprime(arbol)
        elif type(arbol) == Suma:
            self.procesaSuma(arbol)
        elif type(arbol) == Mult:
            self.procesaMult(arbol)
        elif type(arbol) == Signo:
            self.procesaSigno(arbol)
        elif type(arbol) == Si:
            self.procesaSi(arbol)
        elif type(arbol) == Para:
            self.procesaPara(arbol)
        elif type(arbol) == Conjuncion:
            self.procesaConjuncion(arbol)
        elif type(arbol) == Disyuncion:
            self.procesaDisyuncion(arbol)
        elif type(arbol) == Relacional:
            self.procesaRelacional
        else:
            raise NameError('Nodo no Procesado')
        
    def procesaVariables(self,arbol):
        self.registraID(arbol.ide,arbol.tipo)
        if not arbol.sig == None:
            self.procesa(arbol.sig)
            
    def registraID(self,arbol,tipo):
        self.tablasimbol[arbol.simbolo] = tipo.simbolo
        if not arbol.sig == None:
            self.registraID(arbol.sig,tipo)
            
    def procesaID(self,arbol):
        try:
            arbol.tipo = self.tablasimbol[arbol.simbolo]
        except:
            raise NameError('Variable no declarada')
        if not arbol.sig == None:
            self.procesa(arbol.sig)
        
    def procesaAsignacion(self,arbol):
        self.procesa(arbol.ide)
        self.procesa(arbol.exp)
        if not arbol.exp.tipo == arbol.ide.tipo:
            raise TypeError('Incompatibilidad de tipos')
        if type(arbol.ide) != ID:
            raise TypeError('Imposible modificar constantes')
        if not arbol.sig == None:
            self.procesa(arbol.sig)
        
    def procesaEntero(self,arbol):
        arbol.tipo = 'int'
        if not arbol.sig == None:
            self.procesa(arbol.sig)
            
    def procesaReal(self,arbol):
        arbol.tipo = 'float'
        if not arbol.sig == None:
            self.procesa(arbol.sig)
            
    def procesaImprime(self,arbol):
        self.procesa(arbol.exp)
        if not arbol.sig == None:
            self.procesa(arbol.sig)
    
    def procesaSuma(self,arbol):
        self.procesa(arbol.izq)
        self.procesa(arbol.der)
        if not arbol.izq.tipo == arbol.der.tipo:
            raise TypeError('Incompatibilidad de tipos')
        arbol.tipo = arbol.izq.tipo
        #Suma no tiene atributo sig
        
    def procesaMult(self,arbol):
        self.procesa(arbol.izq)
        self.procesa(arbol.der)
        if not arbol.izq.tipo == arbol.der.tipo:
            raise TypeError('Incompatibilidad de tipos')
        arbol.tipo = arbol.izq.tipo
        #Mult no tiene atributo sig
        
    def procesaSigno(self,arbol):
        self.procesa(arbol.izq)
        arbol.tipo = arbol.izq.tipo
        #Signo no tiene atributo sig
        
    def procesaSi(self,arbol):
        self.procesa(arbol.exp)
        self.procesa(arbol.bloque)
        if not arbol.otro == None:
            self.procesa(arbol.otro)
        if not arbol.sig == None:
            self.procesa(arbol.sig)
            
    def procesaPara(self,arbol):
        self.procesa(arbol.asignacion)
        self.procesa(arbol.exp)
        self.procesa(arbol.incremento)
        self.procesa(arbol.bloque)
        if not arbol.sig == None:
            self.procesa(arbol.sig)
        
    def procesaRelacional(self,arbol):
        self.procesa(arbol.izq)
        self.procesa(arbol.der)
        arbol.tipo = 'int'
        #Relacional no tiene atributo sig
        
    def procesaConjuncion(self,arbol):
        self.procesa(arbol.izq)
        self.procesa(arbol.der)
        arbol.tipo = 'int'
        #Conjuncion no tiene atributo sig
        
    def procesaDisyuncion(self,arbol):
        self.procesa(arbol.izq)
        self.procesa(arbol.der)
        arbol.tipo = 'int'
        #Disyuncion no tiene atributo sig

if __name__ == '__main__':
    import doctest
    doctest.testfile('semanticTest.txt')