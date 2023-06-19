"""
File: replace_keyword.py
Name:
----------------------
This file shows how to replace
old_word with new_word in old_s
by calling replace function
"""


def main():
	old_s = input('Old s: ')
	old_word = input('Old word: ')
	new_word = input('New word: ')
	print(replace(old_s, old_word, new_word))


def replace(old_s, old_word, new_word):
	if old_word not in old_s:  # if old_s.find(old_word) == -1
		return "ABC"
	else:
		ans = ""
		i = old_s.find(old_word)
		ans += old_s[:i]
		ans += new_word
		ans += old_s[i+len(old_word):]

	return ans



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
