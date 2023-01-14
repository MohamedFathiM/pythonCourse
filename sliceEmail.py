
# mohamedfathi66@yahoo.com

theName = input("What is your name ? ").strip().capitalize()
theEmail = input("What is your email ? ").strip()
userName = theEmail[:theEmail.index("@")]
yourDomain = theEmail[theEmail.index("@") + 1:]

print(f"Hello {theName} Your Email Is {theEmail}")
print(f"Your user name is {userName} \nYour Website is {yourDomain}")
