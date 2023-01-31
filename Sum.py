def Sum(a:list,l:list):
    listNumbers = list(filter(lambda x: len([y for y in a if x%y==0])>0,l))
    return sum(listNumbers)

print(Sum(list([3,5,7]),list([1,2,3,4,5,6,7,8,9,10])))