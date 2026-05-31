import random
import string

pass_len = 8
charValues = string.ascii_letters + string.digits + string.punctuation

# List comprehension [function for i in range(n)]

res = "".join([random.choice(charValues) for i in range(pass_len)])
print(res)