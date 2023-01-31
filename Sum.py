def Sum(a,b,n):
    listNumbers = list(range(1,n+1))
    listNumbers = list(filter(lambda x: (((x %a==0) or (x % b ==0)) and x<n),listNumbers))
    return sum(listNumbers)

print(Sum(3,5,10))