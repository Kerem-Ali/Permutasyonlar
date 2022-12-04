#2 farklı permutasyonlar
def perm1(lst):
    if len(lst)==0:
        return []
    elif len(lst)==1:
        return [lst]
    else:
        l=[]
        for i in range(len(lst)):
            x=lst[i]
            xs=lst[:i]+lst[i+1:]
            for p in perm1(xs):
                l.append([x]+p)
        return l

veri=list("abcd")
a=perm1(veri)
print("perm1")
print(len(a))

for p in perm1(veri):
    print(p)

def perm2(lst):
    if len(lst)==0:
        yield []
    elif len(lst)==1:
        yield lst
    else:
        for i in range(len(lst)):
            x=lst[i]
            xs=lst[:i]+lst[i+1:]
            for p in perm2(xs):
                yield ([x]+p)



print("perm2")


for p in perm2(veri):
    print(p)
