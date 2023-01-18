tries = 4

mainPassword = "Mohamed"
inputPassword = input("Write Password ")

while inputPassword != mainPassword:
    tries -= 1
    print(f"Wrong Password , {'Last' if tries == 0 else tries} Chance left")
    if tries == 0:
        print("All Tries are finished")
        break
