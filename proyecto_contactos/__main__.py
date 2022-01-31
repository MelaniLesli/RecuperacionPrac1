from help import show_help
from inputs.input_add import input_add
from inputs.input_rm import rm_contact
import sys
import os

if __name__ == '__main__':
#    if sys.argv[1] == 'init':        
    if  sys.argv[1] == 'help':
       show_help()
    elif sys.argv[1] == 'add':
       input_add()
    elif sys.argv[1] == 'rm':
        rm_contact()
#    else:
 #       print('ERROR: please, initialize the contacts store first with `contacts init`.')
