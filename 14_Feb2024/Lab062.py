#Home-Please  complete
# Fact Program with the function
# Default= 1

#Reverse a String
#str = "Pramod"
#rev_str = ""
#for c in str:
 #rev_str = c+rev_str
#print(rev_str)
def reverse_string(str):

    rev_str = ""
    for c in str:
        rev_str = c+rev_str
    return rev_str

name= reverse_string("Pramod")
print(name)
