import os
from datetime import datetime

file_folder = "DATA"
file_name = "alice.txt"

file_path = os.path.join(file_folder, file_name)

print("file_path: {}\n".format(file_path))

fp = os.path.join("C:", "Users", "John", "Documents", "wombats.txt")
print("fp: {}\n".format(fp))

print("os.path.split():", os.path.split(file_path))
print("os.path.splitext():", os.path.splitext(file_path))
print("os.path.dirname():", os.path.dirname(file_path))
print("os.path.basename():", os.path.basename(file_path))
print("os.path.abspath():", os.path.abspath(file_path))
print()

win_file_path = os.path.join("Program Files", "Microsoft", "notepad.exe")
print("win_file_path: {}\n".format(win_file_path))

file_size = os.path.getsize(file_path)
print("file_size: {}\n".format(file_size))

raw_timestamp = os.path.getmtime(file_path)
print("raw_timestamp: {}\n".format(raw_timestamp))

timestamp = datetime.fromtimestamp(raw_timestamp)
print("timestamp: {}\n".format(timestamp))

#  os.path.getmtime()  .getatime()  .getctime()

for fp in file_path, "DATA/wombats.txt",  "spam", "DATA", "requirements.txt", "hello.py":
    print("{:20s} {!s:5s} {!s:5s} {!s:5s}".format(fp, os.path.exists(fp), os.path.isfile(fp), os.path.isdir(fp)))
print()

print(f"Contents of {file_folder}")
print(os.listdir(file_folder))

for file_name in os.listdir(file_folder):
    file_path = os.path.join(file_folder, file_name)
    print("file_path: {:30s} {!s:5s}".format(file_path, os.path.isfile(file_path)))

wanted = ".txt"

for file_object in os.scandir(file_folder):
    if not file_object.name.endswith(wanted):
        continue  # fail fast
    # from here on, only .txt files are processed
    print(file_object.name, file_object.path, file_object.is_dir(), file_object.is_file())
    # print(file_object.stat())
    print()

# list attributes of file_object
print(dir(file_object))












