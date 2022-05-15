print("Please Login")
trials=0
username=input("Enter your username: ")
def checkPassword():
    global trials
    for trials in range(3):
        password=input("Enter your password: ")
        # trials+=1
        if password=='Snave2015':
            print('Login Success!')
            exit()
    
        else:
            print("Incorrect Password!")
            if trials==3:
                print("Too many Trials!")
                exit()
checkPassword()