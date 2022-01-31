from help import show_help
from inputs.input_add import input_add
import sys
import os

if __name__ == '__main__':
    if  sys.argv[1] == 'help':
       show_help()
    elif sys.argv[1] == 'add':
       input_add()
