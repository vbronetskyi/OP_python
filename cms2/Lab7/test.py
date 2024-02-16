import re

country = "UUUUUUUUUUUUUUUUUUUUUUU"
id = "123450"
print(re.match(r'^[1-9]*0[1-9]*$', id))
