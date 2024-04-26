from cryptography.fernet import Fernet

# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key","wb") as key_file :
#         key_file.write(key)

# write_key()

def load_key():
    file =  open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)
def view() :
     with open ("passwords.txt","r") as f: 
        for line in f.readlines():
            data =line.rstrip()
            account,password = data.split("|")
            print("user :", account," | password :" ,fer.decrypt(password.encode()).decode())

def add() :
    name = input("account name : ")
    pwd = input("password : ")

    with open ("passwords.txt","a") as f: 
        f.write(name + "|"+ fer.encrypt(pwd.encode()).decode() + "\n")
    # print(file="passwords.txt",)

while True :
    mode = input("view or add password or q to quit")
    if mode == "q": 
        quit()
    if mode == "view":
        view()
    elif mode == "add" :
        add()
    else : print("invalid mode")
    continue