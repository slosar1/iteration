import random

a = random
b = random
uniform = (a, b)
secret = random.uniform(a,b)
a, b = b, a % b
print(a)
