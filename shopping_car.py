items=["bread", "milk", "eggs", "chicken"]
print(items)
want_more=input("Do you want more?    ")
more=want_more.split(",")
items.extend(more)
want_remove=input("any thing for removing?   ")
while want_remove in items:
  items.remove(want_remove)
else :
 for index, item in enumerate(items, start= 1):
  print(f"{index}:  {item}")
