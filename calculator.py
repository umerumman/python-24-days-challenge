num1=int(input("enter a nmber   "))
num2=int(input("enter a second number   "))
def calculate(num1, num2):
    return num1 + num2 
return_result= calculate(num1, num2)
multiply= return_result * 2
print(return_result)
print(multiply)
more=input("do you want more?  choose ....")

if more == "+":
    new_num=int(input("new number?   "))
    print(multiply + new_num)
elif more == "-":
    new_num=int(input("new number?   "))
    print(multiply - new_num)
elif more == "*":
    new_num=int(input("new number?   "))
    print(multiply * new_num)
elif more == "/":
    new_num=int(input("new number?   "))
    print(multiply / new_num)
else:
    print("god bye")


