age = int(input("what is your age ? ").strip())

months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print("Your lived For : ")
print(f"{months} Months .")
print(f"{weeks} Weeks .")
print(f"{days:,} Days .")
print(f"{minutes:,} Minutes .")
print(f"{seconds:,} Seconds .")
