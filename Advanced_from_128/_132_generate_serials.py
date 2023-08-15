import string,random


# print(string.digits)
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)

def make_serial(count):
    all_chars = string.ascii_letters + string.digits
    count_of_all_chars = len(all_chars)

    collect_chars = []
    while count > 0 :
        random_number = random.randint(0,count_of_all_chars -1)
        random_char = all_chars[random_number]
        collect_chars.append(random_char)
        count -= 1

    return "".join(collect_chars)


print(make_serial(5))
