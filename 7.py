# Retail Billing with Multiple Discount Rules

count = int(input("Number of products: "))
items = []
subtotal = 0

if count <= 0:
    print("Number of products must be positive.")
else:
    for i in range(count):
        print("\nProduct", i + 1)

        name = input("Product name: ").strip()
        category = input(
            "Category (food/clothing/electronics): "
        ).strip().lower()

        price = float(input("Unit price: "))
        quantity = int(input("Quantity: "))

        while (
            name == ""
            or category not in ["food", "clothing", "electronics"]
            or price < 0 or quantity <= 0
        ):
            print("Invalid product. Enter all details again.")
            name = input("Product name: ").strip()
            category = input(
                "Category (food/clothing/electronics): "
            ).strip().lower()
            price = float(input("Unit price: "))
            quantity = int(input("Quantity: "))

        amount = price * quantity
        subtotal += amount
        items.append((name, category, price, quantity, amount))

    if subtotal >= 5000:
        discount = subtotal * 0.10
    elif subtotal >= 2000:
        discount = subtotal * 0.05
    else:
        discount = 0

    if discount > 800:
        discount = 800

    total_tax = 0
    grand_total = 0

    print("\nITEMIZED INVOICE")
    print(
        "Product".ljust(18),
        "Qty".rjust(5),
        "Gross".rjust(10),
        "Discount".rjust(10),
        "Tax".rjust(10),
        "Total".rjust(10)
    )

    for name, category, price, quantity, amount in items:
        if subtotal > 0:
            item_discount = amount / subtotal * discount
        else:
            item_discount = 0

        taxable_amount = amount - item_discount

        if category == "food":
            tax_rate = 0
        elif category == "clothing":
            tax_rate = 0.05
        else:
            tax_rate = 0.18

        tax = taxable_amount * tax_rate
        item_total = taxable_amount + tax

        total_tax += tax
        grand_total += item_total

        print(
            name[:18].ljust(18),
            str(quantity).rjust(5),
            format(amount, "10.2f"),
            format(item_discount, "10.2f"),
            format(tax, "10.2f"),
            format(item_total, "10.2f")
        )

    print("\nSubtotal: Rs.", format(subtotal, ".2f"))
    print("Discount: Rs.", format(discount, ".2f"))
    print("Total tax: Rs.", format(total_tax, ".2f"))
    print("Grand total: Rs.", format(grand_total, ".2f"))