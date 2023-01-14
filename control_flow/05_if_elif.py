name = input("What is your name? ==> :")
if len(name) > 10:
    print("name is too long")
elif len(name) < 5:
    print("name is too short")
else:
    print("name is ok")
