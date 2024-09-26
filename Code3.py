complex_num1 = 2+5j
complex_num2 = 1-4j
complex_sum = complex_num1 + complex_num2
complex_sub = complex_num1 - complex_num2
complex_mult = complex_num1 * complex_num1
complex_div = complex_num1 / complex_num2
print("Complex number 1:", complex_num1)
print("Complex number 2:", complex_num2)
print("The sum of complex numbers:", complex_sum)
print("The subtraction of complex numbers:", complex_sub)
print("The multiplication of complex numbers:", complex_mult)
print("The division of complex numbers:", complex_div)

real1 = complex_num1.real
imag1 = complex_num1.imag
print("\nReal part of number 1:", real1)
print("Imaginary part of number 1:", imag1)

magnit1 = (real1**2 + imag1**2)**0.5 
print("Magnitude of complex number 1:", magnit1)

real2 = complex_num2.real
imag2 = complex_num2.imag
print("\nReal part of number 2:", real2)
print("Imaginary part of number 2:", imag2)

magnit2 = (real2**2 + imag2**2)**0.5
print("Magnitude of complex number 2:", magnit2)