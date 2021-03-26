Len = int(input())
lst = input().split()
for i in range(Len):
    lst[i]= int(lst[i])
start,Max = Len,0
p = range(Len)
for i in p[Len-1::-1]:
    if lst[i]==1:
        Max = i
        break
for i in range(Len):
    if lst[i]==1:
        start= i
        break
count = 0
for i in range(start,Max-1):
    if lst[i]==1:
        if lst[i+1] != 1:
            count+=1
    else:
        count+=1
print(count+1)
