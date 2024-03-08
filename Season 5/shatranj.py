def shatranj(n, m):
    for i in range(n):
        for a in range (m):
            if(i+a) % 2 ==0:
                print("🖤", end ="")
            else:
                print("🤍", end ="")
        print()

n = int(input("Enter your first number: "))
m = int(input("Enter you second number: "))
shatranj(n, m)