# Numbers Datatype:

a = 18
b = 18.5
c = 3+5j

print(a)
print(type(a))
print(type(b))
print(type(c))

print(type(a)) # integer
print(isinstance(c, complex)) #true

# binary
binary = 0b101
# octal
octal = 0o16
# hexadecimal
hex = 0x723F6A

print("Output of 0b101: ", binary)
print("Output of 0o16: ", octal)
print("Output of 0x723F6A: ", hex)

# Type Coersions in Python:

var_a = 5
var_b = 5.5

print(var_a + var_b)

# Decimal Numbers (floating points) in Python:

print(0.1 + 0.2 == 0.3) # 0.30000000004

# Type Coersion (implicit Conversion of DataType):

ans = 0x15F2A + 0b1001

print(ans)
print(type(ans))

# Explicit DataType Conversion

print(int(5.2))
print(float(5))

# complex numbers: direct conversion is not possible

comp = 2+3j
r = print("Real Part: ", comp.real)
i = print("Imaginary Part: ", comp.imag)

# List in Python

list = ['a', 3685, 'c', 0xF542]

# Accessing Elements (index)

print(list[3])

# Addition in List

list.append(10)

print(list)

# Remove elements in List

list.pop()

print(list)

# Negative Indexes in List

print(list[-1])