import re

class Lexic(object):    
  
  def __init__(self,fr):
    self.allSymbols = []
    self.symbol = ""
    self.pos = 0

    for item in re.findall("\s*(\'.*\'|\d+\.\d+|\d+|\w+|==|\+=|<=|>=|.)", fr):
      self.allSymbols.append(item)


  def nextSymbol(self):
    try:
      self.symbol = self.allSymbols[self.pos]
      self.pos += 1
    except:
      self.symbol = ''


  def getType(self,item):
    keywords = [
      'if','else','return','main','while',
      'for','do','print']
    types = ['int','float','char','string']
    logicals = ['and','or','not']
    relationals = ['>','<','==','>=','<=']
    arithmetics = ['+','-','*','/','+=']
    groupings = ['[',']',';','(',')','{','}']
    #keyword
    if item in keywords:
      return 0
    #types
    if item in types:
      return 10
    #logicalOp
    elif item in logicals:
      return 5
    #int
    elif re.search(r'^\d+$',item):
      return 1
    #float
    elif re.search(r'^\d+\.\d+$',item):
      return 2
    #identifier
    elif re.search(r'^[\w][\w|\d]*$',item):
      return 3
    #string
    elif re.search(r'^\'.*\'$',item):
      return 4
    #relationalOp
    elif item in relationals:
      return 6
    #arithmeticOp
    elif item in arithmetics:
      return 7
    #assignmentOp  
    elif item == '=':
      return 8
    #groupingOp
    elif item in groupings:
      return 9
    #error  
    else:
      return -1


  def getTypeName(self,item):
    typeNames = {0:'keyword',1:'int',2:'float',3:'identifier',4:'string',
    5:'logical operator',6:'relational operator',7:'arithmetic operator',
    8:'assignment operator',9:'grouping operator',-1:'error',10:'type'}
    return item + '\t<-\t' + typeNames[self.getType(item)]


if __name__ == '__main__':
    data = open('test.ari')
    l = Lexic(data.read())
    while True:
        print l.getTypeName(l.symbol)
        l.nextSymbol()
