print("Welcome to the tip calculator!")


total_bill = input("What was the total bill? $")
perc_tip = input("How much would you like to give? 10, 12 or 15? ")
num_people = input("How many people to split the bill?")


total = round((float(total_bill) * (int(perc_tip)/100) + float(total_bill)) / float(num_people), 2)

print(f"Each person should pay: ${total}")
