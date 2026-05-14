# Here we try to read a file and print its content
# We will use the open() function to open the file and read() method to read its content
file = open('read.txt', 'r')  # 'r' stands for read mode
content = file.read(10)  # Read the first 10 characters of the file
print(content)  # Print the content of the file
file.close()  # Close the file after reading