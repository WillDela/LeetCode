def greetings(name):
  print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")

greetings("Michael")
greetings("Winnie the Pooh")

def print_catchphrase():
    character = input("Enter a character: ").lower()
  
    if character == "pooh":
        print("Oh bother!")
    elif character == "tigger":
        print("TTFN: Ta-ta for now!")
    elif character == "eeyore":
        print("Thanks for noticing me.")
    elif character == "christopher robin":
        print("Silly old bear.")
    else:
        print(f"Sorry! I don't know {character}'s catchphrase!")
  

print_catchphrase()
  

"""
def welcome():
  print("Welcome to The Hundred Acre Wood!")
  
welcome()
welcome()

"""