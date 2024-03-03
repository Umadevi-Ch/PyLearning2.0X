# File Handlings
#File Handling means how to read a text and write into  it using Python code

"""To read a file
1.Which function we have to use to read a file
to read a file we have an inbuilt function:"""

#Open("file_name", "mode")

# Mode-
# 'r' for reading (default)
# 'w' for writing (creates a new file  or truncates an existing one)
# 'a' for appending
# 'b' for  binary mode   vlc.exe or zoom.exe file is nothing but binary file
# '+' for updating (reading  and writing)

# Read and Write the content
# Read a file
# Reading Entire content : content = file_object.read()
# line = file_object.readline() for a single line
# lines = file_object.readlines() for all the lines in a list


# close the file


file = open("TestData", 'r')
content = file.read()
print(content)
file.close()
