#Write a program to accept a number from the user and is the no is positive then find out the square.

cost_price=int(input("Enter cost price"))
sell_price=int(input("Enter selling  price"))

result=sell_price-cost_price

if(result==0):
    print("Neither profit Nor Loss")
elif(result>0):
    print("Profit ",result)
else:
    print("Loss ",-result)


