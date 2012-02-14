import sys
import re
import Lexic
from Lexic import *

def main():
  if len(sys.argv)<=1:
      print 'Usage: python Compiler.py <filename>'
      return
  
  arg = sys.argv[1]
  f = open(arg,'r')
  fr = f.read()
  Lex = Lexic()
  for item in re.findall("\s*(\'.*\'|\d+\.\d+|\d+|\w+|.)", fr):
    print Lex.getTypeName(item)
  return

if __name__ == '__main__':
  main()
