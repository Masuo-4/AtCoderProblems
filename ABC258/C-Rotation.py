def query(s, t, x):
   if t == 1:
        s = s[-x:] + s[:-x]
        return s
   else:
       print(s[x - 1])

n, q = list(map(int, input().split()))
s = input()

query_lst = []
for i in range(q):
    query_lst.append(list(map(int, input().split()))) 

for t, x in query_lst:
    query(s, t, x)