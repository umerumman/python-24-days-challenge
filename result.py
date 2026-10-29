def result(Name, Section, Tech, Language, UI):# ye function ka naam hai result aur ye 5 parameters le raha hai Name, Section, Tech, Language, UI
    print("_" * 10) #line bnwai ta k desry student ka result alag se show ho
    print("Welcome to the result portal")
    print("_" * 36) #line bnai ta k result ka heading alag se show ho
    total_marks= 300
    obtained_marks= Tech+Language+UI #upr waly 3 parameters ka sum kiya gya ta k total marks ka pata chal sake
    percentage= obtained_marks/total_marks * 100 #upr waly 3 parameters ka percentage nikala gya ta k grade ka pata chal sake
    if percentage > 90:
        Grade= 'A+'#wesy hm print krty hain lekin hm ne yahan variable bnaya ta k grade ka akhir me program khod btaey
    elif percentage > 40:
        Grade= "Pass"
    else:
        Grade= "Fail, You need to improve your performance"
    #ab yhan sy output print hoga
    print("Student name:", Name)
    print("Section:", Section)
    print("_" *36)
    print("subject    |    Marks")
    print("Tech       |    ", Tech) #space aur | wgera sb comma k andr hun gy, brabr krny k lye itna space diya gya
    print("Language   |    ", Language)
    print("UI         |    ", UI)
    print("_" *36)
    print("Total Marks:", total_marks)
    print("Obtained Marks:", obtained_marks)
    print(f"Percentage: {percentage:.2f}%") #2f ka matlab hai k percentage ka result 2 decimal points tk show hoga or ye f string ka use kr k kiya gya
    print("Grade:", Grade)
#ab jin jin ka result show krna hai unka naam, section aur marks yahan pass krny hain , hr comma k bad wala value bn jaey gi uper waly parameters ka, faida ye hwa k sb k lye alg sy code likh kr nhi krna pary ga, sb ka result show ho jy ga
result("Ali", "A", 45.5, 55.0, 60.5)
result("Rumman", "A", 85.5, 92.0, 78.5)
result("Ahmed", "A", 25.5, 35.0, 40.5)


