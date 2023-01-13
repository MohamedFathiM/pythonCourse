# difference()

a = {1, 2, 3, 4}
b = {1, 2, "Mohamed", "Fathi"}

print(a)
print(a.difference(b))  # a - b
print(b-a)
print("=" * 40)

# difference_update()
c = {1, 2, 3, 4}
d = {1, 2, 3, "Mohamed", "Ahmed"}
print(c)
c.difference_update(d)
print(c)
print("=" * 40)

# intersection()
e = {1, 2, 3, 4}
f = {1, 2, 3, "Mohamed", "Ahmed"}
print(e)
print(e.intersection(f))  # e & f
print(e)
print("=" * 40)

# intersection_update()
g = {1, 2, 3, 4}
h = {1, 2, 3, "Mohamed", "Ahmed"}
print(g)
g.intersection_update(h)
print(g)
print("=" * 40)


# symmetric_difference() // بيطلع العناصر الي مش موجودة في الاتنين او واحده من الاتنين
i = {1, 2, 3, 4, 5, "x"}
j = {"Mohamed", "Zero", 1, 2, 4}
print(i)
print(i.symmetric_difference(j))  # i ^ j
print(i)
print("=" * 40)

# symmetric_difference() // بيطلع العناصر الي مش موجودة في الاتنين او واحده من الاتنين و كمان بيعمل تعديل للاصلية
k = {1, 2, 3, 4, 5, "x"}
l = {"Mohamed", "Zero", 1, 2, 4}
print(k)
k.symmetric_difference_update(l)
print(k)
