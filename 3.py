# Hospital Billing and Patient Classification

patients = int(input("Number of patients: "))

if patients <= 0:
    print("Number of patients must be positive.")
else:
    for i in range(patients):
        print("\nPatient", i + 1)

        name = input("Patient name: ").strip()
        age = int(input("Age: "))
        income = float(input("Annual family income: "))

        consultation = float(input("Consultation charge: "))
        diagnostics = float(input("Diagnostic charge: "))
        treatment = float(input("Treatment charge: "))

        if (
            name == "" or age < 0 or income < 0
            or consultation < 0 or diagnostics < 0 or treatment < 0
        ):
            print("Invalid patient details or negative charges.")
            continue

        concession_rate = 0

        if age >= 60:
            concession_rate = 0.10

        if income <= 200000:
            concession_rate = 0.15

        gross = consultation + diagnostics + treatment
        concession = (consultation + treatment) * concession_rate
        final_bill = round(gross - concession, 2)

        print("\nGross bill: Rs.", format(gross, ".2f"))
        print("Concession: Rs.", format(concession, ".2f"))
        print("Final bill: Rs.", format(final_bill, ".2f"))

        paid = float(input("Amount paid: "))

        while paid < 0 or paid > final_bill:
            paid = float(input("Enter payment between 0 and final bill: "))

        balance = round(final_bill - paid, 2)

        if balance == 0:
            category = "Fully paid"
        elif paid == 0:
            category = "Unpaid"
        else:
            category = "Partially paid"

        print("\nPATIENT BILL")
        print("Name:", name)
        print("Payment classification:", category)
        print("Paid: Rs.", format(paid, ".2f"))
        print("Outstanding: Rs.", format(balance, ".2f"))