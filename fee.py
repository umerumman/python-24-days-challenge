print("Welcome to Student fee submition app")
student_data={"safia": {"fee":200},
              "eshal": {"fee":250},
              "toba": {"fee":300}
              }
#dictionary me sara data store hoga
total_fee=0 #fees ko collect krny k lye pehly 0 ka variable zrori hy wrna agy define na hony ka error ayega
remaining_fee=0 #hm ny nichy remaining fee print ki is lye loop sy pehly define krna zrori hy
remaning_student= list(student_data.keys()) #remaining student ko list me convert krny k lye, student name dictionary me keys hy usy call ki
while len(remaning_student) >0: #jb tk remaining student ki length 0 sy bzy hy tb tk loop chaly ga
   student_name=input("Enter student name?  ")
   name=student_name.strip().lower() #jo input sy lia hy usy lower case me convert krny k lye, aur strip k zriye agr koi dy dya to sy space remove krny k lye
   names=name .split(",") #zyada student k lye comma sy split krny k lye
   for name in names: #names me jitny b student hy unko loop me call krny k lye
     if name in remaning_student: #uper jo list hy usme check krny k lye k ye student rehta tha ya nhi,wrna pta na chale ga k student ne fee submit kr di ya nhi
       print(f"{name} 's fee is {student_data[name]["fee"]}")#student ki total fee ki yaddihani b ho gae
       paid_fee=int(input(f"Enter paid fee for {name}?  "))#ab poch rha hy k kitni di
       total_fee += paid_fee#jama krny k lye total fee me add krny k lye agr hm toatal pehly astimat kr lety to abb - lgaty
       if paid_fee == student_data[name]["fee"]:
         print("Complete fee submit")
         remaning_student.remove(name)
       elif paid_fee > student_data[name]["fee"]:
         extra_fee= paid_fee - student_data[name]["fee"]
         print(f"for {name} {extra_fee} rp submited for next month")
         remaning_student.remove(name)#ye is lye hy k jb student ki fee zyzda b  ho jaye to usy list me sy remove kr dy is mahiny k lye
       else:
         remaining_fee= student_data[name]["fee"] - paid_fee
         student_data[name]["fee"]= remaining_fee
         print(f"Remaining fee: {remaining_fee}" )

     else:
       print("Student is not found or already paid")#name mila fees poch kr upr ka if chala wrna ye keh dya

   print("remaining students:" ,remaning_student ,remaining_fee)
   print("total fee:",total_fee)
print("All students have submitted their fees.")

