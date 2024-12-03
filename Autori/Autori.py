x=input()
t = x[0]
for i in  range(len(x)):
    if x[i]== "-":
        t+= x[i+1]
print(t)
