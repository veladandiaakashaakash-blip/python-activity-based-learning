# Multi-Currency Travel Budget Analysis

budget = float(input("Travel budget in INR: "))
currency_count = int(input("Number of foreign currencies: "))

currencies = [("INR", 1.0)]

if budget < 0 or currency_count < 0:
    print("Invalid budget or currency count.")
else:
    for i in range(currency_count):
        code = input("\nCurrency code: ").strip().upper()
        rate = float(input("INR value of one currency unit: "))

        duplicate = False
        for stored_code, stored_rate in currencies:
            if code == stored_code:
                duplicate = True

        while code == "" or rate <= 0 or duplicate:
            print("Invalid or duplicate currency.")
            code = input("Currency code: ").strip().upper()
            rate = float(input("INR value of one currency unit: "))

            duplicate = False
            for stored_code, stored_rate in currencies:
                if code == stored_code:
                    duplicate = True

        currencies.append((code, rate))

    expense_count = int(input("\nNumber of expenses: "))

    if expense_count <= 0:
        print("Number of expenses must be positive.")
    else:
        categories = []
        category_totals = []
        total_spending = 0

        for i in range(expense_count):
            print("\nExpense", i + 1)

            category = input("Category: ").strip().lower()
            amount = float(input("Amount in original currency: "))
            code = input("Currency code: ").strip().upper()
            fee_percent = float(input("Conversion fee percentage: "))

            rate = 0
            for stored_code, stored_rate in currencies:
                if code == stored_code:
                    rate = stored_rate

            while category == "" or amount < 0 or fee_percent < 0 or rate == 0:
                print("Invalid expense. Re-enter all details.")
                category = input("Category: ").strip().lower()
                amount = float(input("Amount in original currency: "))
                code = input("Currency code: ").strip().upper()
                fee_percent = float(input("Conversion fee percentage: "))

                rate = 0
                for stored_code, stored_rate in currencies:
                    if code == stored_code:
                        rate = stored_rate

            converted = amount * rate
            fee = converted * fee_percent / 100
            final_amount = round(converted + fee, 2)
            total_spending += final_amount

            print("Converted expense: Rs.", format(converted, ".2f"))
            print("Conversion fee: Rs.", format(fee, ".2f"))
            print("Total expense: Rs.", format(final_amount, ".2f"))

            position = -1
            for j in range(len(categories)):
                if categories[j] == category:
                    position = j

            if position == -1:
                categories.append(category)
                category_totals.append(final_amount)
            else:
                category_totals[position] += final_amount

        largest = 0

        print("\nCATEGORY TOTALS")
        for i in range(len(categories)):
            print(categories[i], ": Rs.", format(category_totals[i], ".2f"))

            if category_totals[i] > category_totals[largest]:
                largest = i

        print("\nTotal spending: Rs.", format(total_spending, ".2f"))

        if total_spending <= budget:
            print("Within budget.")
            print("Remaining: Rs.", format(budget - total_spending, ".2f"))
        else:
            print("Budget exceeded.")
            print("Overspending: Rs.", format(total_spending - budget, ".2f"))

        print("Largest expense category/categories:")
        for i in range(len(categories)):
            if category_totals[i] == category_totals[largest]:
                print("-", categories[i])