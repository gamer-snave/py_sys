# print("What do you think is funny today?:")
# funny=input('type something short here: ')
password_list=[]
with open('list.txt', 'r') as pas:
    for password in pas.readlines():
        password_list.append(password.strip('\n'))
while True:
    user_password=input('enter your password: ')
    if user_password in password_list:
        break
    print("Invalid Password!")
    





    
            
        
 