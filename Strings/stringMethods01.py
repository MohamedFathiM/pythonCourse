# -----------------------
# -- Strings Methods
# -----------------------

# strip() rstrip() lstrip()

a = "  I Love Python   "
print(a.strip())
print(a.lstrip())
print(a.rstrip())


b = "#@#@#@I Love Python#@##"
print(b.strip('@#'))
print(b.lstrip('@#'))
print(b.rstrip('@#'))

# title() , capitalize()
c = "I Love Python 3th"
print(c.title())
print(c.capitalize())

# zfill (zero fill)
a , b , c , d = "1", "12", "6525", "2"
print(a.zfill(4))
print(b.zfill(4))
print(c.zfill(4))
print(d.zfill(4))

# upper() , lower()
print("ahmed".upper())
print("AHMED".lower())
