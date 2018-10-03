import os
import random

try: #Kollar in vi har filen "accounts.txt" där vi ska lagra alla kontonamn. Finns filen inte skapas den
    accounts = open("accounts.txt", "r")
    accounts.close()
except:
    accounts = open("accounts.txt", "w")
    accounts.close()
try: #Kollar om adminfilen finns. Finns den inte skapas den och ges ett standard lösenord.
    admin = open("admin.txt", "r")
    admin.close()
except:
    admin = open("admin.txt", "w")
    admin.write("123456")
    admin.close()
    print("\nAdmin password set to default. Password is 123456.")

class User:
    def __init__(self, name, password, file):
        self.name = name
        self.file = file
        self.password = password
        print("\nWelcome {}" .format(self.name))
        y = True
        while y == True:
            try:
                option1 = int(input('''[1] Play 
[2] Check currency
[3] Change password
[4] Game instruction
[5] Logout'''))
                if option1 == 1: #Spela spelet
                    with open(self.file, "r") as f:
                        line1 = f.readline() #Läser första raden i filen
                        currency = int(f.readline()) #Läser andra raden i filen
                    if currency >= 5:
                        currency -= 5
                        while True:
                            try:
                                value1 = int(input("Input your first number between 1-10"))
                                value2 = int(input("Input your second number between 1-20"))
                                if value1 < 1 or value1 > 10 or value2 < 1 or value2 > 20:
                                    print("You can only choose between the given numbers")
                                else:
                                    break
                            except:
                                print("You can only choose between the given numbers")
                        random1 = random.randrange(1, 10)
                        random2 = random.randrange(1, 20)
                        if value1 == random1 and value2 == random2:
                            print("\nYou win 50 currency")
                            currency += 30
                            with open(self.file, "w+") as g:
                                g.write(self.password)
                                g.write(str(currency))

                        elif value2 == random2:
                            print("\nYou win 20 currency")
                            currency += 20
                            with open(self.file, "w+") as g:
                                g.write(self.password)
                                g.write(str(currency))
                        elif value1 == random1:
                            print("\nYou win 10 currency")
                            currency += 10
                            with open(self.file, "w+") as g:
                                g.write(self.password)
                                g.write(str(currency))
                        else:
                            print("\nYou lose")
                            with open(self.file, "w+") as g:
                                g.write(self.password)
                                g.write(str(currency))
                    else:
                        print("You dont have enough curency.\n Contact admin to add more currency")
                elif option1 == 2: #Kolla hur mycket pengar du har
                    with open(self.file, "r") as f:
                        line1 = f.readline()
                        print(int(f.readline()))
                elif option1 == 3: #Ändra ditt lösenord
                    with open(self.file, "r") as f:
                        line1 = f.readline()
                        currency = int(f.readline())
                    with open(self.file, "w+") as g:
                        g.write(input("New password") + "\n")
                        g.write(str(currency))
                elif option1 == 4: #Logga ut
                    print('''You start with 100 currecy. 
For each time you play you will be charged with 5 currency.
You will get to choose 2 numbers, first between 1-10 and then between 1-20.
The game will random take out numbers between the given numbers.
If your first number is correct you will get 10 currency, if your 
second number is correct you will ger 20 currency and if both is correct
you will ger 50 currency.''')

                elif option1 == 5: #Logga ut
                    print("Goodbye")
                    y = False
                else:
                    print("You can only choose 1,2,3, or 4")
            except:
                print("You can only choose 1,2,3, or 4")

class Admin:
    def admin(self):
        y = True
        while y == True:
            try:
                option1 = int(input('''[1] Remove account
[2] List accounts
[3] Change password
[4] Add currency to player
[5] Logout'''))
                if option1 == 1: #Här tar vi bort ett konto
                    accname1 = input("What account do you want to remove?")
                    accname = accname1 + ".txt"
                    try:
                        r = open(accname, "r")
                        r.close()
                        os.remove(accname) #Tar bort kontots .txt fil
                        acc = []

                        with open('accounts.txt', 'r') as accounts: #Här under tar vi bort kontonamnet från filen som inehåller alla kontonamn
                            acc = [line.strip() for line in accounts] #Gör filen till en list
                        acc.remove(accname1) #Tar bort namnet från listan
                        with open("accounts.txt", "w") as accounts:
                            for x in acc:
                                accounts.write(x + "\n") #Lägger tillbaka listan i account filen
                        print("Account has been removed")
                        continue
                    except:
                        print("The account does not exist")
                        continue
                elif option1 == 2: #kollar vilka konton som finns
                    accounts = open("accounts.txt", "r")
                    print(accounts.read())

                    accounts.close()

                elif option1 == 3:#ändrar till eget admin lösenord
                    adminfile = open("admin.txt", "w")
                    adminfile.write(input("New password"))
                    adminfile.close()
                elif option1 == 4: #Lägger till currency till spelare
                    accname = input("Account name")
                    accname = accname + ".txt"
                    try:
                        with open(accname, "r") as f: #Försöker öppna angivet konto
                            password = f.readline()  # Läser första raden i filen
                            currency = int(f.readline())  # Läser andra raden i filen
                        while True:
                            try:
                                addcurrency = int(input("How much du you want du add?"))#Frågar hur mycket du vill lägga till
                                break
                            except:
                                print("You can only putin numbers")
                        currency = currency + addcurrency #Adderar det man vill lägga till med det som redan fanns
                        with open(accname, "w+") as g:
                            g.write(password)
                            g.write(str(currency)) #Lägger in den nya currensyn
                    except:
                        print("The account does not exist")

                elif option1 == 5:
                    print("Goodbye")
                    y = False

                else:
                    print("You can only choose 1,2,3, or 4")
            except:
                print("You can only choose 1,2,3, or 4")
x = True
while x == True:
    try:
     option = int(input('''[1] Login
[2] Create account
[3] Login as admin
[4] Exit
'''))
     if option == 2: #Här skapar vi en .txt fil så kontot man skapar sparas
         name = input("Username:")
         if os.path.isfile(name + ".txt") == False:
             accounts = open("accounts.txt", "a+")
             accounts.write("\n" + name)
             accounts.close()
             name = name + ".txt"
             Password = input("Password:")
             create = open(name, "w+") #varje användare får en egen fil. Användarnamnet är filnamnet
             create.write(Password + "\n" + "100")
             create.close()
         else:
             print("The accountname already exists")
             continue

     elif option == 1: #Logga in
         name = input("Username:")
         name2 = name + ".txt"
         Password = input("Password:")
         try: #Här kollar vi om användaren finns
            read = open(name2, "r")
            x = read.readline()
            password = Password +"\n"
            read.close()
            if x == password:
                user = User(name, password, name2)
                x = False
                break
            else:
                x = True
                print("Username or password is incorrect")
         except:
            print("Username or password is incorrect")
     elif option == 3: #Logga in som admin
         Password = input("Password:")
         admin = open("admin.txt", "r")
         for x in admin:
             if x == Password:
                 admin1 = Admin()
                 admin1.admin()
             else:
                 print("Password is incorrect")
     elif option == 4: #Avsluta programmet
         print("Goodbye")
         break
     else:
         print("You can only pick 1, 2 or 3")
    except:
        print("You can only pick 1,2 or 3")