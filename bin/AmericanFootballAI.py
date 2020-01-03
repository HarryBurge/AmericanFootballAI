#!/usr/bin/python
#!/usr/bin/env python3

'''
This is the shortcut/menu for the AmericanFootball AI program suite.
This file will take the option chosen by the user and will start the execution of it.
'''

__Author__ = 'Harry Burge'
__Date__ = '3/1/2020'


# Imports
import sys
import lib.solomain as solomain


# Main
def main(args):
    help = False
    option = None

    for arg in args:
        # TODO: Make it so multiple options can't be chosen
        if arg in ['s','S','-s','-S']:
            option = 's'

        elif arg in ['h','H','-h','-H','--help','--Help','--hlp']:
            help = True

        else:
            raise RuntimeError(f'Invalid Argument ({arg}) passed. Please use --help for more info.')

    if option == 's':
        # TODO: Help statement
        solomain.main() if not help else print('''\n
        Help statement for solo main option.
        ''')

    else:
        # TODO: Help statement
        if not help:
            raise RuntimeError('Please pass an Argument, pass --help for more info.')
        else:
             print('''\n
             All options help statement.
             ''')





if __name__ == '__main__':
    main(sys.argv[1:])
