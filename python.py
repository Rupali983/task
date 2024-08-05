A="python"
B=" "
for i in A:
    B = i+B
print(B)


a = "rupali"
dict = {}
for i in a:
    dict[i] = a.count(i)
print(dict)



n = int(input("Enter any number: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()  

