# Here we try to read a file and print its content
# We will use the open() function to open the file and read() method to read its content
file = open('read.txt', 'w')  # 'w' stands for write mode
file.write('Hello, World!')  # Write some content to the file
file.write('\nWelcome to file handling in Python.')  # Write another line to the file 
file.close()  # Close the file after writing
file = open('read.txt', 'a')  # 'r' stands for append mode
file.write('\nThis line is added in append mode.')
file.close() # Close the file after appending
file = open('read.txt', 'r')  # 'r' stands for read mode
# content = file.read(10)  # Read the first 10 characters of the file
content = file.read()  # Read all lines of the file
print(content)  # Print all lines of the file
# content = file.read()  # Read the entire content of the file
# print(content)  # Print the content of the file
file.close()  # Close the file after reading