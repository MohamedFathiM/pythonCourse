# Function Scope

x = 1  # Global Scope

print(f"Print variable from global scope {x}")

def one():
    x = 2 # function scope
    print(f"Print variable from function scope {x}")

def two():
    global x # make variable global
    x = 4 # function scope
    print(f"Print variable from function scope {x}")





one()
two()

print(f"Print x after call two function which global x {x}")
