from asyncore import write
from cgi import test
from distutils.file_util import write_file

'''
f = open('test.txt')

print(f.read()) # read & prints it
print(f.read()) # wont print for the second time
# because once python read the file, it goes to the end of the file,
# we have to reset it back to the start of the file to read again
f.seek(0) # seeks the read to start of the file
print(f.read()) # now it prints twice. 
f.seek(0)
print(f.readline()) # reads all line
# lets try playing with the seek function tho
f.seek(3)
print(f.read()) # we can see, the word "yea" is gone from the output,
# so seek() will move the reading cursor in the file, nice
f.seek(0)

# trying one small loop
for words in open("test.txt"):
    print(words) # instead of words we can use line too
# prints the all the line
'''
WriteFile = open("testWrite.txt","w")
WriteFile.write("This is a new line i am adding ")
# creates and adds the line.
WriteFile.write("and i am trying to add some more lines")
WriteFile.write(", Now i aunderstood it will rewrite the file instead of appeding content")