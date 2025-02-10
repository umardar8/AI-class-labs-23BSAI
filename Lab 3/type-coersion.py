# Type Coersions means implicit (automatic) conversion of datatype

var_a = 5 # int
var_b = 5.5 # float

print(var_a + var_b) # result is given in float

# Implicit Cooersion of DataType:

ans = 0x15F2A + 0b1001 # addition of hexadecimal and binary number

print(ans)
print(type(ans)) # result is in int

# Explicit Coersion of Datatype:

print(int(5.2)) # float to int
print(float(5)) # int to float

# Coersion of complex numbers: direct conversion from complex to int is not possible due to imaginary part 
# however, real or imaginary part can be extracted separately

comp = 2+3j
r = print("Real Part: ", comp.real)
i = print("Imaginary Part: ", comp.imag)