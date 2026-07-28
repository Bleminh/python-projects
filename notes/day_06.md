JSON (JavaScript Object Notation):
json.load(file_object): Reads a file that contains JSON text and translates it into a Python list or dictionary. You use this inside your 'r' mode block.
json.dump(python_data, file_object, indent=4): Takes your Python list/dictionary and writes it into the file as JSON text. You use this inside your 'w' mode block. The indent=4 argument is optional but highly recommended—it formats the JSON file with line breaks and spaces so it is readable to humans.
json.load() and json.dump() expect file object variable, not the string name of the file.
with open() -> give the opened file a variable name using as
(Note: Don't confuse load/dump with loads/dumps. The ones with the "s" stand for "load string" and "dump string" and deal with variables in memory, while load and dump deal directly with files).
List Manipulation:
Adding: Use my_list.append(new_item) to add a string to the end of your list.

Removing: Use my_list.pop(index) or del my_list[index] to remove an item.

Zero-Indexing: Remember that Python lists start at 0! If your terminal displays "1. Buy groceries", the user will type 1 to delete it, but in Python logic, that is index 0. You will need to subtract 1 from their input.

Type Conversion: The input() function always returns a string. If the user types "2" to delete the second item, you must convert that to an integer using int() before using it as a list index.

for index, task in enumerate(tasks):
    # index starts at 0, so we add 1 for the user display
    print(f"[{index + 1}] {task}")