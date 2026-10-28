# Campus Event Financial Planning

venue = float(input("Venue cost: "))
equipment = float(input("Equipment cost: "))
transport = float(input("Transport cost: "))

catering_per_person = float(input("Catering cost per participant: "))
certificate_per_person = float(input("Certificate cost per participant: "))

participants = int(input("Expected participant count: "))
registration_fee = float(input("Registration fee per participant: "))
sponsorship = float(input("Confirmed sponsorship amount: "))

if (
    venue < 0 or equipment < 0 or transport < 0
    or catering_per_person < 0 or certificate_per_person < 0
    or participants < 0 or registration_fee < 0 or sponsorship < 0
):
    print("Costs, counts, fees, and sponsorship cannot be negative.")
else:
    fixed_cost = venue + equipment + transport
    variable_cost_per_person = (
        catering_per_person + certificate_per_person
    )

    variable_cost = participants * variable_cost_per_person
    total_cost = fixed_cost + variable_cost

    registration_revenue = participants * registration_fee
    total_funds = registration_revenue + sponsorship
    balance = total_funds - total_cost

    print("\nEVENT FINANCIAL REPORT")
    print("Fixed costs: Rs.", format(fixed_cost, ".2f"))
    print("Variable costs: Rs.", format(variable_cost, ".2f"))
    print("Total event cost: Rs.", format(total_cost, ".2f"))
    print("Registration revenue: Rs.", format(registration_revenue, ".2f"))
    print("Confirmed sponsorship: Rs.", format(sponsorship, ".2f"))

    if balance >= 0:
        print("Expected surplus: Rs.", format(balance, ".2f"))
        print("Additional sponsorship required: Rs. 0.00")
    else:
        print("Expected deficit: Rs.", format(-balance, ".2f"))
        print("Additional sponsorship required: Rs.", format(-balance, ".2f"))

    amount_to_recover = total_cost - sponsorship

    if amount_to_recover < 0:
        amount_to_recover = 0

    if participants > 0:
        # Round upward to the next paisa, not to the nearest paisa.
        raw_paise = amount_to_recover / participants * 100
        required_paise = int(raw_paise)

        if raw_paise - required_paise > 0.0000001:
            required_paise += 1

        required_contribution = required_paise / 100

        print(
            "Required contribution per participant: Rs.",
            format(required_contribution, ".2f")
        )
    else:
        print("Per-participant contribution cannot be calculated for zero participants.")

    contribution_margin = registration_fee - variable_cost_per_person
    uncovered_fixed_cost = fixed_cost - sponsorship

    if uncovered_fixed_cost <= 0:
        print("Minimum registrations needed to cover fixed costs: 0")

        if contribution_margin < 0:
            print(
                "Warning: each registration adds more variable cost than revenue."
            )
            print(
                "A larger participant count can therefore create a deficit."
            )

    elif contribution_margin <= 0:
        print("Break-even is impossible with the current fee and sponsorship.")
        print("Increase the registration fee, reduce costs, or obtain sponsorship.")

    else:
        raw_count = uncovered_fixed_cost / contribution_margin
        minimum_registrations = int(raw_count)

        if raw_count - minimum_registrations > 0.0000001:
            minimum_registrations += 1

        print(
            "Minimum registrations needed to break even:",
            minimum_registrations
        )

        if participants >= minimum_registrations:
            print("Expected registrations meet the break-even requirement.")
        else:
            print(
                "Additional registrations needed:",
                minimum_registrations - participants
            )