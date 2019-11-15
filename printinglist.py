# A function that prints the content of a list:
def printlist(mylist):
    formatted_content = ""
    counter = 1
    print() # An empty line first. Looks better.
    for elem in mylist:
        if(counter == 1):
            formatted_content += elem
        elif(counter == le(mylist)):
            formatted_content += " and "+elem
        else:
            formatted_content += ", "+elem
        counter = counter + 1
    print(formatted_content)
    print() # An empty line.
