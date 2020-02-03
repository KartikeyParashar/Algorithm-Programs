# Define a function that takes list of Possible Notes available in Machine
def notes(money):
    # Ask user to input the Amount of Transaction
    amount = int(input("Enter the Amount in Rupees: "))

    # Declare a variable that will be user for traversing a list of Possible notes Available
    i = 0

    # Starting a loop and it will move untill the amount will be zero
    while amount>0:
        numberofNotes = amount // money[i]
        amount = amount % money[i]
        if numberofNotes == 0 :
            i+=1
        else:
            print(f"{money[i]} : {numberofNotes}")
            i+=1


money = [2000,500,200,100,50,20,10,5,1]
notes(money)