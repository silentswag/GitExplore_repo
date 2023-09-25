#Return the maximum K valid sum combinations from all the possible sum combinations.
a=[1,2,8,7]
b=[4,7,8,2]
for i in range(len(a)):
    list=[]
    for j in range(len(b)):
        list.append(a[i]+b[j])
    print(max(list))