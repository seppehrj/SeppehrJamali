x = [11, 13, 15, 16, 13, 15, 16, 11]

result = []

for i in x:
    if i not in result:
        result.append(i)

print(result)