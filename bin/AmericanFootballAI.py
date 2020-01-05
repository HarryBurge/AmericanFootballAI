#!/usr/bin/python

'''
This is the shortcut/menu for the AmericanFootball AI program suite.
This file will take the option chosen by the user and will start the execution of it.
'''

__Author__ = 'Harry Burge'
__Date__ = '3/1/2020'


# Imports
import sys
from mains import solomain
from utils import generalUtil


# Main
def main(args):

    # Gets options from arguments
    help, option = False, None

    # TODO: Add options under in an elif
    if generalUtil.search_items_to_list(['-s','-S'], args):
        option = singular_assign(target=option, input='s')

    if generalUtil.search_items_to_list(['-h','-H','-hlp','--help','--Help'], args):
        help = True

    # Uses options found to execute correct option
    # TODO: Add options under in an elif
    if option == 's':
        # TODO: Help statement
        solomain.main() if not help else print('''\n
        Help statement for solo main option.
        ''')

    else:
        # TODO: Help statement
        if not help:
            raise RuntimeError('Please pass a valid Argument, pass --help for more info.')
        else:
             print('''\n
             All options help statement.
             ''')


# Makes sure only one option choosen
def singular_assign(target, input):
    if target == None:
        return input
    else:
        raise RuntimeError('Multiple options choosen, pass --help for more info.')


if __name__ == '__main__':
    main(sys.argv[1:])
