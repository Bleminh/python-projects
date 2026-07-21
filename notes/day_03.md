21/07/2026

f = open("filename", "mode", encoding=None)

mode: "r" = read, "w" = write (replace the old file), "a" = appending (any data will be added to the end), "r+" = read + write. Mode is optional, default is "r". Add b opens binary mode

encoding="utf-8" is recommended (UTF-8 is the modern de-facto standard)

good practice: use "with" when dealing with file opject (with open...)

f.read(size): reads some quantity of data and returns it as a string (text mode) or bytes object (bin mode). size ommited/negative -> entire content will be read and returned

f.readline() reads a single line.

loop over the file for reading lines:
for line in f:
    print(line, end=' ')

or list(f)/f.readlines()