# Problem with Decimal Numbers (floating points) in Python:

print(0.1 + 0.2 == 0.3) # false

# because in python, 0.1 + 0.2 = 0.30000000004 due to conversion of 0.1 and 0.2 into binary bits for calculation
# therefore, 0.1 + 0.2 == 0.3 is false

# Solution: use decimal library of python

import decimal
from decimal import Decimal

x = 0.1
y = 0.2
a = Decimal('0.1')
b = Decimal('0.2')

print(x+y)
print(a + b)