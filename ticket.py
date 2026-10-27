print("Welcome to Gaming Zone")
print("------------------------")
name=input("Enter your Name?  ")
age=int(input("Enter your Age?  "))
if age<=6:
  price=  0
elif age<=18:
  price= 200
else:
   price= 500
member_ship=input("Are you member? (yes/no)  ")
if member_ship == "yes":
     print("your ticket price" , price*0.90)
else:
    print("your ticket price", price)