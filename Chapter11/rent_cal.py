rent = 55000*12
total = rent
print(f"year  Rent/year  Total_Rent_till_now")
for i in range (1,31):
    print(f"{i}     {round(rent)}    {round(total)}") # round(value, 2) or total:.2f
    rent = rent*1.05
    total += rent
    