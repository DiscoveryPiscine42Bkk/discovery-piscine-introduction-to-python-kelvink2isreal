def greetings(name=None):
    if name == None:
        print("Hello, noble stranger")
    elif isinstance(name,str):
        print(f"Hello, {name}")
    else:
        print("Error! It is not a name")

greetings("Alexendra")
greetings("Will")
greetings()
greetings(42)