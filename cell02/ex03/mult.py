first_num = int(input("Enter the first number:\n"))
sec_num = int(input("Enter ther second number:\n"))
result = first_num * sec_num
print (f"{first_num} x {sec_num} = {result}")
if result > 0:
    print("The result is positive")
elif result < 0:
    print("The result is negative")
elif result == 0:
    print("The result is both positive and negative")
    
