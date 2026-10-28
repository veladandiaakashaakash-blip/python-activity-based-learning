# Manufacturing Cost and Profitability Analysis

units = int(input("Number of units to produce: "))
material_count = int(input("Number of raw materials: "))

if units <= 0 or material_count <= 0:
    print("Units and material count must be positive.")
else:
    net_material_cost = 0

    for i in range(material_count):
        print("\nRaw material", i + 1)

        name = input("Material name: ").strip()
        quantity_per_unit = float(input("Quantity per finished unit: "))
        rate = float(input("Cost per material unit: "))

        while quantity_per_unit < 0 or rate < 0:
            print("Quantity and rate cannot be negative.")
            quantity_per_unit = float(input("Quantity per finished unit: "))
            rate = float(input("Cost per material unit: "))

        material_cost = quantity_per_unit * rate * units
        net_material_cost += material_cost

        print(name, "cost: Rs.", format(material_cost, ".2f"))

    wastage_percent = float(input("\nExtra material wastage percentage: "))
    labour_hours = float(input("Total labour hours: "))
    labour_rate = float(input("Labour cost per hour: "))
    machine_hours = float(input("Total machine hours: "))
    machine_rate = float(input("Machine cost per hour: "))
    overhead = float(input("Other batch overheads: "))
    selling_price = float(input("Selling price per finished unit: "))
    target_percent = float(input("Target profit percentage on cost: "))

    if (
        wastage_percent < 0 or labour_hours < 0 or labour_rate < 0
        or machine_hours < 0 or machine_rate < 0 or overhead < 0
        or selling_price < 0 or target_percent < 0
    ):
        print("Costs, hours, and percentages cannot be negative.")
    else:
        wastage_cost = net_material_cost * wastage_percent / 100
        labour_cost = labour_hours * labour_rate
        machine_cost = machine_hours * machine_rate

        total_cost = (
            net_material_cost + wastage_cost
            + labour_cost + machine_cost + overhead
        )

        revenue = units * selling_price
        profit = revenue - total_cost
        target_profit = total_cost * target_percent / 100
        required_price = (total_cost + target_profit) / units

        print("\nPRODUCTION REPORT")

        entries = [
            ("Net material cost", net_material_cost),
            ("Wastage cost", wastage_cost),
            ("Labour cost", labour_cost),
            ("Machine cost", machine_cost),
            ("Other overheads", overhead),
            ("Total production cost", total_cost),
            ("Cost per unit", total_cost / units),
            ("Sales revenue", revenue),
            ("Profit / loss", profit),
            ("Target profit", target_profit),
            ("Required selling price/unit", required_price)
        ]

        for label, amount in entries:
            print(label.ljust(30), format(amount, "12.2f"))

        if total_cost > 0:
            profit_percent = profit / total_cost * 100
            print("Actual profit on cost:", format(profit_percent, ".2f"), "%")
        else:
            print("Profit percentage is undefined because cost is zero.")

        if profit >= target_profit:
            print("Result: profit target achieved.")
        else:
            print("Result: profit target not achieved.")