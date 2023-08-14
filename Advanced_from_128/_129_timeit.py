# timeit
# test performance of your code
# timeit(statement,setup before statement , timer ,number of execution code)

import timeit
import random
# print(dir(timeit))

# print(timeit.timeit("'Mohamed' * 2000"))
# print("mohamed" * 2000)


# when using external module
print(random.randint(1,1500))

# using timeit on it
print(timeit.timeit(stmt='random.randint(1,1500)',setup='import random'))

print(timeit.repeat(stmt='"mohamed" * 100',repeat=4))
