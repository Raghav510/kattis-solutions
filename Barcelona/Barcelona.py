a1,a2=[int(c) for c in input().split()],[int(c) for c in input().split()]
print("fyrst" if (p:=a2.index(a1[1])+1)==1 else "naestfyrst" if p==2 else f"{p} fyrst")
