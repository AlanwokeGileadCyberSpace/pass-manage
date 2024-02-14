# import sqlite3
# import hashlib
import string
from getpass import getpass
import secrets
print('WELCOME TO GILEADS PASSWORD MANAGER')

# conn = sqlite3.connect('password_manager.db')
# cursor = conn.cursor()
# # to create a table to store a text file
# cursor.execute(''' CREATE TABLE IF NOT EXISTS psswords
#                (username TEXT, website TEXT, password TEXT,
#                FOREIGN KEY(username) REFERENCES users(username))''')
# conn.commit()

# def register(username, password):
#     #hash password before storing
#     hashed_password = hashlib.sha256(password.encode()).hexdigest()
#     try:
#         cursor.execute("INSERT INTO users VALUE (?, ?)", (username, hashed_password))
#         conn.commit()
#         print('Successful User Registration.')
#     except sqlite3.IntegrityError:
#         print('username  already exists. Please enter a different username ')
# def login(username, password):
#     hashed_password = hashlib.sha256(password.encode()).hexdigest()
#     cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, hashed_password))
#     if cursor.fetchone():
#         print('Login Successful')
#         return True
#     else:
#         print('Invalid username or password. ')
#         return False
# def update_password(username, website, password):
#     cursor.execute('INSERT INTO passwoeds VALUES (?, ?, ?)', (username, website, password))
#     conn.commit()
#     print('password added successfully')
# def get_password(website):
#     cursor.execute('SELECT * FROM passwords WHERE username=?', (website,))
#     results = cursor.fetchall()
#     if results:
#         for e in results:
#             print(f'Website: {e[1]}')
#             print(f'password: {e[2]}')
#     else:
#         print('No passwords found. ') 

# def generate_password(lenght=8):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(getpass.choice(characters) for i in range(lenght))
#     return password

# with open ('pass.txt', 'a+') as f:
#      f.write (f'{register} {login} {update_password} {get_password} \n')      
              
   


def generate_password(lenght=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(getpass.choice(characters) for i in range(lenght))
    return password

print('\n1. Register')
print('2. Login')
print('3. Update Password')
print('4. Get Passwords')
print('5. Exit')
choice = input('Enter your choice : ')        
if choice == "1":
            firstname = input('Enter your first name')
            lastname = input('Enter your last name')
            email = input('Enter your email address')
            username = input('Enter username: ')


             
            while True:    
                random = input('Do you want a random password: YES OR NO: ').lower
                if random == "yes":
                    random_pass = generate_password()
                    print("Random Password: ", random_pass)
                    break
                elif random == "no":
                    password = input('Enter password: ')
                    while True:
                                if len(password) < 8:
                                    print('Password must be 8 characters long')
                                elif not any(char.isupper() for char in password):
                                    print('Password must contain an uppercase') 
                                elif not any(char.islower() for char in password):
                                    print('Password must contain a lower case')
                                elif not any(char in string.punctuation for char in password):
                                    print('Password must contain a symbol')
                                elif not any(char.isdigit() for char in password):
                                    print('Password must contain a Number')
                                else:
                                    print('password is okay.')
                                    break
                else:
                    print('ennter yes or no')         
            
            # (username, password)
elif choice == "2":
            username = input('Enter username: ') 
            password = input('Enter password: ')
                
        
        
        
                        
elif choice == "3":
            # def create_master_password():
            #         master_password = input("Set your master password: ")
            #         hashed_password = (master_password.encode()).hexdigest()
            #         with open("pass.txt", "a+") as file:

            #             file.write(hashed_password)
                       

            website = input('Enter website name: ')
            while True:    
                random = input('Do you want a random password: YES OR NO: ').lower
                if random == "yes":
                    random_pass = generate_password()
                    print("Random Password: ", random_pass)
                    break
                elif random == "no":
                    password = input('Enter new password: ')
                    while True:
                                if len(password) < 8:
                                    print('Password must be 8 characters long')
                                elif not any(char.isupper() for char in password):
                                    print('Password must contain an uppercase') 
                                elif not any(char.islower() for char in password):
                                    print('Password must contain a lower case')
                                elif not any(char in string.punctuation for char in password):
                                    print('Password must contain a symbol')
                                elif not any(char.isdigit() for char in password):
                                    print('Password must contain a Number')
                                else:
                                    print('password is valid.')
                                    break
                else:
                    print('ennter yes or no')         
            
            # password = getpass.getpass('Enter new password: ')
            # (website, password)
            print('Updated password successfully')        
elif choice == "4":
             def check_master_password():
                    input_password = input("Enter your master password: ")
                    # hashed_input_password = (input_password.encode()).hexdigest()
                    with open("master_password.txt", "r") as file:
                        stored_password = file.read().strip()
                        # if hashed_input_password == stored_password:
                        #     return True
                        # else:
                        #     return False

                # def display_data():
                #     if check_master_password():
                #         with open("pass.txt", "r") as file:
                #             data = file.read()
                #             print("Data:", data)
                #     else:
                #         print("Incorrect master password")
    
                # (website)
             
                #         
elif choice == "5":
else:
      print()
        
# else:
#     print('Invalid input for choice, please try again')



# import sqlite3
# import getpass
# import string              

    
                # Main program
                # create_master_password()  # Run this once to set the master password
                # display_data()  # Prompt the user to enter the master password before displaying the data
                
                            
            
                # website = input('Enter website name: ')

    # conn.close()
# if __name__ == "__main__":
#     main()       

            # if login(username, password):
           
# with open ('pass.txt', 'w') as f:
#     f.write (f'{username} {website} {password} \n')    
#     import hashlib

# def create_master_password():
#     master_password = input("Set your master password: ")
#     hashed_password = hashlib.sha256(master_password.encode()).hexdigest()
#     with open("pass.txt", "w") as file:
#         file.write(hashed_password)

# def check_master_password():
#     input_password = input("Enter your master password: ")
#     hashed_input_password = hashlib.sha256(input_password.encode()).hexdigest()
#     with open("pass.txt", "r") as file:
#         stored_password = file.read().strip()
#         if hashed_input_password == stored_password:
#             return True
#         else:
#             return False

# def display_data():
#     if check_master_password():
#         with open("data.txt", "r") as file:
#             data = file.read()
#             print("Data:", data)
#     else:
#         print("Incorrect master password")

# # Main program
# create_master_password()  # Run this once to set the master password
# display_data()  # Prompt the user to enter the master password before displaying the data
  
              
                   

 






# print('Welcome to Gileads password manager')
# ab = input('Enter your username : ')
# ap = input('Enter your password : ')


# print(f'Connecting with username {ab} and password {ap}')


# import hashlib

# def create_master_password():
#     master_password = input("Set your master password: ")
#     hashed_password = hashlib.sha256(master_password.encode()).hexdigest()
#     with open("master_password.txt", "w") as file:
#         file.write(hashed_password)

# def check_master_password():
#     input_password = input("Enter your master password: ")
#     hashed_input_password = hashlib.sha256(input_password.encode()).hexdigest()
#     with open("master_password.txt", "r") as file:
#         stored_password = file.read().strip()
#         if hashed_input_password == stored_password:
#             print("Access granted")
#             # Add code here to access the user's data
#         else:
#             print("Incorrect master password")

# # Main program
# create_master_password()  # Run this once to set the master password
# check_master_password()   # Prompt the user to enter the master password


