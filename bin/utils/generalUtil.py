'''
This is a list of general funcs that might be helpful and used throughout the program
'''

__Author__ = 'Harry Burge'
__Date__ = '4/1/2020'


# Imports


# Util Contents

# Searchs multiple items in a list
def search_items_to_list(items, target_list):
    for i in items:
        return True if i in target_list else None
    return False


if __name__ == '__main__':
    raise RuntimeError('This module can\'t be ran by itself. Please run AmericanFootballAI.py')
