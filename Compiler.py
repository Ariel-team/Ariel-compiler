import sys
import re
import Sintactic
from Sintactic import *

def main():
  if len(sys.argv)<=1:
    print 'Usage: python Compiler.py <filename>'
    return
  
  arg = sys.argv[1]
  f = open(arg,'r')
  fr = f.read()
 
  Sin = Sintactic()
  #timein = time.time()
  Sin.init(fr)
  #timeout = time.time()
  #print timeout-timein
  return

if __name__ == '__main__':
  main()
