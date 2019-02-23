# -*- coding: UTF-8 -*-

from cookie import *

from methods import savefile
from methods import signin

if __name__ == '__main__':
    '''
    if len(sys.argv) == 1 or (sys.argv[1] == "-h" or sys.argv[1] == "help"):
        filename = "help.txt"
        if(os.path.isfile(filename) == True):
            user_data = open(filename , "r" ,encoding='utf-8').read()
            print(user_data)
        else:
            print("help file does not exist...")
        sys.exit()
    '''
    signin.search(sys.argv[1], int(sys.argv[2]))
