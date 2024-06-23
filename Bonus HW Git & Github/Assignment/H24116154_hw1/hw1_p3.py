# 輸入所需參數
v=float(input("Input velocity: "))

c=299792458 # The light of speed

# 輸出 Percentage of light speed
percentage=v/c
print("Percentage of light speed = %f"%(percentage))

# Calculate the factor 
factor=1/((1-(percentage**2)))**0.5

# By Einstein’s equation to calculate the travel time to the location
delta_td=[4.3,6.0,309,2000000]
location=["Alpha Centauri","Barnard's Star",
          "Betelgeuse (in the Milky Way)","Andromeda Galaxy (closest galaxy)"]

i = 0 # initialization
while i < len(delta_td):
    delta_tp=float(delta_td[i])/factor
    print("Travel time to %s = %f"%(location[i],delta_tp))
    i+=1


