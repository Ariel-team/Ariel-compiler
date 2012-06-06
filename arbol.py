class Single:
    conten=""
    count = 0
    def etiqueta(self):
        count += 1
        return 'E'+str(count)+'\n'

class Nodo(object):
  
    simbolo = ""
    codigo = Single()
    relacionales={'<':'jl','>':'jg','<=':'jge','>=':'jle','==':'je','!=':'jne'}
    
    def __init__(self):
        self.sig = None
     

class Tipo(Nodo):
    
    def __init__(self, simbolo):
        self.simbolo = simbolo
        self.sig = None
    
    def muestra(self):
        print "<Tipo>" + self.simbolo
        if(self.sig):
            self.sig.muestra()


class Expresion(Nodo):
    
    def __init__(self, izq=None, der=None):
        self.izq = izq
        self.der = der
        self.sig = None
    
    def muestra(self, op):
        print "<"+op+">" + self.simbolo
        self.izq.muestra()
        self.der.muestra()


class ID(Expresion):
    
    def __init__(self, simbolo, sig=None):
        self.simbolo = simbolo
        self.sig = sig

    def muestra(self):
        print "<Identificador>" + self.simbolo
        if(self.sig):
            self.sig.muestra()
                                
    def genera(self):
            self.codigo.conten += 'push ' + self.simbolo + '\n'


class Entero(Expresion):
    
    def __init__(self, simbolo):
        self.simbolo = simbolo
        self.sig = None
    
    def muestra(self):
        print "<Entero>" + self.simbolo
        if(self.sig):
            self.sig.muestra()
                                
    def genera(self):
            self.codigo.conten += 'push ' + self.simbolo + '\n'


class Real(Expresion):
    
    def __init__(self, simbolo):
        self.simbolo = simbolo
        self.sig = None
    
    def muestra(self):
        print "<Real>" + self.simbolo
        if(self.sig):
            self.sig.muestra()
                    
    def genera(self):
            self.codigo.conten += 'push ' + self.simbolo + '\n'


class Signo(Expresion):
    
    def __init__(self, izq):
        self.izq = izq
        self.der = None
    
    def muestra(self):
        print "<Signo>" + self.simbolo
        self.izq.muestra()
                
    def genera(self):
        self.izq.genera()
        self.codigo.conten += 'pop eax\nmul -1\npush eax\n'


class Suma(Expresion):
    
    def __init__(self, izq, der):
        self.izq = izq
        self.der = der
    
    def muestra(self):
        Expresion.muestra(self,"Suma")
    
    def genera(self):
        self.izq.genera()
        self.der.genera()
        self.codigo.conten += 'pop ebx\npop eax\nadd eax, ebx\npush eax\n'
        
class Mult(Expresion):
    
    def __init__(self, izq, der):
        self.izq = izq
        self.der = der
    
    def muestra(self):
        Expresion.muestra(self,"Mult")
        
    def genera(self):
        self.izq.genera()
        self.der.genera()
        self.codigo.conten += 'pop ebx\npop eax\nmul ebx\npush eax\n'

class Conjuncion(Expresion):
    
    def __init__(self, izq, der):
        self.izq = izq
        self.der = der
    
    def muestra(self):
        Expresion.muestra(self,"Conj")
        
    def genera(self):
        self.izq.genera()
        self.der.genera()
        self.codigo.conten += 'pop ebx\npop eax\nand eax,ebx\npush eax\n'


class Disyuncion(Expresion):
    
    def __init__(self, izq, der):
        self.izq = izq
        self.der = der
    
    def muestra(self):
        Expresion.muestra(self,"Disy")
                
    def genera(self):
        self.izq.genera()
        self.der.genera()
        self.codigo.conten += 'pop ebx\npop eax\nor eax,ebx\npush eax\n'


class Relacional(Expresion):
    
    def __init__(self, simbolo, izq, der):
        self.simbolo = simbolo
        self.izq = izq
        self.der = der
    
    def muestra(self):
        Expresion.muestra(self,"Relacional")
        
    def genera(self):
        self.izq.genera
        self.der.genera
        eti = self.codigo.etiqueta()
        etf = self.codigo.etiqueta()
        self.codigo.conten += 'pop ebx\npop eax\ncmp ebx eax\n'
        self.codigo.conten += relacionales[self.simbolo] + ' ' + eti + '\n'
        self.codigo.conten += 'push 1\njmp '+ etf + '\n' 
        self.codigo.conten += eti + ': push 0\n' + etf + ':\n'        

class Variables(Nodo):
    
    def __init__(self, tipo, ide, sig=None):
        self.tipo = tipo
        self.ide = ide
        self.sig = sig
        
    def muestra(self):
        print "<Variables>"
        self.tipo.muestra()
        self.ide.muestra()
        if(self.sig):
            self.sig.muestra()
    
    def genera(self):
        if(self.sig):
            self.sig.genera()


class Asignacion(Nodo):
    
    def __init__(self, ide, exp, sig=None):
        self.ide = ide
        self.exp = exp
        self.sig = sig
        
    def muestra(self):
        print "<Asignacion>"
        self.ide.muestra()
        self.exp.muestra()
        if(self.sig):
            self.sig.muestra()
            
    def genera(self):
        self.ide.genera()
        self.exp.genera()
        self.codigo.conten += 'pop ' + self.ide.simbolo +'\n'
        if(self.sig):
            self.sig.genera()

class Si(Nodo):

    def __init__(self, exp, bloque, otro, sig=None):
        self.exp = exp
        self.bloque = bloque
        self.otro = otro
        self.sig = sig
    
    def muestra(self):
        print "<Si>"
        self.exp.muestra()
        self.bloque.muestra()
        if(self.otro):
            self.otro.muestra()
        if(self.sig):
            self.sig.muestra()
        
    def genera(self):
        ete = self,codigo,etiqueta()
        etf = self,codigo,etiqueta()
        self.codigo.conten += 'pop eax\n cmp eax,0\n jne ' + ete + '\n'
        self.bloque.genera()
        self.codigo.conten += 'jmp ' + etf + '\n' + ete + ':\n'
        if (self.otro):
            self.otro.genera()
        self.codigo.conten += etf + ':\n'
        if (self.sig):
            self.sig.genera()
            


class Para(Nodo):
    
    def __init__(self, asignacion, exp, incremento, bloque, sig=None):
        self.asignacion = asignacion
        self.exp = exp
        self.incremento = incremento
        self.bloque = bloque
        self.sig = sig
    
    def muestra(self):
        print "<Para>"
        self.asignacion.muestra()
        self.exp.muestra()
        self.incremento.muestra()
        self.bloque.muestra()
        if(self.sig):
            self.sig.muestra()
            
    def genera(self):
        eti = self.codigo.etiqueta()
        etf = self.codigo.etiqueta()
        self.asignacion.genera()
        self.codigo.conten += eti + ':\n'
        self.exp.genera()
        self.codigo.conten += 'pop eax\ncmp eax,0\jne  ' + etf + '\n'
        self.bloque.genera()
        self.incremento.genera()
        self.codigo.conten += 'jmp ' + eti + '\n' + etf + ':\n'
        if(self.sig):
            self.sig.genera()
                
    
class Imprime(Nodo):
    
    def __init__(self, exp, sig=None):
        self.exp = exp
        self.sig = sig
        
    def muestra(self):
        print "<Imprime>"
        self.exp.muestra()
        if(self.sig):
            self.sig.muestra()
            
    def genera(self):
        self.exp.genera()
        self.codigo.conten += 'pop eax\nprint str$(eax)\n'
        if(self.sig):
            self.sig.genera()

def arbol0():
    return Variables(Tipo("int"), ID("a"))

def arbol1():
    return Variables(Tipo("int"), ID("a", ID("b", ID("c"))))

def arbol2():
    return Variables(Tipo("int"), ID("a", ID("b")), Variables(Tipo("int"), ID("c", ID("d")), Asignacion(ID("a"), Entero("3"), Imprime(ID("a")))))

def arbol3():
    return Variables(Tipo("int"), ID("a", ID("b")), Variables(Tipo("int"), ID("c", ID("d")), Asignacion(ID("c"), Entero("5"), Asignacion(ID("a"), Suma(Entero("3"), ID("c")), Imprime(ID("a"), Imprime(Suma(Entero("2"), Mult(Entero("3"),Signo(Entero("4"))))))))))

def arbol4():
    return  Variables(Tipo("int"), ID("a", ID("b")), Variables(Tipo("int"), ID("c", ID("d")), Asignacion(ID("b"), Entero( "2" ) , Asignacion(ID("c"), Entero( "4" ) , Asignacion(ID("d"), Entero( "1" ) , Asignacion(ID("a"), Suma(ID("b"), Mult(ID("c"), ID("d"))), Imprime(ID("a"))))))))

def arbol5():
    return  Variables(Tipo("int"), ID("a", ID("z")), Asignacion(ID("z"), Entero( "0" ) , Asignacion(ID("a"), Entero( "5" ) , Si(Relacional(">", ID("a"), Entero( "2" ) ), Asignacion(ID("z"), Entero( "1" ) ), None, Imprime(ID("z"))))))

def arbol6():
    return  Variables(Tipo("int"), ID("a", ID("z")), Asignacion(ID("a"), Entero( "5" ) , Si(Relacional(">", ID("a"), Entero( "2" ) ), Asignacion(ID("z"), Entero( "1" ) ), Asignacion(ID("z"), Entero( "0" ) ), Imprime(ID("z")))));

def arbol7():
    return  Variables(Tipo("int"), ID("a", ID("b")), Asignacion(ID("a"), Entero( "5" ) , Asignacion(ID("b"), Entero( "10" ) , Si(Conjuncion(Relacional("<=", ID("a"), Entero( "10" ) ), Relacional(">=", ID("b"), Entero( "20" ) )), Asignacion(ID("z"), Entero( "1" ) ), Asignacion(ID("z"), Entero( "0" ) ), Imprime(ID("z"))))));

def arbol8():
    return  Variables(Tipo("int"), ID("a", ID("b", ID("c"))), Asignacion(ID("a"), Entero( "5" ) , Asignacion(ID("b"), Entero( "21" ) , Asignacion(ID("c"), Entero( "2" ) , Si(Conjuncion(Relacional("<=", ID("a"), Entero( "10" ) ), Disyuncion(Relacional(">=", ID("b"), Entero( "20" ) ), Relacional("<", ID("c"), Entero( "10" ) ))), Asignacion(ID("z"), Entero( "1" ) ), Asignacion(ID("z"), Entero( "0" ) ), Imprime(ID("z")))))));

def arbol9():
    return  Variables(Tipo("int"), ID("i"), Para(Asignacion(ID("i"), Entero( "0" ) ), Relacional("<", ID("i"), Entero( "100" ) ), Asignacion(ID("i"), Suma(ID("i"), Entero( "1" ) )), Imprime(ID("i"))));

def arbol10():
    return  Variables(Tipo("int"), ID("a", ID("c", ID("i", ID("j")))), Asignacion(ID("a"), Entero( "5" ) , Asignacion(ID("b"), Entero( "23" ) , Asignacion(ID("c"), Entero( "6" ) , Asignacion(ID("j"), Entero( "7" ) , Si(Conjuncion(Relacional("<=", ID("a"), Entero( "10" ) ), Disyuncion(Relacional(">=", ID("b"), Entero( "20" ) ), Relacional("!=", ID("c"), Entero( "30" ) ))), Asignacion(ID("j"), Suma(ID("j"), Entero( "2" ) )), Asignacion(ID("j"), Entero( "0" ) ), Para(Asignacion(ID("i"), ID("j")), Relacional("<", ID("i"), Entero( "10" ) ), Asignacion(ID("i"), Suma(ID("i"), Entero( "1" ) )), Imprime(ID("i")))))))));

def arbol0e():
    return  Variables(Tipo("int"), ID("a"), Variables(Tipo("float"), ID("x"), Asignacion(ID("a"), ID("x"))));

def arbol1e():
    return  Variables(Tipo("int"), ID("a", ID("b", ID("c"))), Asignacion(ID("a"), Entero( "2" ) , Asignacion(ID("b"), Mult(Entero( "3" ) , ID("a")), Asignacion(ID("c"), Suma(ID("a"), Mult(ID("b"), ID("d"))), Imprime(ID("c"))))));

def arbol2e():
    return  Variables(Tipo("int"), ID("a", ID("b", ID("c"))), Variables(Tipo("float"), ID("d"), Asignacion(ID("a"), Suma(Entero( "2" ) , Mult(Entero( "3" ) , ID("d"))), Imprime(ID("a")))));

def arbol3e():
    return  Variables(Tipo("int"), ID("a", ID("b", ID("c"))), Asignacion(ID("b"), Entero( "2" ) , Asignacion(ID("c"), Entero( "3" ) , Asignacion(ID("a"), Suma(ID("b"), Mult(ID("c"), Real( "2.5" ) )), Imprime(ID("a"))))));

