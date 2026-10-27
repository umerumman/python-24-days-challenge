persons=4
total_bill=0
order_food={"biryani": 100, "pizza": 200, "salad": 50, "raita": 50}
total_bill = sum(order_food.values())
tip= total_bill * 0.10
print("Tip amount:" ,tip)
print("Total bill without tip:" ,total_bill)
total_with_tip = total_bill + tip
print("Total bill_with tip:" ,total_with_tip)
print("Bill per person:" ,total_with_tip/persons)
    





