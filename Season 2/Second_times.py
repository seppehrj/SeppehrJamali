h = 0
m = 0
s = 0
seconds = int(input("enter your seconds: "))
h = seconds // 3600
m = (seconds % 3600) // 60
s = (seconds % 3600) % 60
print(h, ":", m, ":", s)


print(h)