actual_cost=float(input("enter actual price:"))
sale_amount=float(input("enter sale value:"))

if sale_amount > actual_cost :
    amount = sale_amount - actual_cost
    print(f"total profit={amount}")
else:
    print("no profit")