# Progressive Electricity Billing

months = int(input("Number of months: "))
records = []

if months <= 0:
    print("Number of months must be positive.")
else:
    for i in range(months):
        month = input("\nMonth name: ").strip()
        units = float(input("Units consumed: "))

        while units < 0:
            units = float(input("Enter non-negative consumption: "))

        if units <= 100:
            energy = units * 1.50
        elif units <= 200:
            energy = 100 * 1.50 + (units - 100) * 2.50
        else:
            energy = 100 * 1.50 + 100 * 2.50 + (units - 200) * 4

        fixed = 100
        surcharge = 0
        rebate = 0

        if units > 300:
            surcharge = energy * 0.10

        if units <= 100:
            rebate = energy * 0.05

        bill = round(energy + fixed + surcharge - rebate, 2)
        records.append((month, units, bill))

        print("Energy charge: Rs.", format(energy, ".2f"))
        print("Fixed charge: Rs.", format(fixed, ".2f"))
        print("Surcharge: Rs.", format(surcharge, ".2f"))
        print("Rebate: Rs.", format(rebate, ".2f"))
        print("Final bill: Rs.", format(bill, ".2f"))

    total = 0
    highest = records[0]

    print("\nMONTHLY COMPARISON")

    for i in range(len(records)):
        month, units, bill = records[i]
        total += bill

        if bill > highest[2]:
            highest = records[i]

        print(month, "| Units:", units, "| Bill: Rs.", format(bill, ".2f"))

        if i > 0:
            previous_bill = records[i - 1][2]
            increase = (bill - previous_bill) / previous_bill * 100

            print("Change from previous month:", format(increase, ".2f"), "%")

            if increase > 25:
                print("Alert: unusual bill increase")

    print("\nTotal bills: Rs.", format(total, ".2f"))
    print("Average bill: Rs.", format(total / months, ".2f"))
    print("Highest bill month:", highest[0])