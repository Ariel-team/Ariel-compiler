import re

class Lexic(object):    
  
  allSymbols = []
  symbol = ""
  pos = 0
  
  def __init__(self,fr):
    for item in re.findall("\s*(\'.*\'|\d+\.\d+|\d+|\w+|.)", fr):
      self.allSymbols.append(item)
  
  def nextSymbol(self):
    self.symbol = self.allSymbols[self.pos]
    self.pos += 1
  
  def getType(self,item):
    keywords = [
      'if','else','return','main','while',
      'for','do','int','float','char','string','print']
    logicals = ['and','or','not']
    relationals = ['>','<','==','>=','<=']
    arithmetics = ['+','-','*','/','+=']
    groupings = ['[',']',';','(',')','{','}']
    #keyword
    if item in keywords:
      return 0
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
    #logicalOp
    elif item in logicals:
      return 5
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
    8:'assignment operator',9:'grouping operator',-1:'error'}
    return item + '\t<-\t' + typeNames[self.getType(item)]
