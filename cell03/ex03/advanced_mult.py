i = 0
while i <= 10:
    j = 0
    print(f"Table de {i}: ", end="")
    while j <= 10:
        result = i*j
        print(result, end=" ") # end = " " having space, has to follow after , comma.
        j+=1
    print() #Skip the line 
    i += 1