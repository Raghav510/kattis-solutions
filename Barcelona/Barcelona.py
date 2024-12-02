a1,a2 =[ int(c) for c in input().split()],[int(c) for c in input().split()]
i = a1[1]
p = a2.index(i)+1
print("fyrst" if p == 1 else "naestfyrst" if p == 2 else f"{p} fyrst")