name = input("Give me your name: ")
name = name.replace("\n", "")
if (name != ""):
    age = int(input ("Inform your age:"))
    if (age >= 100):
        print(name,"just have 100 years old or more")
    elif(age >= 0):
        print(name,"will have 100 years in ",100 - age,"years.")
    else:
        print("Oh my gosh",name,"even born yet.")
else:
    print("Do you havent a name?")