"""
A program that checks if a word is spelt the same way both backwards and forward
"""


word :str= str(input('Enter the word or phrase >>'))
# remove symbols
word :str= ''.join(filter(str.isalpha, word)).lower()
lenght :int= len(word)
# you could also reverse it an use == to check if it's equal
if __name__ == '__main__':
    for number in range(lenght):
        if word[number] == word[-1-number]:
            if number == lenght-1:
                print('This is a palindrome')
        else:
            print('This is not a palindrome')
            break