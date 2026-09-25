from random_word import RandomWords

name = input("Enter name: ")
print("Hello " + name + " time to play hangman!")

r = RandomWords()
secret_word = r.get_random_word().lower()

guess_string = ""

lives = 10

while lives > 0:

	character_left = 0

	for character in secret_word:

		if character in guess_string:

			print(character)
		else:
			print("-")
			character_left += 1

	print()		

	if character_left == 0:
		print("You won!!!")
		break

	guess = input("Guess a word: ").lower()

	guess_string += guess

	if guess not in secret_word:
		lives -= 1
		print("Wrong!")
		print(f"You have {lives} left")

		if lives == 0:
			print(f"You died! The word was: {secret_word}")
			