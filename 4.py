x# Employee Payroll and Deduction Analysis

employees = int(input("Number of employees: "))

if employees <= 0:
    print("Number of employees must be positive.")
else:
    for i in range(employees):
        print("\nEmployee", i + 1)

        employee_id = input("Employee ID: ").strip()
        name = input("Employee name: ").strip()

        basic = float(input("Basic salary: "))
        overtime_hours = float(input("Overtime hours: "))
        incentive = float(input("Incentive: "))

        if (
            employee_id == "" or name == ""
            or basic < 0 or overtime_hours < 0 or incentive < 0
        ):
            print("Invalid employee details.")
            continue

        hra = basic * 0.20
        da = basic * 0.10
        overtime_pay = overtime_hours * 200

        gross = basic + hra + da + overtime_pay + incentive

        if gross <= 25000:
            progressive_deduction = 0
        elif gross <= 50000:
            progressive_deduction = (gross - 25000) * 0.05
        else:
            progressive_deduction = (
                25000 * 0.05 + (gross - 50000) * 0.10
            )

        provident_fund = basic * 0.12
        total_deductions = provident_fund + progressive_deduction
        net_salary = gross - total_deductions

        print("\n" + "=" * 42)
        print("SALARY STATEMENT")
        print("Employee:", employee_id, "-", name)
        print("-" * 42)

        entries = [
            ("Basic salary", basic),
            ("HRA", hra),
            ("DA", da),
            ("Overtime pay", overtime_pay),
            ("Incentive", incentive),
            ("Gross salary", gross),
            ("Provident fund", provident_fund),
            ("Progressive deduction", progressive_deduction),
            ("Total deductions", total_deductions),
            ("Net salary", net_salary)
        ]

        for label, amount in entries:
            print(label.ljust(26), format(amount, "12.2f"))

        print("=" * 42)