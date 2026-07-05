bill_amt = float(input("What was the total bill amount?"))
tip=int(input("How much tip you want to give? 10,12 or 15 "))
split = int(input("How many people to split the bill?"))

tip_amount = bill_amt * (tip)/100
split_amount = round((bill_amt + tip_amount)/split,2)

print(f"Amount to pay each person is {split_amount}")