# Write a python program to rename a file to “renamed_by_ python.txt.

from pathlib import Path
import os

#approach1
directory = "~/github_repo/python_v2/Chapter9"
old_name ="rename_file_1.txt"
new_name="rename_file.txt"

os.rename(old_name,new_name)
print(f"File renamed from {old_name} to {new_name}")

#approach2
old_path = Path("rename_file_1.txt")
new_path = Path("rename_file.txt")

old_path.rename(new_path)