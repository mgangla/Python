#read from the text file file.txt and output the tenth line

file = open ("file.txt", "r") 

content = file.readlines ()

print (content[9])