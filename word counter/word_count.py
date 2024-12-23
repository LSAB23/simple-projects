'''
This app just takes in a text docs and count the words and characters in it 
'''
import os
file :str = input('File or path >> ')

path :str = os.path.abspath(file)

# count the all words
def count_words(line:str, word_count :int) -> int:
    
    remove_symbols :str= ' '.join(filter(str.isprintable, line.split()))
    word_count += len(remove_symbols.split())
    return word_count

# count the all characters
def count_chars(line, chars_count) -> int:

    remove_symbols :str = ' '.join(filter(str.isprintable, line.split()))
    chars_count += len(remove_symbols)
    return chars_count

# only try when the path exists
with open(path, 'r') as textfile:
    word_count :int = 0
    chars_count :int = 0
    for line in textfile.readlines():
        word_count+=count_words(line, word_count)
        chars_count+=count_chars(line, chars_count)

print(f' There are {word_count} word(s) and {chars_count} characters in {file}')
