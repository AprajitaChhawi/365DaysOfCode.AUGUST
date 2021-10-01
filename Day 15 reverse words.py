def reverse(s):
    low=0
    high=len(s)-1
    while(low<high):
        s[low],s[high]=s[high],s[low]
        low=low+1
        high=high-1
    return s
s1=input()
l=list(map(str,s1.split(" ")))
l1=reverse(l)
s=''
for i in l1:
    s=s+i
    s=s+' '
print(s)
