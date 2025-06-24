number = float(input("Give me a number: "))
    # Check if the float has a fractional part (i.e., is not a whole number)
if number.is_integer(): #Checking the input is integer or not 
    print("This number is an integer.")
else:
    print("This number is a decimal.")

