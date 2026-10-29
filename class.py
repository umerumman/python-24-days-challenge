class cat:
    def __init__ (self, name, color):
        self.name=name
        self.color=color
    def meow (self):
        print(self.name, "says meow!")
c1=cat ("whiskers","orange")
c1. meow()

class dog:
    def __init__ (self,name,color):
        self.name=name
        self.color=color
    def bark(self):
        print(self.name, "says bark!")
d1= dog("tom","brown")
d1. bark()

class car:
    def __init__ (self,make,model):
        self.make=make
        self.model=model
    def start(self):
        print(self.make, self.model, "is starting!")
c1=car("toyota","camry")
c1.start()

class book:
    def __init__ (self, title, author):
        self.title=title
        self.author=author
    def read(self):
        print("reading" , self.title , "by" , self.author)
b1=book("The Hobbit", "J.R.R. Tolkien")
b1.read()


    

class bankaccount:
     def __init__ (self, owner, balance):
       self.owner=owner
       self.balance=balance
     def deposit(self, amount):
       self.balance +=amount
       print(self.owner,"New balance is" , self.balance)
account_number= input('enter account number:  ')
amount=int(input("enter amount to deposit:   "))

c1=bankaccount("Ali",100)
c2=bankaccount("Sara",200)
account_number.deposit(amount)


  