# Railway Fare and Reservation Calculator

distance = float(input("Journey distance in km: "))
travel_class = input("Class (sleeper/ac/first): ").strip().lower()
passengers = int(input("Number of passengers: "))

if (
    distance <= 0 or passengers <= 0
    or travel_class not in ["sleeper", "ac", "first"]
):
    print("Invalid journey details.")
else:
    if distance <= 100:
        distance_fare = distance
    elif distance <= 500:
        distance_fare = 100 + (distance - 100) * 0.80
    else:
        distance_fare = 100 + 400 * 0.80 + (distance - 500) * 0.60

    if travel_class == "sleeper":
        multiplier = 1
    elif travel_class == "ac":
        multiplier = 2
    else:
        multiplier = 3

    total_booking = 0
    total_refund = 0

    for i in range(passengers):
        print("\nPassenger", i + 1)
        name = input("Name: ").strip()
        age = int(input("Age: "))

        while age < 0:
            age = int(input("Enter a non-negative age: "))

        if age < 5:
            concession_rate = 1
        elif age < 12:
            concession_rate = 0.50
        elif age >= 60:
            concession_rate = 0.40
        else:
            concession_rate = 0

        base_fare = distance_fare * multiplier
        concession = base_fare * concession_rate
        travel_fare = round(base_fare - concession, 2)
        reservation_fee = 40
        ticket_total = travel_fare + reservation_fee

        print("Travel fare: Rs.", format(travel_fare, ".2f"))
        print("Reservation fee: Rs.", format(reservation_fee, ".2f"))
        print("Ticket total: Rs.", format(ticket_total, ".2f"))

        total_booking += ticket_total

        cancel = input("Cancel this ticket? (yes/no): ").strip().lower()

        while cancel not in ["yes", "no"]:
            cancel = input("Enter yes or no: ").strip().lower()

        if cancel == "yes":
            hours = float(input("Hours remaining before departure: "))

            while hours < 0:
                hours = float(input("Enter non-negative hours: "))

            if hours >= 48:
                penalty_rate = 0.10
            elif hours >= 24:
                penalty_rate = 0.25
            else:
                penalty_rate = 0.50

            penalty = round(travel_fare * penalty_rate, 2)
            refund = round(travel_fare - penalty, 2)
            total_refund += refund

            print("Cancellation penalty: Rs.", format(penalty, ".2f"))
            print("Refund: Rs.", format(refund, ".2f"))

    print("\nOriginal booking total: Rs.", format(total_booking, ".2f"))
    print("Total refund: Rs.", format(total_refund, ".2f"))
    print(
        "Net amount after refunds: Rs.",
        format(total_booking - total_refund, ".2f")
    )