# 輸入所需參數
F=float(input("Input the force: "))
m1=float(input("Input the mass of m1: "))
r=float(input("Input the distance: "))

c=299792458 #  The speed of light (constant)
G=6.67e-11 # The gravitational constant

# By Newton’s law of universal gravitation to calculate the mass of m2
m2=(F*(r**2))/(G*m1)
print("The mass of m2 = %f"%(m2))

# By Mass-energy equivalence to calculate the energy of m2
E=m2*(c**2)
print("The energy of m2 = %f"%(E))

