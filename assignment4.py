
#task 1 : read a file and handle errors
# if file exists
file_path = ("myfile.txt")
try:
    with open(file_path, 'r') as file1:
        n1file = file1.read()
        print(n1file)
except FileNotFoundError:
    print(f"File '{file_path}' was not found")
'''
# if file doesn't exist
file_path = ("11myfile.txt")
try:
    with open(file_path, 'r') as file1:
        n1file = file1.read()
        print(n1file)
except FileNotFoundError:
    print(f"File '{file_path}' was not found")
'''

'''
# task 2: write and append data to a file
file2 = open('output.txt','r')
readfile = file2.read()
print (readfile)
file2.close()
file2 = open('output.txt','a')
appending_file = file2.write('Learning file handling in Python.')
file2.close()
'''