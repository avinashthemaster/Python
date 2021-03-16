h=10
r=5
f=10
t=int(input("100"))
vtank = 3.14*r**2*h
vwtr = f*t
if wtr > vtank:
    print("Overflow")
    print("volume of",vwtr-vtank)
elif vwtr == vtank:
    print("Tank full")
else:
    print("Under flow")
ht = vwtr/(3.14*r**2)
hr = h-ht
print(f"filled height{ht}\n remaining height{hr}")
