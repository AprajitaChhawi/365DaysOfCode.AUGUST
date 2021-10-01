def wordBreak(s, wordDict):
    k=''
    for i in wordDict:
        k=k+i
    n=len(s)
    m=len(k)
    j=0
    i=0
    for i in range(m):
        if k[i]==s[j]:
            j=j+1
        if j==n:
            return True
    return False
s="abcd"
l=["a","abc","b","cd"]
print(wordBreak(s,l))
