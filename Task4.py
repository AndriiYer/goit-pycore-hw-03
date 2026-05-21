from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list) -> list:
    today = datetime.today().date()
    upcoming = []

    for user in users:
        # Parsing the birthday string
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Birthday this year
        birthday_this_year = birthday.replace(year=today.year)

        # If it has already passed, we postpone it to next year.
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Difference in days
        delta_days = (birthday_this_year - today).days

        # If the birthday is within 7 days inclusive
        if 0 <= delta_days <= 7:
            congratulation_date = birthday_this_year

            # If it falls on a weekend, we postpone it to Monday.
            if congratulation_date.weekday() >= 5:  # 5 = субота, 6 = неділя
                congratulation_date += timedelta(days=(7 - congratulation_date.weekday()))

            # Add to the result
            upcoming.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming

users = [
    {"name": "John Doe", "birthday": "1985.05.23"},
    {"name": "Jane Smith", "birthday": "1990.05.25"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)