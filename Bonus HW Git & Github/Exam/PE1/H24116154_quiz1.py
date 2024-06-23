# 輸入參數值
rsv=float(input("Please input a Richter scale value: "))


# calculate the energy in Joules
energy = 10**((1.5*rsv)+4.8)

# Equivalence in tons of TNT
TNT = energy/4.184e9

# Equivalence in the number of nutritious lunches
lunches = energy/2930200

# 輸出結果
print("Richter scale value: %f"%(rsv))
print("Equivalence in Joules: %f"%(energy))
print("Equivalence in tons of TNT: %f"%(TNT))
print("Equivalence in the number of nutritious lunches: %f"%(lunches))