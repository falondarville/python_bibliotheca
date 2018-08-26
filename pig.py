# ORIGINAL EXERCISE: http://openbookproject.net/pybiblio/practice/wilson/piglatin.php

# Translation rules
# If a word has no letters, don't translate it.
# All punctuation should be preserved.
# If the word begins with a capital letter, then the translated word should too.
# Separate each word into two parts. The first part is called the prefix and extends from the beginning of the word up to, but not including, the first vowel. (The letter y will be considered a vowel.) The Rest of the word is called the stem.
# The Pig Latin text is formed by reversing the order of the prefix and stem and adding the letters ay to the end. For example, sandwich is composed of s + andwich + ay + . and would translate to andwichsay.
# If the word contains no consonents, let the prefix be empty and the word be the stem. The word ending should be yay instead of merely ay. For example, I would be Iyay.

# Phase 1
# Your first task is to produce a function that takes one argument, a word, and returns the portion of the word up to, but not including the first vowel. For example, if you sent 'banana' to your function, it should return 'b'. Sending 'Sibley' should return 'S', 'stream' should return 'str', and 'break' should return 'br'. Print out your working function and a sample run.

def translate(word):
	vowels = ["a", "e", "i", "o", "u"]
	new_word = []
	for i in word:
		if i not in vowels:
			new_word.append(i)
		else:
			break
	return new_word

print(translate("falon"))
print(translate("great"))

