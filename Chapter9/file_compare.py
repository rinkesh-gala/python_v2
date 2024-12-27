# Write a program to find out whether a file is identical & matches the content of
# another file.

with open("file_copy.txt", "rb") as file1, open("file_copy1.txt", "rb") as file2:
    if file1.read() == file2.read():
        print("The files are identical.")
    else:
        print("The files are different.")

"""
Text Mode ("r") processes file as text, interpreting characters based on the platform's default encoding (e.g.,UTF-8,ASCII).
This can lead to issues like:
Line-ending differences (e.g., \n vs. \r\n between Unix/Linux and Windows).
Encoding mismatches or automatic character conversion.
Binary Mode ("rb") reads the file as raw bytes, ensuring no interpretation or conversion is performed, 
which makes it suitable for comparing any type of file (text or binary).
"""