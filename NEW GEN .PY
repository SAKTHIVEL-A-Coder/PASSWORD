import random
print("WELCOME TO MY PASSWORD GENERATOR")
print("********************************")
#input function
letters = int(input("NUMBER OF ALPABETS:"))
symbols = int(input("NUMBER OF NUMERICAL:"))
numbers = int(input("NUMBER OF SPECIALCHAR:"))
#declarations
ALPABETS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
NUMERICAL = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SPECIALCHAR = ['!', '#', '$', '%', '&']
#conditions 
Passcode='THIS IS YOUR passcode='
for sec in range(0,letters):
    Passcode+=random.choice(ALPABETS)
for sec in range(0,symbols):
    Passcode+=random.choice(SPECIALCHAR)
for sec in range(0,numbers):
    Passcode+=random.choice(NUMERICAL)
print(Passcode)