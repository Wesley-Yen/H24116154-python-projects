h=float(input("Input the height of the 1st ball: "))
m1=float(input("Input the mass of the 1st ball: "))
m2=float(input("Input the mass of the 2nd ball: "))

g=9.8 # The acceleration

# To calculate the amount of Potential Energy of m1
U1=m1*g*h

# 滑落至底部時,位能全部轉為m1動能(設不計阻力)
Ek=U1
# To calculate the velocity of the 1st ball
v1=((2*Ek)/m1)**0.5
print("The velocity of the 1st ball after slide: %f m/s"%(v1))

# when the elastic collision occurs,the total amount of kinetic energy remains unchanged.
# 設2顆球碰撞後1st球將動能盡數傳遞給2nd球,而1st球在碰撞後靜止 i.e. Ek=1/2*(m2)*(v**2)
v=(Ek*2/(m2))**0.5
print("The velocity of the 2nd ball after collision: %f m/s"%(v))