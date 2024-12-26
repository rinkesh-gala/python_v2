# Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle

with open("file_find.txt") as content:
    content_read = (content.read()).lower()
    
if("twinkle" in content_read):
    print("file has \"twinkle\" word")
else:
    print("file doesn't have \"twinkle\" word")