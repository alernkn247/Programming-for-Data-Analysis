def Sum(a,b,l):
    listNumbers = list(filter(lambda x: (((x %a==0) or (x % b ==0)) ),l))
    return sum(listNumbers)

print(Sum(3,5,list([1,2,3,4,5,6,7,8,9,10])))