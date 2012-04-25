import re
import Lexic
from Lexic import *

class Sintactic(object):
  
  Lex = Lexic()
  
  def init(self,fr):
    self.Lex.init(fr)
    self.Lex.nextSymbol()
    print self.Lex.allSymbols
    print self.Lex.symbol
    print self.Lex.getType(self.Lex.symbol)
