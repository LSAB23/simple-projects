import random

with open('words.txt', 'r+') as words:
	word :list= words.readlines()

generated_word :str = str(random.choice(word).lower())

guess :list = list(''.join(' ' for i in range(len(generated_word)-1)))

# guess_to_str :str= ''
word_len :int= len(generated_word)

# check if a word is in the generated word and add 
def check_and_add(word):
	global guess_to_str
	for index,letter in enumerate(generated_word):
		if letter == word and guess[index] == ' ':
			guess[index] = word

	guess_to_str = str(''.join(guess)).replace(' ', '_').lower()


	print(str(''.join(_ for _ in guess)).replace(' ', '_'))


if __name__ == '__main__':
	print(f'''{generated_word}
	you can enter one or two guesses
	'''
	)

	guesses = 0


	while guesses < 6:
		user_input :str= input('Enter guess >> ') or ''

		guess_len :int= int()

		if user_input is '':
			print('it cannot be empty')

		if user_input not in guess and user_input is not None or user_input in guess:
			guess_to_str :str= str(''.join(guess)).replace(' ', '_').lower()
			guess_len :int= len(guess_to_str)
			guesses+=1

			for number in range(len(user_input)):
				check_and_add(user_input[number])


		if  word_len - 1 == guess_len:
			is_equal :bool= False
			for num in range(guess_len):
				if guess_to_str[num] == generated_word[num]:
					is_equal :bool= True
				else:
					is_equal :bool= False
					break
			if is_equal:
				print(f'You guessed right the answer was {generated_word}')
				break
	else:
		print(f'Guesses ran out the word was {generated_word}...')