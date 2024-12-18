# Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

word_dict = {
    "congrats": "thanks",
    "low": "down"
}

word_search = input("enter a word to search:")
print(word_dict.get(word_search))
print(word_dict[word_search])

