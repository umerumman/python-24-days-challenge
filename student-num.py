<<<<<<< HEAD
students={"Faiqa": 45, "Rumman": 95, "Friha": 85}
total_marks=100

student=input("About which stuudent you want to see it's result?   ").title()
if student in students:
    marks=students[student]

    percentage=(marks/total_marks)*100
    print(marks)
    print(f"{percentage:.2f} %")
else:
   print("student not fouund")




=======
students={"Faiqa": 45, "Rumman": 95, "Friha": 85}
total_marks=100

student=input("About which stuudent you want to see it's result?   ").title()
if student in students:
    marks=students[student]

    percentage=(marks/total_marks)*100
    print(marks)
    print(percentage, "%")
else:
   print("student not fouund")




>>>>>>> 670a930ae5c53fbc9e6ed55df32a64dfe3fea920
