decimal_number = float(input("Enter the Number you want to convert in binary: "))


def toBinary(number):
    place = 1
    binary = 0
    tempDecimal = number
    while tempDecimal > 0:
        rem = tempDecimal % 2
        binary = binary + rem*place
        place = place * 10
        tempDecimal = tempDecimal//2
    return binary

        
print(f"The binary conversion of {decimal_number} is ----> {toBinary(decimal_number)}")