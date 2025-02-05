# Write a python function to remove a given word from a list and strip it at the same time
# strip function removes all the mentioned/passed character if they appear in starting/training in a word



def rm_strip(l,word):
    strip_l = []
    for item in l:
        if (word==item):
            l.remove(word)
        else:
            strip_l.append(item.strip(word))
    print(strip_l)


l = ["rinkesh", "rohan", "more", "malay", "himalay"]
rm_strip(l,"rhney")