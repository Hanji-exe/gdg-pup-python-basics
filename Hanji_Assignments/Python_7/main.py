try:
    with open('Sample.txt', 'r') as file:
        contents = file.read()
        print("Contents of the file: ")
        print(contents)

except FileNotFoundError:
    print("The file 'Sample.txt' was not found.")

with open('NewFile.txt', 'w') as file:
        file.write("This is a New file, Try Natin if gumagana ba talaga ito or eme eme lang itong code na ito XD.\n")
        print("\nNew file created with content: ")

with open('NewFile.txt', 'r') as file:
        newfile_contents = file.read()
        print(newfile_contents)

print("Angas! Gumana siya!\n\n")
    