# in
# not in

# string
name = "Mohamed"
print("s" in name)
print("a" in name)
print("A" in name)

print("#" * 40)

friends = ["Ahmed", "Sayed", "Mahmoud"]

print("Mohamed" in friends)
print("Mohamed" not in friends)


countries = ["Egypt", "KSA", "Kuwait"]
discount = 80
myCountry = "Egypt"

if myCountry in countries:
    print(f"Your Discount is {discount}")
else:
    print(f"Hello, your discount is equal to 50")
