class CarShowroom:
    def __init__(self):
        self.users = {}
        self.names ={}
        self.contact = {}
        
    def register(self):
        print()
        print("Registration")
        username = input("Username:")
        password = input("Password:")
        name = input("Name    :")
        contact = input("Contact :")
        
        self.users[username] = password
        self.names[username] = name
        self.contact[username] = contact
        print(self.users)
        print()
        self.login()
        
    def login(self):
        choice = input("Are you already registered ?(Y/N) :").upper()
        if choice == "N":
            self.register()
            
        elif choice == "Y":
            while True:
                username = input("Username: ")
                password = input("Password: ")
                if username in self.users and password == self.users[username]:
                    print("Login Successful")
                    self.uname = username
                    break
                else:
                    print("Invalid username or password !\nPlease try again")   
                print()
        else:
            print("Invalid input")
            self.login()
            
        print()
    
    def company(self):
        print()
        self.login()
        while True:
            print("Choose your dream car")
            print("1. Ford\n2. Toyota\n3. Hyundai")
            choice = input("Enter your choice: ").upper()
            if choice == "FORD" or choice =="1":
                self.models("Ford")
                
            elif choice == "TOYOTA" or choice =="2":
                self.models("Toyota")
                
            elif choice == "HYUNDAI" or choice == "3":
                self.models("Hyundai")
                
            else:
                print("Oh no! It seems we don't have that brand.")
                cont = input("Would you like to purchase from the above mentioned brands?(Y?N)").upper()
                if cont == "Y":
                    continue
                elif cont == "N":
                    print("We're sorry to see you go")
                    self.company()
                    
    def models(self,brand):
        print()
        if brand == "Ford":
            print("The available models are:\n 1.Endeavour\n2.Ecosport")
            while True:
                model = input("Enter desired model from above:").lower()
                if model == "endeavour" or "1":
                    self.variant("endeavour")
                elif model == "ecosport" or "2":
                    self.variant("ecosport")
                else:
                    print("Please choose from the given models\n")
            
                
        elif brand == "Toyota":
            print("The available models are:\n 1.Fortuner\n2.Land Cruiser")
            
            while True:    
                model = input("Enter desired model from above:").lower()
                if model == "Fortuner" or "1":
                    self.variant("fortuner")
                if model == "land cruiser" or "2":
                    self.variant("land cruiser")
                else:
                    print("please choose from the above models")
        
        elif brand == "Hyundai":
            print("The available models are:\n 1.Creta\n2.Exter")
            while True:    
                model = input("Enter desired model from above:").lower()
                if model == "creta" or "1":
                    self.variant("creta")
                if model == "exter" or "2":
                    self.variant("exter")
                else:
                    print("please choose from the above models")
                    
    
    def variant(self,model):
        print()
        var = input("Enter variant:(Petrol/Diesel) :").lower()
        if var == "petrol":
            if model == "endeavour":
                self.price = 2900000
            elif model == "ecosport":
                self.price = 1100000
            elif model == "fortuner":
                self.price = 5100000
                
            elif model == "land cruiser":
                self.price = 21000000
                
            elif model == "creta":
                self.price = 1200000
            elif model == "exter":
                self.price = 1028000
            
            
        elif var == "diesel":
            if model == "endeavour":
                self.price = 3060000
            elif model == "ecosport":
                self.price = 1250000
            elif model == "fortuner":
                self.price = 526000               
            elif model == "land cruiser":
                self.price = 21020000
            elif model == "creta":
                self.price = 1350000
            elif model == "exter":
                self.price = 1188000
                
        self.total()
                
    def total(self):
        self.sgst = 0.18*self.price
        self.cgst = 0.18*self.price
        self.insurance = 100000
        self.total = self.price + self.sgst+self.cgst + self.insurance
        
        self.display()
        
    def display(self):
        print()
        print("".ljust(40,"="))
        print("Name".ljust(20),":",self.names[self.uname])
        print("Contact".ljust(20),":",self.contact[self.uname])
        print("SGST".ljust(20),":",self.sgst)
        print("CGST".ljust(20),":",self.cgst)
        print("Insurance".ljust(20),":",self.insurance)
        print("".ljust(20," "),"".ljust(20,"_"))
        print("Total".ljust(20),":",self.total)
        print("".ljust(40,"="))
        
        self.company()
        
            
        
obj = CarShowroom()
obj.company()
