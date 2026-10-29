
def calculate_bill(units):
    if units <= 100:
        charge = units * 2
    elif units <= 200:
        charge = 100 * 2 + (units - 100) * 3
    else:
        charge = 100 * 2 + 100 * 3 + (units - 200) * 5

    fixed = 50
    surcharge = charge * 0.05
    rebate = 20 if units < 100 else 0

    total = charge + fixed + surcharge - rebate
    return total


bills = []

for month in range(1, 4):
    units = int(input("Enter units for month " + str(month) + ": "))
    bill = calculate_bill(units)
    bills.append(bill)
    print("Month", month, "Bill: Rs.", round(bill, 2))

for i in range(1, 3):
    increase = (bills[i] - bills[i - 1]) / bills[i - 1] * 100

    if increase > 20:
        print("Month", i + 1, ": Unusual increase")
    else:
        print("Month", i + 1, ": Normal increase")

