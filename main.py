import pathlib
import random

#adding more word options from wordlist.txt
WORDLIST = pathlib.Path("wordlist.txt")

words = [
  word.upper()
  for word in WORDLIST.read_text(encoding="utf-8").strip().split("\n")
]
word = random.choice(words)

#runs a loop for 6 guesses
for guess_num in range(1, 7):
  guess = input(f"\nGuess {guess_num}: ").upper() #users input
  #test if the guess == (same as) WORD
  if guess == word:
    print("Correct")
    break

else: 
  print(f"the word was {word}")

  correct_letters = {
    letter for letter, correct in zip(guess, word) if letter == correct
  }
  misplaced_letters = set(guess) & set(word) - correct_letters
  wrong_letters = set(guess) - set(word)

  print("Correct letters:", ", ".join(sorted(correct_letters)))
  print("Misplaced letters:", ", ".join(sorted(misplaced_letters)))
  print("Wrong letters:", " ,".join(sorted(wrong_letters)))

