import json

def reg_username_validate(username):
    import re
    x = re.search("^[a-z][A-Za-z0-9._-]*@[A-Za-z].[A-Z|a-z]{2,3}", username)
    if x:
        uN=username
        return True
    else:
        print("Enter valid Username")
        return False
    

def reg_pass_validate(password):
    import re
    #while True:
        #password=input("Enter Password")
    if 5 > len(password) or len(password) > 16:
        print("Enter password of lenght between 5 to 16")
    elif re.search("[a-z]", password) is None:
        print("Make sure password has one lowercase character")
    elif re.search("[A-Z]", password) is None:
        print("Make sure password has one uppercase character")
    elif re.search("[0-9]", password) is None:
        print("Make sure password has one number")
        return False
    else:
        return True


def register(usr):
    userN=False
    while not userN:
        username = input("Name: ")
        userN=reg_username_validate(username)
    passW=False
    while not passW:
        password=input("Enter Password")
        passW=reg_pass_validate(password)
    usr[username] = password
    print(username,usr[username])
    writeUsers(usr)
    

    


def login(usr):
    print("-------- LOGIN --------")
    uN = input("Name: ")
    pW = input("Password: ")

    if uN in usr.keys():
        if pW == usr[uN]:
            print("Welcome back.\t:",uN)
            return True
        else:
            pp=input("Incorrect password. If you wanna give FORGET PASSWORD please Enter FORGET PASSWORD")
            if pp.lower() == "forget password":
                print("Your Password is \t:",usr[uN])
                print("Please Login again")
            return False
    else:
        print("Username didn't exist . Please Register")
        print("-------- REGISTER --------")
        register(usr)
        print("Successfully Registered")
        print("  THANK YOU  ")
        return True
    

def readUsers():
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def writeUsers(usr):
    with open("users.json", "w+") as f:
            json.dump(usr, f)

username=''
password=''
users = readUsers()
success = login(users)

while not success:
    success = login(users)
