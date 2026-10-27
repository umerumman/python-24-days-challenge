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




