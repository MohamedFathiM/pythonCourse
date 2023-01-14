age = int(input("what is your age ? ").strip())
unit = input("Please Choose time unit : Months , weeks , Days ").strip().lower()

months = age * 12
weeks = months * 4
days = age * 365


if unit == "months" or unit == "m":
    print((f"You Lived For {months:,} Months."))
elif unit == "weeks" or unit == "w":
    print((f"You Lived For {weeks:,} Weeks."))
else:
    print((f"You Lived For {days:,} Days."))
