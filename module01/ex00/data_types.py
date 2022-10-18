i = 8
s = "gfvdk"
f = 1.4
b = True
l = [i,s,f]
d = {'apple' : 1}
t = tuple()
s = set()


all = [i, s, f,b,l,d,t,s]
res = []
for x in all:
    res.append(type(x).__name__)
print(str(res).replace("'", ""))
