myNumbers = [1, 2, 3, 4, 5, 6, 7, 13, 8, 9, 17, 18, 19]


# continue

for number in myNumbers:
    if number == 13:
        continue
    print(number)

print("=" * 20)


# break
for number in myNumbers:
    if number == 13:
        break
    print(number)

print("=" * 20)


# pass
for number in myNumbers:
    if number == 13:
        pass
    print(number)

print("=" * 20)
