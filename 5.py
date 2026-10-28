# Multi-Plan Telecommunications Cost Optimization

# name, price, validity days, included minutes, included GB,
# extra-minute rate, extra-GB rate
plans = [
    ("Basic", 199, 28, 200, 2, 0.50, 30),
    ("Standard", 399, 28, 600, 10, 0.40, 25),
    ("Premium", 699, 56, 1500, 30, 0.30, 20),
    ("LongValid", 999, 84, 2000, 45, 0.25, 18)
]

minutes = float(input("Total required call minutes: "))
data = float(input("Total required data in GB: "))
required_days = int(input("Required validity in days: "))
budget = float(input("Maximum budget: "))

if minutes < 0 or data < 0 or required_days <= 0 or budget < 0:
    print("Invalid usage, validity, or budget.")
else:
    best_name = ""
    best_cost = 0

    print("\nPLAN COMPARISON")

    for plan in plans:
        name, price, validity, free_minutes, free_data, minute_rate, data_rate = plan

        extra_minutes = minutes - free_minutes
        extra_data = data - free_data

        if extra_minutes < 0:
            extra_minutes = 0

        if extra_data < 0:
            extra_data = 0

        excess_charge = (
            extra_minutes * minute_rate + extra_data * data_rate
        )
        total_cost = round(price + excess_charge, 2)

        print("\nPlan:", name)
        print("Validity:", validity, "days")
        print("Excess charges: Rs.", format(excess_charge, ".2f"))
        print("Total cost: Rs.", format(total_cost, ".2f"))

        if validity < required_days:
            print("Not eligible: insufficient validity")
        elif total_cost > budget:
            print("Not eligible: exceeds budget")
        else:
            print("Eligible")

            if best_name == "" or total_cost < best_cost:
                best_name = name
                best_cost = total_cost

    if best_name == "":
        print("\nNo plan satisfies all constraints.")
    else:
        print("\nMost economical eligible plan:", best_name)
        print("Cost: Rs.", format(best_cost, ".2f"))