n=int(input())
s=0
while n>0:
    r=n%10
    n=n//10
    if r>s:
        s=r
print(s)