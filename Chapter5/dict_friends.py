# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

friend_lang_dict ={}

friend_name = input("enter your name:")
friend_lang = input("enter your language:")
friend_lang_dict.update({friend_name:friend_lang})

friend_name = input("enter your name:")
friend_lang = input("enter your language:")
friend_lang_dict.update({friend_name:friend_lang})

print(friend_lang_dict)



