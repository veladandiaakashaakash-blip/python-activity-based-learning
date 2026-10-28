# University Scholarship Allocation

eligible = []
used_ids = []

count = int(input("Number of applicants: "))
quota = int(input("Number of scholarships available: "))

if count <= 0 or quota < 0:
    print("Invalid applicant count or scholarship quota.")
else:
    for i in range(count):
        print("\nApplicant", i + 1)

        student_id = input("Registration ID: ").strip()
        name = input("Name: ").strip()

        marks = []
        for subject in range(3):
            mark = float(input("Subject " + str(subject + 1) + " marks: "))
            marks.append(mark)

        attendance = float(input("Attendance percentage: "))
        income = float(input("Annual family income: "))

        reasons = []

        if student_id == "" or student_id in used_ids:
            reasons.append("Missing or duplicate registration ID")
        else:
            used_ids.append(student_id)

        if name == "":
            reasons.append("Name cannot be empty")

        valid_marks = True
        for mark in marks:
            if mark < 0 or mark > 100:
                valid_marks = False

        if not valid_marks:
            reasons.append("Marks must be between 0 and 100")
        else:
            aggregate = (marks[0] + marks[1] + marks[2]) / 3

            if aggregate < 75:
                reasons.append("Aggregate below 75%")

            for j in range(3):
                if marks[j] < 60:
                    reasons.append("Subject " + str(j + 1) + " below 60")

        if attendance < 0 or attendance > 100:
            reasons.append("Invalid attendance")
        elif attendance < 80:
            reasons.append("Attendance below 80%")

        if income < 0:
            reasons.append("Invalid income")
        elif income > 300000:
            reasons.append("Income exceeds limit")

        if len(reasons) == 0:
            # Smaller tuple values rank first.
            record = (
                -aggregate, -attendance, income,
                student_id, name
            )
            eligible.append(record)
            print("Eligible")
        else:
            print("Not eligible:")
            for reason in reasons:
                print("-", reason)

    # Manual sorting using tuple comparison.
    for i in range(len(eligible)):
        for j in range(i + 1, len(eligible)):
            if eligible[j] < eligible[i]:
                eligible[i], eligible[j] = eligible[j], eligible[i]

    print("\nSCHOLARSHIP RANKING")
    print("Rank | ID | Name | Aggregate | Status")

    for i in range(len(eligible)):
        negative_average, negative_attendance, income, sid, name = eligible[i]

        if i < quota:
            status = "Selected"
        else:
            status = "Waiting list"

        print(
            i + 1, "|", sid, "|", name, "|",
            format(-negative_average, ".2f"), "|", status
        )

    if len(eligible) == 0:
        print("No eligible applicants.")