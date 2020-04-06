# -*- coding: utf-8 -*-
# @Author: Jiang Ji
# @Date:   2020-04-06 13:50:55
# @Last Modified by:   Jiang Ji
# @Last Modified time: 2020-04-06 14:18:46
'''
python 3.7.5
'''
import re
import itertools

def solve(puzzle):
    '''将输入拆分成一个个单词
    
    Parameters
    ----------
    puzzle : [type]
        [description]
    
    Returns
    -------
    [type]
        [description]
    '''
    words = re.findall('[A-Z]+',puzzle.upper()) # findall接受一个正则表达式和字符串作为输入
    unique_characters = set(''.join(words))
    assert len(unique_characters) <= 10, 'Too many letters'
    first_letters = {word[0] for word in words}
    n = len(first_letters)
    sorted_characters = ''.join(first_letters) + ''.join(unique_characters - first_letters)
    characters = tuple(ord(c) for c in sorted_characters) # ord() 转为ASCII数值
    digits =  tuple(ord(c) for c in '0123456789') # tuple将列表转为远足
    zero = digits[0]
    for guess in itertools.permutations(digits,len(characters)):
        if zero not in guess[:n]:
            equation = puzzle.translate(dict(zip(characters,guess)))
            if eval(equation):
                return equation

if __name__ == '__main__':
    import sys
    for puzzle in sys.argv[1:]:
        print(puzzle)
        solution = solve(puzzle)
        if solution:
            print(solution)
