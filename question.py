finish = False
while finish == False:
    print("Do you want to continue?: ")
    answer = input()
    if answer == "yes":
        print (answer)
    # Do this.
    elif answer == "no":
        print("no")
        finish = True
    else:
        print("I don't understand you, sorry!")
    # Do that.
