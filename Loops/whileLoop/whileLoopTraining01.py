myFavoriteWebs = []

maximumWebs = 5

while maximumWebs > 0:
    web = input("Add new Website  ").strip().lower()
    myFavoriteWebs.append(f"https://{web}")
    maximumWebs -= 1
    print(f"website Added , {maximumWebs } places Left")
    print(myFavoriteWebs)
else:
    print("Bookmark is Full")

index = 0
if (len(myFavoriteWebs) > 0):
    print("print Websites : ")
    while (index < len(myFavoriteWebs)):
        print(myFavoriteWebs[index])
        index += 1
